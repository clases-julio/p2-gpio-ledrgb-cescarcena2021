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
## Elaboración de nuestro código 
En primer lugar nos dimos cuenta de que con el *while true* del codigo no funciona, asique lo eliminamos y decidimos elaboara mas funciones para encender nuevos colores como Magenta, Cyan, Verde, Azul, Amarillo, Blanco...
También hicimos varios *if's* simulando un *switch case* para que el usuario tubiera la opción de escoger el color que él quiera y que también pueda apagar el led cuando quiera
### Primera versión ( ledRGB1.py )
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
```
El color naranja concretamente costó bastante mas que el resto de colores puesto que para este había que poner 100% rojo y 50% verde. Y conseguir este 50% en uno de los colores nos costó mucho.

### Imágenes de demostracón de algunos de los colores y de la interface de usuario:
![Imagen del led encendido de Magenta](https://github.com/clases-julio/p2-gpio-ledrgb-cescarcena2021/blob/main/src/img/Imagen1.jpeg)
Imagen del punto de vista del usuario encendiendo el color Magenta, ademas se muetra en el monitor lo que este ve.
![Imagen del led encendido de Amarillo](https://github.com/clases-julio/p2-gpio-ledrgb-cescarcena2021/blob/main/src/img/Imagen2.jpeg)
Imagen del led endendido en color Amarillo

![Link de un video de la vista del usuario](https://github.com/clases-julio/p2-gpio-ledrgb-cescarcena2021/blob/main/src/img/Video.mp4)

### Segunda versión ( ledRGB.py )

En esta segunda versión realizaremos el mismo estilo de interface para el usuario, pero esta vez en ver de que este escoja el color del que desea que se enecienda el led, escogerá el la orden concreta que quiere que el led realice. Es decir, este puede escoger esntre encender el color rojo, apagrlo, encender el color verde, apagarlo...

```python 
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
```


