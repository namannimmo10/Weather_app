import os
import sys
import requests
import tkinter as tk

from tkinter import font

WEATHER_KEY = os.getenv('WEATHER_APP_KEY')
if WEATHER_KEY is None:
    print("Weather key env variable not set.", file=sys.stderr)
    quit(1)

URL = 'https://api.openweathermap.org/data/2.5/weather'

HEIGHT = 500
WIDTH = 800


def get_response(weather):
    """Parse the API response into a presentable string"""
    try:
        name_of_city = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        return "The name of the city: {}\nTemperature: {} Degree celsius\nDescription: {}".format(
            name_of_city, temp, description
        )
    except:
        return "there is some problem in getting the information!"


def get_the_weather(city):
    parameters = {'APPID': WEATHER_KEY, 'q': city, 'units': 'Metric'}
    # using Metric because we want the weather in degree celsius
    # To get weather in fahrenheit --> Imperial

    response = requests.get(URL, params=parameters)
    weather = response.json()
    label['text'] = get_response(weather)


root = tk.Tk()
#main code starts from here
root.title('Weather App')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#FA8072", bd=7)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=70)
entry.place(relwidth=0.7, relheight=1)

button = tk.Button(
    frame,
    text="How's the weather??",
    font=70,
    command=lambda: get_the_weather(entry.get())
)
button.place(relx=0.72, relheight=1, relwidth=0.275)

lower_frame = tk.Frame(root, bd=1)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Rasa', 25))
label.place(relwidth=1, relheight=1)

root.mainloop()
