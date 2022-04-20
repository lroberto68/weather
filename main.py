from weather_result import get_weather

result = get_weather(city_name='Quarto', state_code='it',lang='it', type='forecast')
print(type(result))

""" for x in result:
    print (x)

print("\n")
print(f"coordinate: lon({result['coord']['lon']}) - lat({result['coord']['lat']})")
print(f"condizioni: {result['weather'][0]['main']}")
print(f"temperatura percepita: {result['main']['feels_like']}")
print(f"città: {result['name']}") """

print(result['list'])
for d in result['list']:
    print(f"città: {result['city']['name']}, {result['city']['country']} - datatime: {d['dt_txt']} - temperatura: {d['main']['temp']}° - condizione: {d['weather'][0]['description']}")