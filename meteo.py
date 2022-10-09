import requests

city = "Moscow,RU"
appid = "bde816a9134cfdfb0d91449aba12c8f8"


res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print("Город:", data['name'])
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Давление:", data['main']['pressure'])
print("Скор.ветра:", data['wind']['speed'])
print("Температура по ощущениям:", data['main']['feels_like'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])