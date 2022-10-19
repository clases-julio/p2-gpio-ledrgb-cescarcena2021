'''-----------------------------------------------------------------------------
File: ledRGB.py
Author: Carlos Escarcena y Sergio Robledo
Date: 19/10/2022
Goal: Programacion de un ledRGB
-----------------------------------------------------------------------------'''
import time, sys
import RPi.GPIO as GPIO

rojoPin = 11
azulPin = 13
verdePin = 15

#------Funciones para configurar los colores------#

def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def encenderRojo():
    encender(rojoPin)
    
def encenderVerde():
    encender(verdePin)

def encenderAzul():
    encender(azulPin)
    
def apagarRojo():
    apagar(rojoPin)
    
def apagarVerde():
    apagar(verdePin)

def apagarAzul():
    apagar(azulPin)
    
def encenderMagenta():
    encender(azulPin)
    encender(rojoPin)

def encenderCyan():
    encender(azulPin)
    encender(verdePin)

def encenderAmarillo():
    encender(rojoPin)
    encender(verdePin)
    
def encenderBlanco():
    encender(rojoPin)
    encender(verdePin)
    encender(azulPin)
    
#-----Zona de declaracion de variables------#
    
color = input("Escoge un color para encender el LED...\n")
mensaje = "Pulsa enter si quieres apagar el led "

#----------Main-----------#

if color == "rojo":
	encenderRojo()
	input(mensaje) 
	GPIO.cleanup ()
elif color == "verde":
	encenderVerde()
	input(mensaje) 
	GPIO.cleanup ()
elif color == "azul":
	encenderAzul()
	input(mensaje) 
	GPIO.cleanup ()
elif color == "magenta":
	encenderMagenta()
	input(mensaje) 
	GPIO.cleanup ()
elif color == "cyan":
	encenderCyan()
	input(mensaje) 
	GPIO.cleanup ()
elif color == "amarillo":
	encenderAmarillo()
	input(mensaje) 
	GPIO.cleanup ()
elif color == "blanco":
	encenderBlanco()
	input(mensaje) 
	GPIO.cleanup ()
	
elif color == "colores":
	print("Los colores que puede reproducir este led son: rojo\n verde\n azul\n magenta\n cyan\n amarillo\n blanco\n")

else:
	print("El color escrito no es valido, escribe colores como argumento para saber los posobles colores")




        

    
