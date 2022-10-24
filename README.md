# Practica 2 Sensores y actuadores
## Inicio de la Práctica
En primer lugar ambos nos leimos el pdf sobre las intruciones de como hacer la práctica y nos leimos la hoja de especificaciones de led y nos dimos cuenta de que la polaridad del led estaba cambiada y que el supuesto anodo del led, en realidad es el catodo. Asi que lo que en el dibujo va conectado a GND realmente va conectado a corriente (3,3V) y en el codigo:
``` python
def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
```
Como la polaridad esta invertida en la funcion encender realmente hay que poner el GPIO el LOW:
```python 
    GPIO.output(pin, GPIO.LOw)
```
Y en la función de apagar tambien hay que cambiarlo a GPIO.HIGH:
```python 
    GPIO.output(pin, GPIO.HIGH)
```
## Revisión del código 
Una vez solucionados los problemas del código, nos pusimos manos a la obra con el código que ya nos viene dado y comenzamos a añadir comentarios y solucionar lo anteriormente dicho.
```python

import time, sys
import RPi.GPIO as GPIO      #importa las librerias de GPIO

rojoPin = 11      #declaración de variables
azulPin = 13
verdePin = 15

def encender(pin):      #función que enciende el pin que entre como parametro
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def apagar(pin):      #función que enciende el pin que entre como parametro
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def encenderRojo():   #función que enciende el led en rojo 
    encender(rojoPin)
    
while True:   #bucle while para que se que encienda todo el rato
    encenderRojo()
    
return
``` 
## Elaboración de nuestro codigo 
En primer lugar nos dimos cuenta de que con el *while true* del codigo no funciona, asique lo eliminamos y decidimos elaboara mas funciones para encender nuevos colores como Magenta, Cyan, Verde, Azul, Amarillo, Blanco...
También hicimos varios *if's* para que el usuario tubiera la opciòn de escoger el color que el quiera y que también pueda apagar el led cuando quiera
### Primera versión 
```python 
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
```
### Segunda versión 

En esta segunda versión realizaremos el mismo estilo de interface para el usuario, pero esta vez en ver de que este escoja el color del que desea que se enecienda el led, escogerá el la orden concreta que quiere que el led realice. Es decir, este puede escoger esntre encender el color rojo, apagrlo, encender el color verde, apagarlo...


