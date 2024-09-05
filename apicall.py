import requests, json
apikey="bd43bbc45b88b7ee44599f87fcd90394"
baseURL="https://api.openweathermap.org/data/2.5/weather?q="
city=input("Enter name of the city :")
completeURL= baseURL + city + "&appid=" + apikey
response = requests.get(completeURL)
data = response.json()
print("Current temp" ,data["main"]["temp"])
print("Max temp" ,data["main"]["temp_max"])
print("Min temp" ,data["main"]["temp_min"])
print("feels like" ,data["main"]["feels_like"])

