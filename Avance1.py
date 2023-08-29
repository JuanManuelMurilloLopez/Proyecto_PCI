import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

#Abrir ventana
#screen = tk.Tk()
#screen.title("Calculadora de números complejos")
#screen.mainloop()

#Configuracción plt
plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#ax.scatter(raiz[0],raiz[1])
#plt.annotate(("Raiz",raiz),[raiz[0],raiz[1]])

#Definir operación
"""suma = 1
resta = 2
multiplicación = 3
división = 4
potencia = 5
raíz = 6"""
operacion = float(input("¿Qué operación desea hacer?"))
conversion = np.pi/180

#Definir todas las funciones de operaciones
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
#Definir la potencia
def potenciar(r,ang):
    return (r**exp)*(np.cos(ang*exp*conversion)),(r**exp)*(np.sin(ang*exp*conversion))
#Definir la raíz
def racionalizar(r,ang):
    k = 0
    for k in range(-1,(exponente-1),1):
        raiz = (np.cos(((ang + 2*(k+1)*180)/exponente)*conversion))*r**(1/exponente),(np.sin(((ang + 2*(k+1)*180)/exponente)*conversion))*r**(1/exponente)
        k = k+1
        print("Para K=",k)
        print(raiz)
        ax.scatter(raiz[0],raiz[1])
        plt.annotate(("Raiz",k),[raiz[0],raiz[1]])

#Operaciones que utilizan 2 números (suma, resta, multiplicación, división)
if operacion <=4:
    pr1 = float(input("Ingrese el valor de la parte real del primer número"))
    pi1 = float(input("Ingrese el valor de la parte imaginaria del primer número"))
    pr2 = float(input("Ingrese el valor de la parte real del segundo número"))
    pi2 = float(input("Ingrese el valor de la parte imaginaria del segundo número"))
    num1 = [pr1,pi1]
    num2 = [pr2,pi2]

#Mostar la operación
    if operacion == 1:
        suma = sumar(num1,num2)    
        print(suma)
        ax.scatter(suma[0],suma[1])
        plt.annotate(("Suma"),[suma[0],suma[1]])
        ax.scatter(num1[0],num1[1])
        plt.annotate(("Num1"),[num1[0],num1[1]])
        ax.scatter(num2[0],num2[1])
        plt.annotate(("Num2"),[num2[0],num2[1]])
    elif operacion == 2:
        rest = restar(num1,num2)    
        print(rest) 
        ax.scatter(rest[0],rest[1])  
        plt.annotate(("Resta"),[rest[0],rest[1]])
        ax.scatter(num1[0],num1[1])
        plt.annotate(("Num1"),[num1[0],num1[1]])
        ax.scatter(num2[0],num2[1])
        plt.annotate(("Num2"),[num2[0],num2[1]])
    elif operacion == 3:
        mult = multiplicar(num1,num2)  
        print(mult) 
        ax.scatter(mult[0],mult[1])
        plt.annotate(("Multiplicación"),[mult[0],mult[1]])
        ax.scatter(num1[0],num1[1])
        plt.annotate(("Num1"),[num1[0],num1[1]])
        ax.scatter(num2[0],num2[1])
        plt.annotate(("Num2"),[num2[0],num2[1]])
    elif operacion == 4:
        divs = dividir(num1,num2)    
        print(divs)
        ax.scatter(divs[0],divs[1])
        plt.annotate(("División"),[divs[0],divs[1]])
        ax.scatter(num1[0],num1[1])
        plt.annotate(("Num1"),[num1[0],num1[1]])
        ax.scatter(num2[0],num2[1])
        plt.annotate(("Num2"),[num2[0],num2[1]])

#Operaciones que utilizan 1 número (potencia, raíz)
elif operacion == 5 or 6:
        forma = float(input("¿Forma Vectorial o Trigonométrica?"))
# Vectorial = 1, Trigonométrica = 2
        if forma == 1:
            pr1 = float(input("Ingrese el valor de la parte real del número"))
            pi1 = float(input("Ingrese el valor de la parte imaginaria del número"))
            num1 = [pr1,pi1]
            r = ((num1[0]**2)+(num1[1]**2))**(1/2)
            ang = np.arctan(num1[1]/num1[0])
            if operacion == 5:
                exp = float(input("Potencia a elevar"))
                potencia = potenciar(r,ang)
                print(potencia)
                ax.scatter(potencia[0],potencia[1])
                plt.annotate(("Potencia"),[potencia[0],potencia[1]])
                ax.scatter(num1[0],num1[1])
                plt.annotate(("Num1"),[num1[0],num1[1]])
            else:
                exponente = int(input("Ingrese el exponente de la raíz"))
                k = 0
                raiz = racionalizar(r,ang)
                ax.scatter(num1[0],num1[1])
                plt.annotate(("Num1"),[num1[0],num1[1]])
        elif forma == 2:
            r = float(input("Ingrese el valor de R"))
            ang = float(input("Ingrese el valor del ángulo (Grados)"))
            if operacion == 5:
                exp = float(input("Potencia a elevar"))
                potencia = potenciar(r,ang)
                print(potencia)
                ax.scatter(potencia[0],potencia[1])
            else:
                exponente = int(input("Ingrese el exponente de la raíz"))
                raiz  = racionalizar(r,ang)
plt.show()
