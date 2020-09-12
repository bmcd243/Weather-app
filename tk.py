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


main_frame = tk.Frame(root)

my_canvas = tk.Canvas(main_frame)

main_scrollbar = tk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)

second_frame = tk.Frame(my_canvas)

my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all"))) #<Configure> is an event that is triggered everytime my_canvas changes



my_canvas.create_window((0,0), window=second_frame, anchor="nw")
my_canvas.configure(yscrollcommand=main_scrollbar.set)

main_frame.pack(fill='both', expand=1)

my_canvas.pack(side='left', fill='both', expand=True)

main_scrollbar.pack(side='right', fill='y')

second_frame.pack()


def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)


Images = dict()


def display_photo(row=0, column=0):

	global weather_main
	global city

	if weather_main + '_tk' not in [*Images]:
		image_1 = ImageTk.PhotoImage(Image.open("./images/" + weather_main + ".jpg"))
		photo = tk.Label(second_frame, image = image_1)
		photo.image = image_1
		# photo.grid(row=2, column=8, columnspan=3)
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

	# mylabel2 = tk.Label(second_frame, text = 'URL=' + request_address)
	# mylabel2.pack()


	coordinates = api["coord"]
	weather_main = api["weather"][0]["main"]
	weather_description = api["weather"][0]["description"]
	temp = int(api["main"]["temp"])

	# mainy = tk.Label(second_frame, text = "the weather is " + weather_main)
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

	for i in range(12):
		time_store[i] = datetime.datetime.fromtimestamp(int(api["hourly"][i]["dt"]))

	intro = tk.Label(second_frame, text="Here is the forecast for " + city.capitalize() + ":")
	intro.pack()

	spacing = tk.Label(second_frame, text="")
	spacing.pack()

	class weather_data:
		def __init__(self, hour, temp, weather):
			self.hour = hour
			self.temp = temp
			self.weather = weather

	hour_1 = weather_data(str(time_store[0]), int(api["hourly"][0]["temp"]), api["hourly"][0]["weather"][0]["main"])
	hour_1 = tk.Label(second_frame, text=hour_1.hour[11:16] + "	 --> 	" + str(hour_1.temp) + "°C " + "and " + str(hour_1.weather))
	hour_1.pack()

	hour_2 = weather_data(str(time_store[1]), int(api["hourly"][1]["temp"]), api["hourly"][1]["weather"][0]["main"])
	hour_2 = tk.Label(second_frame, text=hour_2.hour[11:16] + "	 --> 	" + str(hour_2.temp) + "°C " + "and " + str(hour_2.weather))
	hour_2.pack()

	hour_3 = weather_data(str(time_store[2]), int(api["hourly"][2]["temp"]), api["hourly"][2]["weather"][0]["main"])
	hour_3 = tk.Label(second_frame, text=hour_3.hour[11:16] + "	 --> 	" + str(hour_3.temp) + "°C " + "and " + str(hour_3.weather))
	hour_3.pack()

	hour_4 = weather_data(str(time_store[3]), int(api["hourly"][3]["temp"]), api["hourly"][3]["weather"][0]["main"])
	hour_4 = tk.Label(second_frame, text=hour_4.hour[11:16] + "	 --> 	" + str(hour_4.temp) + "°C " + "and " + str(hour_4.weather))
	hour_4.pack()

	hour_5 = weather_data(str(time_store[4]), int(api["hourly"][4]["temp"]), api["hourly"][4]["weather"][0]["main"])
	hour_5 = tk.Label(second_frame, text=hour_5.hour[11:16] + "	 --> 	" + str(hour_5.temp) + "°C " + "and " + str(hour_5.weather))
	hour_5.pack()

	hour_6 = weather_data(str(time_store[5]), int(api["hourly"][5]["temp"]), api["hourly"][5]["weather"][0]["main"])
	hour_6 = tk.Label(second_frame, text=hour_6.hour[11:16] + "	 --> 	" + str(hour_6.temp) + "°C " + "and " + str(hour_6.weather))
	hour_6.pack()

	hour_7 = weather_data(str(time_store[6]), int(api["hourly"][6]["temp"]), api["hourly"][6]["weather"][0]["main"])
	hour_7 = tk.Label(second_frame, text=hour_7.hour[11:16] + "	 --> 	" + str(hour_7.temp) + "°C " + "and " + str(hour_7.weather))
	hour_7.pack()

	hour_8 = weather_data(str(time_store[7]), int(api["hourly"][7]["temp"]), api["hourly"][7]["weather"][0]["main"])
	hour_8 = tk.Label(second_frame, text=hour_8.hour[11:16] + "	 --> 	" + str(hour_8.temp) + "°C " + "and " + str(hour_8.weather))
	hour_8.pack()

	hour_9 = weather_data(str(time_store[8]), int(api["hourly"][8]["temp"]), api["hourly"][8]["weather"][0]["main"])
	hour_9 = tk.Label(second_frame, text=hour_9.hour[11:16] + "	 --> 	" + str(hour_9.temp) + "°C " + "and " + str(hour_9.weather))
	hour_9.pack()

	hour_10 = weather_data(str(time_store[9]), int(api["hourly"][9]["temp"]), api["hourly"][9]["weather"][0]["main"])
	hour_10 = tk.Label(second_frame, text=hour_10.hour[11:16] + "	 --> 	" + str(hour_10.temp) + "°C " + "and " + str(hour_10.weather))
	hour_10.pack()

	hour_11 = weather_data(str(time_store[10]), int(api["hourly"][10]["temp"]), api["hourly"][10]["weather"][0]["main"])
	hour_11 = tk.Label(second_frame, text=hour_11.hour[11:16] + "	 --> 	" + str(hour_11.temp) + "°C " + "and " + str(hour_11.weather))
	hour_11.pack()

	hour_12 = weather_data(str(time_store[11]), int(api["hourly"][11]["temp"]), api["hourly"][11]["weather"][0]["main"])
	hour_12 = tk.Label(second_frame, text=hour_12.hour[11:16] + "	 --> 	" + str(hour_12.temp) + "°C " + "and " + str(hour_12.weather))
	hour_12.pack()

	print (request_address)


def minute():
	global city

	minute_frame = tk.Frame(second_frame)
	minute_scrollbar = tk.Scrollbar(minute_frame, orient='vertical', command=my_canvas.yview)

	city = e.get()
	geo_address = "http://www.mapquestapi.com/geocoding/v1/address?key=BYpND8FnPOffqVr9AUAYb3flHyCWLeLk&location=" + city
	geo_request = requests.get(geo_address)
	geo_api = json.loads(geo_request.content)

	lat_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lat"]
	long_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lng"]

	request_address = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat_coordinates) + "&lon=" + str(long_coordinates) + "&exclude=hourly,daily&units=metric&appid=0a0699452f695d2f9f82b65af024a134"
	api_request = requests.get(request_address)
	api = json.loads(api_request.content)

	print(request_address)



	listbox = tk.Listbox(minute_frame, width=20, height=500, yscrollcommand=minute_scrollbar.set)
	for i in range(60):
		time_store = datetime.datetime.fromtimestamp(int(api["minutely"][i]["dt"]))
		time_store_string = str(time_store)
		precip_store = int(api["minutely"][i]["precipitation"])
		listbox.insert(i-1, time_store_string[11:16] + "	-->		" + str(precip_store) + "%")

	listbox.pack(fill='both')
	minute_scrollbar.config(command=listbox.yview)

	minute_frame.pack()
	listbox.pack(pady=15)
	minute_scrollbar.pack(side='right', fill='y')
	
	










def daily():

	daily_frame = tk.Frame(second_frame)
	daily_scrollbar = tk.Scrollbar(daily_frame)


	city = e.get()
	geo_address = "http://www.mapquestapi.com/geocoding/v1/address?key=BYpND8FnPOffqVr9AUAYb3flHyCWLeLk&location=" + city
	geo_request = requests.get(geo_address)
	geo_api = json.loads(geo_request.content)

	lat_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lat"]
	long_coordinates = geo_api["results"][0]["locations"][0]["latLng"]["lng"]

	request_address = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat_coordinates) + "&lon=" + str(long_coordinates) + "&exclude=hourly,minutely&units=metric&appid=0a0699452f695d2f9f82b65af024a134"
	api_request = requests.get(request_address)
	api = json.loads(api_request.content)

	print(request_address)

	class daily_data:
			def __init__(self, mini, maxi, weather):
				self.mini = mini
				self.max = maxi
				self.weather = weather


	# time_store = datetime.datetime.fromtimestamp(int(api["daily"][i]["dt"]))

		listbox = tk.Listbox(daily_frame, width=20, height=500, yscrollcommand=daily_scrollbar.set)
		for i in range(10):
		dt_store = datetime.datetime.fromtimestamp(int(api["daily"][i]["dt"]))
		day_store_string = str(dt_store)
		listbox.insert(END, day_store_string)

	daily_frame.pack()
	listbox.pack(pady=15)
	daily_scrollbar.config(command=listbox.yview)
	minute_scrollbar.pack(side='right', fill='y')
		
		

def text_runner():

	mylabel = tk.Label(second_frame, text = "The weather in " + city + " is " + weather_main + " and the temperature is " + str(temp) + "°C", font=("Helvetica", 20))
	mylabel.pack()



# START_OF_PROGRAM

info = tk.Label(second_frame, text="Press Restart to clear the screen.")
info.pack()


restarter = ttk.Button(second_frame, text="Restart", command=restart)
restarter.pack()

title = tk.Label(second_frame, text="Enter a city below:")
title.pack()

e = tk.Entry(second_frame)
e.pack()

def yes_no_current():
	if len(e.get()) == 0:
		null_entry = tk.Label(second_frame, text="Please enter a city above")
		null_entry.pack()
	else:
		current()

def yes_no_hourly():
	if len(e.get()) == 0:
		null_entry = tk.Label(second_frame, text="Please enter a city above")
		null_entry.pack()
	else:
		hourly()

def yes_no_minute():
	if len(e.get()) == 0:
		null_entry = tk.Label(second_frame, text="Please enter a city above")
		null_entry.pack()
	else:
		minute()

def yes_no_daily():
	if len(e.get()) == 0:
		null_entry = tk.Label(second_frame, text="Please enter a city above")
		null_entry.pack()
	else:
		daily()


current_clicker = ttk.Button(second_frame, text = "Current forecast", command=yes_no_current)
current_clicker.pack()


hourly_clicker = ttk.Button(second_frame, text = "By hour", command=yes_no_hourly)
hourly_clicker.pack()


minute_clicker = ttk.Button(second_frame, text = "By minute", command=yes_no_minute)
minute_clicker.pack()


daily_clicker = ttk.Button(second_frame, text = "Daily", command=yes_no_daily)
daily_clicker.pack()

# print(daily_clicker.grid_size())


second_frame.mainloop()