import tkinter as tk
import requests
import json
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("800x600")
# root.configure(bg = 'black')

# root.iconbitmap('./images/rain_jpeg.jpg')

Images = dict()

def display_photo(row=0, column=0):

	if weather_main + '_tk' not in [*Images]:
		image_1 = ImageTk.PhotoImage(Image.open("./images/" + weather_main + ".jpg"))
		photo = tk.Label(root, image = image_1)
		photo.image = image_1
		photo.pack()

	text_runner()


	


def city_clicker_runner():
	
	global weather_main
	global city

	city = e.get()
	request_address = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=0a0699452f695d2f9f82b65af024a134"
	api_request = requests.get(request_address)
	api = json.loads(api_request.content)

	mylabel2 = tk.Label(root, text = 'URL=' + request_address)
	# mylabel2.configure(foreground="white")
	mylabel2.pack()


	coordinates = api["coord"]
	weather_main = api["weather"][0]["main"]
	weather_description = api["weather"][0]["description"]
	temp = int(api["main"]["temp"])

	mainy = tk.Label(root, text = "the weather is " + weather_main)
	mainy.pack()

	display_photo()
		

def text_runner():

	running = tk.Label(root, text = 'we are running')
	running.pack()

	mylabel = tk.Label(root, text = "The weather in " + city + " is " + weather_main + " and the temperature is " + str(temp), font=("Helvetica", 20))
	mylabel.pack()


	


e = tk.Entry(root)
e.pack()

city_clicker = tk.Button(root, text = "GO", command=city_clicker_runner)
city_clicker.pack()