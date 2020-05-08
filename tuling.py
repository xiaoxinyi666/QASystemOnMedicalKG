import requests
import json
import os

tuling_apikey = os.getenv('tuling_apikey',"55446545110f4a5e95c6167b5235dc32")
userId='xiaoxinyi'
def visit_tuling(msg):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
        "perception": {
            "inputText": {
                "text": msg
            }
        },

        "userInfo": {
            "apiKey": tuling_apikey,
            "userId":userId
        }
    }
    dat = json.dumps(dat)
    r = requests.post(api, data=dat).json()
    message = r['results'][0]['values']['text']
    print(r['results'][0]['values']['text'])
    return message
