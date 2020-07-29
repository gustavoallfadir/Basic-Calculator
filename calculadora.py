from tkinter import *
from math import sqrt 


root=Tk()
root.title("Calculadora de Gus")
root.geometry("+400+100")
root.resizable(0, 0)

frame=Frame(root, width=0, height=0)
frame.pack()

#---------------Imagen de fondo---------------------
import os

def find_image(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

try:

	imagen=PhotoImage(file=find_image("matrix.png","."))
	fondo=Label(frame,image=imagen).place(x=-400,y=-400)
except:
	pass

#--------------Variables---------------------------


operacion=""

resultado=0

reset_pantalla=False

#-------------------------PANTALLA------------------


numeropantalla=StringVar()

pantalla=Entry(frame,width=15, textvariable=numeropantalla, font=(18), fg="#00FF00")
pantalla.grid(row=1,column=1, padx=10, pady=30, columnspan=5)
pantalla.config(background="black",font=("Uroob, bold", 26),fg="#03e106", justify="right")

#---------------Comandos de pulsar botones-----------


def numeroPulsado(num):

    global operacion

    global reset_pantalla

    
    if reset_pantalla!=False:

        numeropantalla.set(num)

        reset_pantalla=False

   
    else:

        numeropantalla.set(numeropantalla.get() + num)

#------------funcion suma-------------


def suma(num):

    global operacion

    global resultado

    global reset_pantalla

    resultado=resultado+float(num)

    operacion="suma"

    reset_pantalla=True
    
    numeropantalla.set(resultado)

#---------------funcion resta------------------------------
num1=0

contador_resta=0

def resta(num):
    
	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if pantalla.get()==(""):

		numeroPulsado("-")

	else:

		if contador_resta==0:

			num1=float(num)

			resultado=num1

		else:

			if contador_resta==1:

				resultado=num1-float(num)

			else:

				resultado=float(resultado)-float(num)	

			numeroPantalla.set(resultado)

			resultado=numeroPantalla.get()


		contador_resta=contador_resta+1

		operacion="resta"

		reset_pantalla=True

#-------------funcion multiplicacion---------------------
contador_multi=0

def multi(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*float(num)

		else:

			resultado=float(resultado)*float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multi"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def div(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="div"

	reset_pantalla=True



def raiz_cuadrada():
	resultado=sqrt(float(numeropantalla.get()))

	numeropantalla.set((format(resultado, '.7f')))

	reset_pantalla=TRUE


contador_porcentaje=0

def porcentaje(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_porcentaje==1:

			resultado=(num1*float(num))/100

		else:

			resultado=(float(resultado)*float(num))/100	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_porcentaje=+1

	operacion="porc"

	reset_pantalla=True

#-------------funcion Igual-----------

def igual():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeropantalla.set(resultado+float(numeropantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeropantalla.set(float(resultado)-float(numeropantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multi":

		numeropantalla.set(float(resultado)*float(numeropantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="div":

		numeropantalla.set(float(resultado)/float(numeropantalla.get()))

		resultado=0

		contador_divi=0
	
	elif operacion=="porc":

		resultadopercent=((float(resultado)*float(numeropantalla.get())/100))

		numeropantalla.set((resultadopercent,"%"))

		resultado=0

		contador_porcentaje=0

#------------------------funcion Cero-------------------------------------

def cero():
    if numeropantalla!="0":
        numeropantalla.set("") 
        reset_pantalla=True

    else:
        reset_pantalla=True



#---------------------------------fila1 ----------------------------------

boton7=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black",text="7", width=2,height=1,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1,padx=5, pady=10)

boton8=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="8", width=2,height=1,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2,padx=5, pady=10)

boton9=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="9", width=2,height=1,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3,padx=5, pady=10)

botondiv=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="÷", width=2,height=1, command=lambda:div(numeropantalla.get()))
botondiv.grid(row=2,column=4,padx=5, pady=10)

#------------------Fila2--------------------

boton4=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="4", width=2,height=1,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1,padx=5, pady=10)

boton5=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="5", width=2,height=1,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2,padx=5, pady=10)

boton6=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="6", width=2,height=1,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3,padx=5, pady=10)

botonmult=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="x", width=2,height=1, command=lambda:multi(numeropantalla.get()))
botonmult.grid(row=3,column=4,padx=5, pady=10)

#------------------Fila3--------------------

boton1=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="1", width=2,height=1,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1,padx=5, pady=10)

boton2=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="2", width=2,height=1,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2,padx=5, pady=10)

boton3=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="3", width=2,height=1,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3,padx=5, pady=10)

botonrest=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="-", width=2,height=1, command=lambda:resta(numeropantalla.get()))
botonrest.grid(row=4,column=4,padx=5, pady=10)

#--------------------Fila4-----------------

botonpunto=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text=".", width=2,height=1,command=lambda:numeroPulsado("."))
botonpunto.grid(row=5,column=1,padx=5, pady=10)

boton0=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="0", width=2,height=1,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=2,padx=5, pady=10)

botonigual=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="=", width=2,height=1,command=lambda:igual())
botonigual.grid(row=5,column=3,padx=5, pady=10)

botonsuma=Button(frame,font=("Uroob, bold", 20),fg="white", bg="green", text="+", width=2,height=3,command=lambda:suma(numeropantalla.get()))
botonsuma.grid(row=5,column=4,padx=5, pady=10, rowspan=2)

#-------------extras------------------------

boton_c=Button(frame, font=("Uroob, bold", 20),fg="white", bg="black", text="C", width=2,height=1,command=lambda:cero())
boton_c.grid(row=6, column=1, padx=5, pady=10)

boton_raiz=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="√", width=2,height=1,command=lambda:raiz_cuadrada())
boton_raiz.grid(row=6, column=2, padx=5,pady=10)

botonporcentaje=Button(frame,font=("Uroob, bold", 20),fg="white", bg="black", text="%", width=2,height=1,command=lambda:porcentaje(numeropantalla.get()))
botonporcentaje.grid(row=6, column=3, padx=5,pady=10)



root.mainloop()


