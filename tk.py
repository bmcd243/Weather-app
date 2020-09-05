import tkinter as tk
import os
import sys
from tkinter import ttk
import requests
import json
from PIL import ImageTk, Image
import datetime

root = tk.Tk()
root.geometry("800x600")
root.title("Weather app")
# root.configure(bg = 'black')
root.iconbitmap('./images/rain.jpg')

Images = dict()

def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)



def display_photo(row=0, column=0):

	global weather_main
	global city

	if weather_main + '_tk' not in [*Images]:
		image_1 = ImageTk.PhotoImage(Image.open("./images/" + weather_main + ".jpg"))
		photo = tk.Label(root, image = image_1)
		photo.image = image_1
		photo.grid(row=2, column=8, columnspan=3)
		photo.pack()

	text_runner()


	


def current():
	
	global weather_main
	global city
	global coordinates
	global weather_description
	global temp

	city = e.get()
	request_address = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=0a0699452f695d2f9f82b65af024a134"
	api_request = requests.get(request_address)
	api = json.loads(api_request.content)

	# mylabel2 = tk.Label(root, text = 'URL=' + request_address)
	# mylabel2.pack()


	coordinates = api["coord"]
	weather_main = api["weather"][0]["main"]
	weather_description = api["weather"][0]["description"]
	temp = int(api["main"]["temp"])

	# mainy = tk.Label(root, text = "the weather is " + weather_main)
	# mainy.pack()

	display_photo()

def hourly():

	global city

	city = e.get()
	geo_address = "http://www.mapquestapi.com/geocoding/v1/address?key=BYpND8FnPOffqVr9AUAYb3flHyCWLeLk&location=" + city
	geo_request = requests.get(geo_address)
	geo_api = json.loads(geo_request.content)

	print(geo_address)

	lat_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lat"]
	long_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lng"]

	request_address = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat_coordinates) + "&lon=" + str(long_coordinates) + "&exclude=minutely,daily&units=metric&appid=0a0699452f695d2f9f82b65af024a134"
	api_request = requests.get(request_address)
	api = json.loads(api_request.content) #returns as a string
	print(api)

	time_store = dict()

	for i in range(12):
		time_store[i] = datetime.datetime.fromtimestamp(int(api["hourly"][i]["dt"]))
	print (time_store)

	intro = tk.Label(root, text="Here is the forecast for " + city.capitalize())
	intro.pack()

	class weather_data:
		def __init__(self, hour, temp, weather):
			self.hour = hour
			self.temp = temp
			self.weather = weather

	hour_1 = weather_data(str(time_store[0]), int(api["hourly"][0]["temp"]), api["hourly"][0]["weather"][0]["main"])
	hour_1 = tk.Label(root, text=hour_1.hour[11:16] + "	 --> 	" + str(hour_1.temp) + "°C " + "with " + str(hour_1.weather))
	hour_1.pack()

	hour_2 = weather_data(str(time_store[1]), int(api["hourly"][1]["temp"]), api["hourly"][1]["weather"][0]["main"])
	hour_2 = tk.Label(root, text=hour_2.hour[11:16] + "	 --> 	" + str(hour_2.temp) + "°C " + "with " + str(hour_2.weather))
	hour_2.pack()

	hour_3 = weather_data(str(time_store[2]), int(api["hourly"][2]["temp"]), api["hourly"][2]["weather"][0]["main"])
	hour_3 = tk.Label(root, text=hour_3.hour[11:16] + "	 --> 	" + str(hour_3.temp) + "°C " + "with " + str(hour_3.weather))
	hour_3.pack()

	hour_4 = weather_data(str(time_store[3]), int(api["hourly"][3]["temp"]), api["hourly"][3]["weather"][0]["main"])
	hour_4 = tk.Label(root, text=hour_4.hour[11:16] + "	 --> 	" + str(hour_4.temp) + "°C " + "with " + str(hour_4.weather))
	hour_4.pack()

	hour_5 = weather_data(str(time_store[4]), int(api["hourly"][4]["temp"]), api["hourly"][4]["weather"][0]["main"])
	hour_5 = tk.Label(root, text=hour_5.hour[11:16] + "	 --> 	" + str(hour_5.temp) + "°C " + "with " + str(hour_5.weather))
	hour_5.pack()

	hour_6 = weather_data(str(time_store[5]), int(api["hourly"][5]["temp"]), api["hourly"][5]["weather"][0]["main"])
	hour_6 = tk.Label(root, text=hour_6.hour[11:16] + "	 --> 	" + str(hour_6.temp) + "°C " + "with " + str(hour_6.weather))
	hour_6.pack()

	hour_7 = weather_data(str(time_store[6]), int(api["hourly"][6]["temp"]), api["hourly"][6]["weather"][0]["main"])
	hour_7 = tk.Label(root, text=hour_7.hour[11:16] + "	 --> 	" + str(hour_7.temp) + "°C " + "with " + str(hour_7.weather))
	hour_7.pack()

	hour_8 = weather_data(str(time_store[7]), int(api["hourly"][7]["temp"]), api["hourly"][7]["weather"][0]["main"])
	hour_8 = tk.Label(root, text=hour_8.hour[11:16] + "	 --> 	" + str(hour_8.temp) + "°C " + "with " + str(hour_8.weather))
	hour_8.pack()

	hour_9 = weather_data(str(time_store[8]), int(api["hourly"][8]["temp"]), api["hourly"][8]["weather"][0]["main"])
	hour_9 = tk.Label(root, text=hour_9.hour[11:16] + "	 --> 	" + str(hour_9.temp) + "°C " + "with " + str(hour_9.weather))
	hour_9.pack()

	hour_10 = weather_data(str(time_store[9]), int(api["hourly"][9]["temp"]), api["hourly"][9]["weather"][0]["main"])
	hour_10 = tk.Label(root, text=hour_10.hour[11:16] + "	 --> 	" + str(hour_10.temp) + "°C " + "with " + str(hour_10.weather))
	hour_10.pack()

	hour_11 = weather_data(str(time_store[10]), int(api["hourly"][10]["temp"]), api["hourly"][10]["weather"][0]["main"])
	hour_11 = tk.Label(root, text=hour_11.hour[11:16] + "	 --> 	" + str(hour_11.temp) + "°C " + "with " + str(hour_11.weather))
	hour_11.pack()

	hour_12 = weather_data(str(time_store[11]), int(api["hourly"][11]["temp"]), api["hourly"][11]["weather"][0]["main"])
	hour_12 = tk.Label(root, text=hour_12.hour[11:16] + "	 --> 	" + str(hour_12.temp) + "°C " + "with " + str(hour_12.weather))
	hour_12.pack()

	# hour_2_string = str(time_store[1])
	# temp_2_string = int(api["hourly"][1]["temp"])
	# weather_2_string = api["hourly"][1]["weather"][0]["main"]
	# hour_2 = tk.Label(root, text=hour_2_string[11:16] + "	 --> 	" + str(temp_2_string) + "°C " + "with " + str(weather_2_string))
	# hour_2.pack()

	# hour_3_string = str(time_store[2])
	# temp_3_string = int(api["hourly"][2]["temp"])
	# weather_3_string = api["hourly"][2]["weather"][0]["main"]
	# hour_3 = tk.Label(root, text=hour_3_string[11:16] + "	 --> 	" + str(temp_3_string) + "°C " + "with " + str(weather_3_string))
	# hour_3.pack()

	# hour_4_string = str(time_store[3])
	# temp_4_string = int(api["hourly"][3]["temp"])
	# weather_4_string = api["hourly"][3]["weather"][0]["main"]
	# hour_4 = tk.Label(root, text=hour_4_string[11:16] + "	 --> 	" + str(temp_4_string) + "°C " + "with " + str(weather_4_string))
	# hour_4.pack()

	# hour_5_string = str(time_store[4])
	# temp_5_string = int(api["hourly"][4]["temp"])
	# weather_5_string = api["hourly"][4]["weather"][0]["main"]
	# hour_5 = tk.Label(root, text=hour_5_string[11:16] + "	 --> 	" + str(temp_5_string) + "°C " + "with " + str(weather_5_string))
	# hour_5.pack()

	# hour_6_string = str(time_store[5])
	# temp_6_string = int(api["hourly"][5]["temp"])
	# weather_6_string = api["hourly"][5]["weather"][0]["main"]
	# hour_6 = tk.Label(root, text=hour_6_string[11:16] + "	 --> 	" + str(temp_6_string) + "°C " + "with " + str(weather_6_string))
	# hour_6.pack()

	# hour_7_string = str(time_store[6])
	# temp_7_string = int(api["hourly"][6]["temp"])
	# weather_7_string = api["hourly"][6]["weather"][0]["main"]
	# hour_7 = tk.Label(root, text=hour_7_string[11:16] + "	 --> 	" + str(temp_7_string) + "°C " + "with " + str(weather_7_string))
	# hour_7.pack()

	# hour_8_string = str(time_store[7])
	# temp_8_string = int(api["hourly"][7]["temp"])
	# weather_8_string = api["hourly"][7]["weather"][0]["main"]
	# hour_8 = tk.Label(root, text=hour_8_string[11:16] + "	 --> 	" + str(temp_8_string) + "°C " + "with " + str(weather_8_string))
	# hour_8.pack()

	# hour_9_string = str(time_store[8])
	# temp_9_string = int(api["hourly"][8]["temp"])
	# weather_9_string = api["hourly"][8]["weather"][0]["main"]
	# hour_9 = tk.Label(root, text=hour_9_string[11:16] + "	 --> 	" + str(temp_9_string) + "°C " + "with " + str(weather_9_string))
	# hour_9.pack()

	# hour_10_string = str(time_store[9])
	# temp_10_string = int(api["hourly"][9]["temp"])
	# weather_10_string = api["hourly"][9]["weather"][0]["main"]
	# hour_10 = tk.Label(root, text=hour_10_string[11:16] + "	 --> 	" + str(temp_10_string) + "°C " + "with " + str(weather_10_string))
	# hour_10.pack()

	# hour_11_string = str(time_store[10])
	# temp_11_string = int(api["hourly"][10]["temp"])
	# weather_11_string = api["hourly"][10]["weather"][0]["main"]
	# hour_11 = tk.Label(root, text=hour_11_string[11:16] + "	 --> 	" + str(temp_11_string) + "°C " + "with " + str(weather_11_string))
	# hour_11.pack()

	# hour_12_string = str(time_store[11])
	# temp_12_string = int(api["hourly"][11]["temp"])
	# weather_12_string = api["hourly"][11]["weather"][0]["main"]
	# hour_12 = tk.Label(root, text=hour_12_string[11:16] + "	 --> 	" + str(temp_12_string) + "°C " + "with " + str(weather_12_string))
	# hour_12.pack()

	print (request_address)


def minute():
	empty = ""

def daily():
	empty = ""
		

def text_runner():

	mylabel = tk.Label(root, text = "The weather in " + city + " is " + weather_main + " and the temperature is " + str(temp) + "°C", font=("Helvetica", 20))
	mylabel.pack()


restarter = ttk.Button(root, text="Restart", command=restart)
restarter.pack()

title = tk.Label(root, text="Enter a city below")
# title.grid(row=0, column=5)
restarter.pack()


e = tk.Entry(root)
# e.grid(row = 1, column = 5)
e.pack()


current_clicker = ttk.Button(root, text = "Current forecast", command=current)
# current_clicker.grid(row=2, column=4)
current_clicker.pack()


hourly_clicker = ttk.Button(root, text = "By hour", command=hourly)
# hourly_clicker.grid(row=2, column=5)
hourly_clicker.pack()


minute_clicker = ttk.Button(root, text = "By minute", command=minute)
# minute_clicker.grid(row=2, column=6)
minute_clicker.pack()


daily_clicker = ttk.Button(root, text = "Daily", command=daily)
# daily_clicker.grid(row=2, column=7)
daily_clicker.pack()

# print(daily_clicker.grid_size())


root.mainloop()