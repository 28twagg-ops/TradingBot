"""Safe GitHub diagnostics for free Groq model access. Never print credentials."""
import json
import os
import urllib.request
import urllib.error

KEY=os.environ.get("GROQ_API_KEY","").strip()
BASE="https://api.groq.com/openai/v1/"
def status_of(exc):
    kind=exc.headers.get("Content-Type","").split(";",1)[0]
    try:
        blob=exc.read(2048).decode("utf8","replace")
    except Exception:
        blob=""
    known=["model_permission_blocked_project","model_permission_blocked_org",
           "permissions_error","authentication_error","invalid_api_key",
           "rate_limit_exceeded","model_decommissioned","access_denied"]
    markers=[item for item in known if item in blob]
    return f"HTTP_{exc.code} content_type={kind[:35]} categories={','.join(markers) or 'unclassified'}"

def main():
    if not KEY:
        print("Groq: API key not configured")
        return
    common={"Authorization":"Bearer "+KEY,"Content-Type":"application/json"}
    available=[]
    req=urllib.request.Request(BASE+"models",headers=common)
    try:
        with urllib.request.urlopen(req,timeout=15) as response:
            result=json.load(response)
            available=[m.get("id") for m in result.get("data",[]) if isinstance(m,dict)]
        print("Groq GET /models: OK; GPT-OSS 20B listed:", "openai/gpt-oss-20b" in available,
              "; Llama 3.1 8B listed:", "llama-3.1-8b-instant" in available)
    except urllib.error.HTTPError as exc:
        print("Groq GET /models:",status_of(exc))
    except Exception as exc:
        print("Groq GET /models: transport failure",type(exc).__name__)
    if "llama-3.1-8b-instant" not in available:
        print("Groq lightweight model probe skipped: model unavailable or model list inaccessible")
        return
    body={"model":"llama-3.1-8b-instant",
          "messages":[{"role":"user","content":"Return a JSON object with the boolean ok set true."}],
          "response_format":{"type":"json_object"},
          "max_tokens":35, "temperature":0}
    req=urllib.request.Request(BASE+"chat/completions",headers=common,method="POST",data=json.dumps(body).encode())
    try:
        with urllib.request.urlopen(req,timeout=20) as response:
            j=json.load(response)
        success=bool(j.get("choices"))
        print("Groq minimal Llama completion:", "SUCCESS" if success else "EMPTY_RESPONSE")
    except urllib.error.HTTPError as exc:
        print("Groq minimal Llama completion:",status_of(exc))
    except Exception as exc:
        print("Groq minimal Llama completion: transport failure",type(exc).__name__)

if __name__=="__main__":
    main()
