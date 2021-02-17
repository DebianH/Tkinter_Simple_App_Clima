from tkinter import *
import requests
import time

#No olvides intalar la libreria requests para las peticiones a la API

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=7f7896b6e0a75278efcecc02533e7135 <= Formato de peticion GET

def mostrar_Peticion(clima):
	try:
		nombre_ciudad = clima["name"]
		descrip = clima["weather"][0]["description"].capitalize()
		temp = clima["main"]["temp"]
		ahora = time.strftime("%H:%M:%S")

		ciudad["text"] = nombre_ciudad
		temperatura["text"] = str(int(temp)) + "°C"
		detalle["text"] =  descrip
		fecha["text"] = "Hora: " + ahora
	except:
		ciudad["text"] = "Intenta nuevamente"


#Vamos a utilizar la Api de https://openweathermap.org/

def obtener_Json(ciudad):
	try:
		Api_key = "7f7896b6e0a75278efcecc02533e7135"
		URL = "https://api.openweathermap.org/data/2.5/weather"
		parametres = {"q": ciudad, "APPID" : Api_key, "units":"metric", "lang":"es"}
		respuesta = requests.get(URL, params = parametres)
		clima = respuesta.json()
		mostrar_Peticion(clima)
	except:
		print("Error")

#Tkinter como interfaz grafica

ventana = Tk()
ventana.title("App Clima")
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 18, "normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "Obtener clima", font = ("device", 20, "normal"), command = lambda: obtener_Json(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("Courier", 20, "normal"))
ciudad.pack(padx = 20, pady = 20)

temperatura = Label(font = ("Courier", 50, "normal"))
temperatura.pack(padx = 10, pady = 10)

detalle = Label(font = ("Courier", 20, "normal"))
detalle.pack(padx = 10, pady = 10)

fecha = Label(font = ("Courier", 10, "normal"))
fecha.pack(padx = 15, pady = 15)

ventana.mainloop()
