import requests

def get_check_text(text, language="auto"):
    
    url = "https://api.languagetool.org/v2/check"
    
    data = {
        'text': text,
        'language': language
    }

    response = requests.post(url=url, data=data)
    return response.text