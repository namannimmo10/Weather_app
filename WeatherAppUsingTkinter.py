import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 800

#passing in the json received from the API
def get_response(weather):
    try:
        name_of_city = weather['name']
        # print(name_of_city)
        description = weather['weather'][0]['description']
        # print(description)   
        temp = weather['main']['temp']
        return "The name of the city: {}\nTemperature: {} Degree celsius\nDescription: {}".format(name_of_city,temp,description)
    except:
        return "there is some problem in getting the information!"

def get_the_weather(city):
    weather_key = '286c1a921db08ce5971c879b7671efce'
    #get your own key

    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    # using Metric because we want the weather in degree celsius
    # To get weather in fahrenheit --> Imperial
    
    response = requests.get(url, params = parameters)
    weather = response.json()
    label['text'] = get_response(weather)
    

root = tk.Tk()
#main code starts from here
root.title('Weather App')

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = "#FA8072", bd = 7)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.8, relheight=0.1, anchor ='n')

entry = tk.Entry(frame, font=70)
entry.place(relwidth = 0.7, relheight = 1)

button = tk.Button(frame, text = "How's the weather??", font = 70, command=lambda: get_the_weather(entry.get()))
button.place(relx = 0.72, relheight = 1, relwidth = 0.275)

lower_frame = tk.Frame(root, bd = 1)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.8, relheight=0.6, anchor ='n')

label = tk.Label(lower_frame, font = ('Rasa',25))
label.place(relwidth=1, relheight=1)

root.mainloop()
