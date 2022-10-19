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
'''-----------------------------------------------------------------------------
File: ledRGB.py
Author: Carlos Escarcena y Sergio Robledo
Date: 19/10/2022
Goal: Programacion de un ledRGB   
-----------------------------------------------------------------------------''' 

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

