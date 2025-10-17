import requests

city = input('Введите город: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

try:
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    description = (weather_data['weather'][0]['description'])
    print(f"Сейчас в городе {city} {description}, {temperature} °C")
except:
    print("Город не найден, попробуйте снова.")
