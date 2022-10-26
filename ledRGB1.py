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

GPIO.setwarnings(False)		# para desactivar los warnings 

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
elif color == "naranja":
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
	
	input(mensaje) 
	GPIO.cleanup ()	
	
elif color == "colores":
	print("Los colores que puede reproducir este led son: rojo\n verde\n azul\n magenta\n cyan\n amarillo\n blanco\n naranja\n")

else:
	print("El color escrito no es valido, escribe colores como argumento para saber los posobles colores")
