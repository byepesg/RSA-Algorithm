#!/usr/bin/env python
# coding: utf-8

# # Algoritmo RSA
# -----------------------------------Características---------------------------------------------------
# Es criptografía asimétrica o de llave pública
# Posibilita el envío de mensajes de forma segura
# Utiliza números primos


# -------------------------------------Algoritmo--------------------------------------------------------
# Se necesitan dos primos p y q siendo p diferente de q
# calcular un n que es igual al producto de p por q
# Se debe calcular una función phi(n) = (p-1)(q-1)
# Se debe calcular un nuevo número e (que sea impar, primo) que cumpla la condición de ser coprimo con el resultado de la función phi, es decir 1< e < phi(n), además que el mcd(phi(n),e) = 1
# Se debe calcular un número d tal que d * e sea congruente con 1 (mod (phi(n))) es decir que d sea el multiplicador inverso de e mod phi(n)

# --------------------------------------Llaves------------------------------------------------------------
# La llave pública queda de la siguiente manera (e,n)
# La llave privada queda de la siguiente manera (d,n)

# -------------------------------------Cifrado de mensajes-------------------------------------------------
# M es el mensaje que se va encriptar (número entero)
# C = M^(e) mod n
#-------------------------------------Descifrado de mensajes-----------------------------------------------
# M = C^(d) mod n 

#### Los números primos que se utilizarán para el ejemplo.

# In[1]:


print("####################################################")
print(" \n ")
print("                Algoritmo RSA                       ")
print(" \n ")
print("####################################################")
print("Este programa esta hecho para encriptar un mensaje, usted debe ingresar un mensaje y el sistema le arrojara su correspondencia en un sistema numérico, usted puede escoger si quiere que tenga un desplazamiento. Si selecciona 0 empezara en a = 0 hasta z = 25")
texto = input("Mensaje> ").upper()
n = int(input("Desplazamiento > "))
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
convert = ""
listaABC = []
for l in texto:
    if l in abc:
        pos_letra = abc.index(l)
        nueva_pos = (pos_letra+n)%len(abc)
        convert+= abc[nueva_pos]
        listaABC.append(pos_letra)
    else:
        convert+= l
print("Mensaje Cifrado:", convert)
print("----------------------------------------------------")
print("La lista de cifrado es la siguiente:")
print(listaABC)
print("----------------------------------------------------")
p = 11                       
q = 23
##p=int(input('Ingrese p: '))
##q=int(input('Enter prime q: '))

#### Cálculo del valor como el producto de los dos números primos
n = p * q
#### Cálculo de la función de Euler para el número
phi = ( p - 1 ) * ( q - 1 ) 
#### Cálculo de un entero menor a phi y que satisface la condición de mcd(phi,e) = 1, es decir son coprimos 
e = 3                       
                            
                            
d = 1
### función de cálculo de d desde la congruencia, esto quiere decir que d*e es congruente con 1 mod (phi(n))
while ( d * e % phi  != 1):
    d = d + 1
print (d)     
    
print ("Llave pública:")
print(n,e)
print ("Llave privada:")
print(n,d)




mensaje = []
i = 1 
while i!= 0 :
  m=int(input('Ingrese uno a uno los valores de la lista de cifrado: '))
  mensaje.append(m)
  print ("Si desea ingresar mas números ingrese 'si' de lo contrario ingrese 'no' ")
  condicion = str(input())
  
  if (condicion == "si"):
      i = 1
    
  else:
      i = 0
print("El valor final de la lista es :")
print(m)
print("----------------------------------------------------")
print("La cadena del mensaje de texto inicial es: ")
print (mensaje)
print("----------------------------------------------------")
 



mensajeCifrado = []
j = 0
print ("Cifrar")
for j in range (0,len(mensaje)):
    print(mensaje[j])
    c = mensaje[j]**e%n
    mensajeCifrado.append(c)
    
print ("Cifrado")
print(mensajeCifrado)
print("----------------------------------------------------")
mensajeDescifrado = []
print ("Descifrar")
for k in range (0,len(mensajeCifrado)):
    print(mensajeCifrado[k])
    decryp =  (mensajeCifrado[k]**d) % n
    mensajeDescifrado.append(decryp)
print("Descifrado")
print(mensajeDescifrado)
    


# In[ ]:




