import requests

def get_weather(city_name, state_code, type='forecast', units='metric', lang='en', API_key='e951cc49db5aceebd4adf02682644335'):

    url = f'http://api.openweathermap.org/data/2.5/{type}?q={city_name},{state_code}&units={units}&lang={lang}&appid={API_key}'
    r = requests.get(url)
    result = r.json()
    return result
