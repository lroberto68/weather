from multiprocessing.sharedctypes import Value
from weather_result import get_weather
from language_check import get_check_text
import json

result = get_weather(city_name='Pozzuoli', state_code='it',lang='it', type='forecast')
print(type(result))

for x in result:
    print (x)

""" print("\n")
print(f"coordinate: lon({result['coord']['lon']}) - lat({result['coord']['lat']})")
print(f"condizioni: {result['weather'][0]['main']}")
print(f"temperatura percepita: {result['main']['feels_like']}")
print(f"città: {result['name']}") """

print(result['list'])

with open("data.txt", "w") as file:
    file.write(f"City,Time,Temperature,Condition\n")
    for d in result['list']:
        record=f"città: {result['city']['name']}, {result['city']['country']} - datatime: {d['dt_txt']} - temperatura: {d['main']['temp']}° - condizione: {d['weather'][0]['description']}\n"
        file.write(record)

""" text = "Tis is a nixe day"
language = 'auto'
result_check = json.loads(get_check_text(text, language))
print(type(result_check))
#print (result_check)
for k,v in result_check.items():
    print(f"{k} - {v}\n") """