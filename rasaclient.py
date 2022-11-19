import requests


def rasaint(text):
    payload1 = {'text':text}
    headers = {'content-type': 'application/json'}
    r = requests.post('http://192.168.1.5:5005/model/parse', json=payload1, headers=headers)
    intent = r.json()['intent']
    entities = r.json()['entities']
    return(intent,entities)
    
def rasatext(text):
    headers = {'content-type': 'application/json'}
    payload2 = {"sender": "abdo", "message": text}
    y = requests.post('http://192.168.1.5:5005/webhooks/rest/webhook', json=payload2, headers=headers)
    response = y.json()
    return (response)

def ga(text):
    x = requests.get("http://0.0.0.0:4000/index?source="+text)
    print(x)
    
def say(text):
    url = 'http://0.0.0.0:6000/index?source='+text
    resp = requests.get(url)
    
    
