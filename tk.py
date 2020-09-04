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

	lat_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lat"]
	long_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lng"]

	request_address = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat_coordinates) + "&lon=" + str(long_coordinates) + "&exclude=minutely,daily&units=metric&appid=0a0699452f695d2f9f82b65af024a134"
	api_request = requests.get(request_address)
	api = json.loads(api_request.content) #returns as a string

	time_store = dict()

	for i in range(5):
		time_store[i] = datetime.datetime.fromtimestamp(int(api["hourly"][i]["dt"]))
	print (time_store)


	hour_1_string = str(time_store[0])
	hour_1 = tk.Label(root, text=hour_1_string[11:16])
	hour_1.pack()

	hour_2_string = str(time_store[1])
	hour_2 = tk.Label(root, text=hour_2_string[11:16])
	hour_2.pack()

	hour_3_string = str(time_store[2])
	hour_3 = tk.Label(root, text=hour_3_string[11:16])
	hour_3.pack()

	hour_4_string = str(time_store[3])
	hour_4 = tk.Label(root, text=hour_4_string[11:16])
	hour_4.pack()

	hour_5_string = str(time_store[4])
	hour_5 = tk.Label(root, text=hour_5_string[11:16])
	hour_5.grid(row=0, column=0)
	hour_5.pack()


	print (request_address)


def minute():
	empty = ""

def daily():
	empty = ""
		

def text_runner():

	mylabel = tk.Label(root, text = "The weather in " + city + " is " + weather_main + " and the temperature is " + str(temp) + "°C", font=("Helvetica", 20))
	mylabel.pack()


restarter = ttk.Button(root, text="restart", command=restart)
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