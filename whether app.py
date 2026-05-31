import requests
api_key ="d2700fc4e66ead375e8d27f7a5b97873"
city = input("enter city name:")
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data =response.json()

if data["cod"]==200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    
    print("\n weather details:")
    print("city:",city)
    print("tempreture:",temp,"°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)
else:
    print("❌ City not found!")
                   