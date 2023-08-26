import tkinter as tk
import numpy as np

#Abrir ventana
screen = tk.Tk()
screen.title("Calculadora de números complejos")
screen.mainloop()

#Definir operación
"""suma = 1
resta = 2
multiplicación = 3
división = 4
potencia = 5
raíz = 6"""
operacion = float(input("¿Qué operación desea hacer?"))

#Operaciones que utilizan 2 números (suma, resta, multiplicación, división)
if operacion <=4:
    pr1 = float(input("Ingrese el valor de la parte real del primer número"))
    pi1 = float(input("Ingrese el valor de la parte imaginaria del primer número"))
    pr2 = float(input("Ingrese el valor de la parte real del segundo número"))
    pi2 = float(input("Ingrese el valor de la parte imaginaria del segundo número"))
    num1 = [pr1,pi1]
    num2 = [pr2,pi2]
#Definir la suma
    def sumar(num1,num2):
        return num1[0]+num2[0],num1[1]+num2[1]
#Definir la resta
    def restar(num1,num2):
        return num1[0]-num2[0],num1[1]-num2[1]
#Definir la multiplicación
    def multiplicar (num1,num2):
     return num1[0]*num2[0]+num1[1]*num2[1]*-1,num1[0]*num2[1]+num1[1]*num2[0]
#Definir la división
    def dividir(num1,num2):
        return (num1[0]*num2[0]+num1[1]*num2[1])/((num2[0]**2)+(num2[1]**2)),((num2[0]*num1[1])-num1[0]*num2[1])/((num2[0]**2)+(num2[1]**2))
#Mostar la operación
    if operacion == 1:
        suma = sumar(num1,num2)    
        print(suma)
    elif operacion == 2:
        rest = restar(num1,num2)    
        print(rest)   
    elif operacion == 3:
        mult = multiplicar(num1,num2)  
        print(mult) 
    elif operacion == 4:
        divs = dividir(num1,num2)    
        print(divs)

#Operaciones que utilizan 1 número (potencia, raíz)
elif operacion == 5 or 6:
        pr1 = float(input("Ingrese el valor de la parte real del número"))
        pi1 = float(input("Ingrese el valor de la parte imaginaria del número"))
        num1 = [pr1,pi1]
        r = ((num1[0]**2)+(num1[1]**2))**(1/2)
        ang = np.arctan(num1[1]/num1[0])
        if operacion == 5:
            potencia = float(input("Potencia a elevar"))
            def potenciar(num1):
                return (r**potencia)*(np.cos(ang*potencia)),(r**potencia)*(np.sin(ang*potencia))
            potencia = potenciar(num1)
            print(potencia)
        else:
            exponente = float(input("Ingrese el exponente del binomio"))
            def racionalizar(num1):
             return 
            raiz = racionalizar(num1)
            print(raiz)