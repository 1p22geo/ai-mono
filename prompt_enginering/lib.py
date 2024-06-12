import requests
import json

def ai(system, prompt, model="mistral"):
    q = {
        "model": model,
        "raw": False,
        "system": system,
        "prompt": prompt,
        "stream":False
    }

    req = requests.post("http://minisforum:9000/api/generate", json.dumps(q))
    res = req.json()
    answer = res["response"]
    return answer

def raw(prompt, model="mistral"):
    q = {
        "model": model,
        "raw": True,
        "prompt": prompt,
        "stream":False
    }

    req = requests.post("http://minisforum:9000/api/generate", json.dumps(q))
    res = req.json()
    answer = res["response"]
    return answer
