import requests

from setting import OAUTH_TOKEN

req = {
    "model": "general",
    "instruction_uri": "ds://<идентификатор_дообученной_модели>",
    "request_text": "Привет",
    "generation_options": {
        "max_tokens": 1000,
        "temperature": 0.1
    }
}
headers = {'Authorization': 'Bearer ' + OAUTH_TOKEN}
res = requests.post("https://llm.api.cloud.yandex.net/llm/v1alpha/instruct",
                    headers=headers, json=req)
print(res.json())
