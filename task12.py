import requests, json

key = "5dbf46a909cfff899165d41970d482bc"

cityname = input("Enter city name : ")

url = "http://api.openweathermap.org/data/2.5/weather?appid=" + key + "&q=" + cityname

response = requests.get(url)

x = response.json()

if x["cod"] != "404":
  y = x["main"]
  temperature = y["temp"]
  pressure = y["pressure"]
  humidity = y["humidity"]
  z = x["weather"]
  weatherdescription = z[0]["description"]
  print(" Temperature (in kelvin unit) = " +str(temperature) +"\n atmospheric pressure (in hPa unit) = " +str(pressure) +"\n humidity (in percentage) = " +str(humidity) +"\n description = " +str(weatherdescription))
else:
	print(" City Not Found ")