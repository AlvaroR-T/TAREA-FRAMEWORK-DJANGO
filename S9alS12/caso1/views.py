from django.shortcuts import render #Libreria para reconocer el equest
from django.http import HttpResponse # Permite mostrar en pantalla un resultado

# Create your views here.

def sumaDosValores(request,*cadena,**cadenaId):
    x=5
    y=10
    z=x+y;

    return render(request,"hola.html",{'resultado':z})

def sumaDiezNumeros(request,*cadena,**cadenaId):
    #vARIABLE DE ENTRADA
    n=10
    acum=0
    #Operación
    for i in range(n+1):
        acum=acum+i
    #Mostrar resultados
    return render(request,"ejercicios.html",{'suma':acum}) 

def Lecturadelapalabra(request,*cadena,**cadenaId):
    #VARIABLE DE ENTRADA
    text=str("hola")
    a=len(text)
    for i in range(a):
        b=(text[a-i-1])
    #Mostrar resultados
    return render(request,"ejercicio1.html",{'lectura':b})   

def Lecturadelapalabra_(request,*cadena,**cadenaId):
    #VARIABLE DE ENTRADA
    text=str("hola")
    a=len(text)
    for i in range(a):
        b=(text[a-i-2])
    #Mostrar resultados
    return render(request,"ejercicio2.html",{'lectura_':b}) 

def Multiplicacióndexnúmeros(request,*cadena,**cadenaId):
    numero=5
    lista=[]
    for i in range (1,11):
        lista.append(i*numero)
    print(lista)
    return render(request,"ejercicio3.html",{'multiplicacion':lista})

def ordenamientoascendente(request,*cadena,**cadenaId):
    loteria=[10,20,40,32,12]
    for i in range(1):
        loteria.append(14)
    loteria.sort()
    print(loteria)
    return render(request,"ejercicio4.html",{'orden':loteria})

def ingresototalitario(request,*cadena,**cadenaId):
    ingresos=[20,30,40,60,80,90]
    def ingresototal(ing):
        contador=0
        for i in ing:
            contador += i
        return contador
    a=ingresototal(ingresos)
    return render(request,"ejercicio5.html",{'sumatotal':a})


#Impresión 
def actividades_ver(request, *cadena,**cadenaID):
    return render(request,"S11-S12.html",{'respuesta1':respuesta1,'lyrics':lyrics,
    'respuesta3':respuesta3,'lista':lista,'suma':suma,'les':les, 'resp7':resp7,'respuesta8':respuesta8, 'respuesta_9':respuesta_9, 'temperatura':temperatura})

#EJERCICIOS RELACIONADOS A LA SEMANA Nº11:
#PREGUNTA 1
bloques=21
total=1
altura=1
while bloques>= total + altura +1:
    altura+=1
    total +=altura
respuesta1=altura
    

#EJERCICIO NÚMERO 2
i = 0 
lyrics = []
palabra = "Mesa"
#Escribir todas las consonantes que contiene la 
while i < len(palabra):
    if palabra[i] == "e" or palabra[i] =="a":
        i += 1
        continue
    lyrics.append(palabra[i])
    print(palabra[i])
    i = i + 1
print (lyrics)

#EJERCICIO NÚMERO 3

puntaje=2100
while puntaje>1100 and puntaje<=2000:
    respuesta3="Usted Ingresó"   
else:
    respuesta3="Usted no Ingresó"

#EJERCICIO NÚMERO 4

lista = []
num = 4
while num > 3 and num < 12:
  num = num + 1
  print(f"El número se encuentra en el rango {num}")
  lista.append(f"El número se encuentra en el rango {num}")
else:
  noup="STOP"
  print(noup)
  lista.append(noup)
print(lista)

#EJERCICIO NÚMERO 5
listaglobal = [15,28,48,13,62,16,72]
n = 0 
suma = 0

while n < len(listaglobal):
    suma += listaglobal[i]
    n += 1

print(suma)

#SEMANA 12 - DO WHILE

#EJERCICIO #6
i = 1
num=6
les=[]
while i <= 10:
    resul=num*i
    generador= str(num) + "x" + str(i) + "=" + str(resul)
    les.append(generador)
    i = i + 1

print(les)

#EJERCICIO #7
numero=8
ini=1
resp7= []
while ini<=12:
    resultado = numero * ini
    ini = ini +1
    resp7.append(resultado)
print(resp7)

#EJERCICIO #8

num_ini=10
num_fin=73
cantidad=0

while num_ini <= num_fin:
    if num_ini % 2 != 1:
        cantidad += 1
    num_ini = num_ini +1
respuesta8=cantidad   
print(cantidad)  

#EJERCICIO #9
import random
numbers = []
while True:
    num = random.randint(1, 14) 
    print(num)
    numbers.append(num)
    if num == 8:
        break
print (numbers)
respuesta_9 = numbers

#EJERCICIO #10
temp = 12
temperatura=[]
while True:
  temp += 1
  temperatura.append(temp)
  print(temp)
  if temp >= 30:
    a="El agua está hirviendo"
    break
temperatura.append(a)
print(temperatura)