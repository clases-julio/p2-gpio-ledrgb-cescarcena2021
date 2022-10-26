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
   	
def apagarBlanco():
	apagar(rojoPin)
	apagar(verdePin)
	apagar(azulPin)
	
def apagarMagenta():
	apagar(rojoPin)
	apagar(azulPin)
	
def apagarCyan():
	apagar(azulPin)
	apagar(verdePin)
	
def apagarAmarillo():
	apagar(rojoPin)
	apagar(verdePin)

    
#-----Zona de declaracion de variables------#
    
orden = input("Escoge una orden para que se ejecute en el LED...\n")
running = True
GPIO.setwarnings(False)			# Desactivamos los warnings que puedan ser molestos 

#----------Main-----------#
while running:

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
	elif orden == "encender blanco":
		encenderBlanco()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar blanco":
		apagarBlanco()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar magenta":
		apagarMagenta()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar cyan":
		apagarCyan()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar amarillo":
		apagarAmarillo()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "encender amarillo":
		encenderAmarillo()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "encender cyan":
		encenderCyan()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "encender magenta":
		encenderMagenta()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "apagar todo":
		GPIO.cleanup ()
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	elif orden == "encender naranja":
		#rojo
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(rojoPin, GPIO.OUT)
		pwm = GPIO.PWM(rojoPin, 100)
		pwm.start(1)			## aqui se pone a 1 que realmente corresponde al 100
		#verde
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(verdePin, GPIO.OUT)
		pwm2 = GPIO.PWM(verdePin, 100)
		pwm2.start(70)			## aqui es exactamente igual que con el rojo
		
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	
	elif orden == "apagar naranja":
		pwm.start(0)
		pwm2.start(0)
		GPIO.cleanup ()
			
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	
	elif orden == "ordenes":
		print("Las ordenes que puede reproducir este led son:\n encenedr rojo\n encender verde\n encender azul\n apagar rojo\n apagar verde\n apagar azul\n apagar todo\n salir\n")
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
		
	elif orden == "salir":
		GPIO.cleanup ()
		running = False
		
	else:
		print("La orden escrita no es valida, escribe ordenes como argumento para saber las posobles ordenes")
		orden = input("Escoge una orden para que se ejecute en el LED...\n")
	




        

    
