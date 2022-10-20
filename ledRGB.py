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

#------Funciones para configurar los ordenes------#

def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.setwarnings(False)
    
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    GPIO.setwarnings(False)
    
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
    
orden = input("Escoge una orden para que se ejecute en el LED...\n")
true = True

#----------Main-----------#
while true:

	if orden == "encender rojo":
		encenderRojo() 
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "encender verde":
		encenderVerde()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "encender azul":
		encenderAzul()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	if orden == "apagar rojo":
		apagarRojo()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar verde":
		apagarVerde()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar azul":
		apagarAzul()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar todo":
		apagarAzul()
		apagarRojo()
		apagarVerde()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
		
	elif orden == "ordenes":
		print("Las ordenes que puede reproducir este led son:\n encenedr rojo\n encender verde\n encender azul\n apagar rojo\n apagar verde\n apagar azul\n apagar todo\n salir\n")
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
		
	elif orden == "salir":
		true = False
		
	else:

		print("La orden escrita no es valida, escribe ordenes como argumento para saber las posobles ordenes")
		break
	




        

    
