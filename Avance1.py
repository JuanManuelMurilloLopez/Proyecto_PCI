import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Configuración plt
plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ventana = tk.Tk()
ventana.title("Calculadora de Números Complejos")
#Función pasar un número de forma vectorial a trigonométrica
def convertirVaT(num1):
    if num1[0]<0:
        r = -(np.sqrt((num1[0]**2)+(num1[1]**2)))
        angRad = np.arctan((num1[1]/num1[0]))
        angGrad = (angRad*radAgrad)
        if r<0:
            r = np.abs(r)
            angGrad = angGrad + 180
        else:
            if angGrad<0:
                angGrad = angGrad +  360
    else: 
        r = (np.sqrt((num1[0]**2)+(num1[1]**2)))
        angRad = np.arctan((num1[1]/num1[0]))
        angGrad = (angRad*radAgrad)
        if r<0:
            r = np.abs(r)
            angGrad = angGrad + 180
        else:
            if angGrad < 0:
                angGrad = angGrad +  360
    return [r,angGrad]
def convertirTaV(r,ang):
    angRad = (ang*gradArad)
    pr = r*np.cos(angRad)
    pi = r*np.sin(angRad)
    return [pr,pi]
#Función radianes  a grados
radAgrad = 180/np.pi
#Función grados a radianes
gradArad = np.pi/180
#Definir la suma
def sumar(num1,num2):
    return num1[0]+num2[0],num1[1]+num2[1]
def plotSumar(num1,num2,suma):
    ax.scatter(suma[0],suma[1])
    plt.annotate(("Suma"),[suma[0],suma[1]])
    ax.scatter(num1[0],num1[1])
    plt.annotate(("Num1"),[num1[0],num1[1]])
    ax.scatter(num2[0],num2[1])
    plt.annotate(("Num2"),[num2[0],num2[1]])
#Definir la resta
def restar(num1,num2):
    return num1[0]-num2[0],num1[1]-num2[1]
def plotRestar(num1,num2,rest):
    ax.scatter(rest[0],rest[1])  
    plt.annotate(("Resta"),[rest[0],rest[1]])
    ax.scatter(num1[0],num1[1])
    plt.annotate(("Num1"),[num1[0],num1[1]])
    ax.scatter(num2[0],num2[1])
    plt.annotate(("Num2"),[num2[0],num2[1]])
#Definir la multiplicación
def multiplicar (num1,num2):
     return num1[0]*num2[0]+num1[1]*num2[1]*-1,num1[0]*num2[1]+num1[1]*num2[0]
def plotMultiplicar(num1,num2,mult):
    ax.scatter(mult[0],mult[1])
    plt.annotate(("Multiplicación"),[mult[0],mult[1]])
    ax.scatter(num1[0],num1[1])
    plt.annotate(("Num1"),[num1[0],num1[1]])
    ax.scatter(num2[0],num2[1])
    plt.annotate(("Num2"),[num2[0],num2[1]])
#Definir la división
def dividir(num1,num2):
    return (num1[0]*num2[0]+num1[1]*num2[1])/((num2[0]**2)+(num2[1]**2)),((num2[0]*num1[1])-num1[0]*num2[1])/((num2[0]**2)+(num2[1]**2))
def plotDividir(num1,num2,divs):
    ax.scatter(divs[0],divs[1])
    plt.annotate(("División"),[divs[0],divs[1]])
    ax.scatter(num1[0],num1[1])
    plt.annotate(("Num1"),[num1[0],num1[1]])
    ax.scatter(num2[0],num2[1])
    plt.annotate(("Num2"),[num2[0],num2[1]])
#Definir la potencia
def potenciar(r,ang,exp):
    return (r**exp)*(np.cos(ang*exp*gradArad)),(r**exp)*(np.sin(ang*exp*gradArad))
def plotPotenciar(num1,potencia):
    ax.scatter(potencia[0],potencia[1])
    plt.annotate(("Potencia"),[potencia[0],potencia[1]])
    ax.scatter(num1[0],num1[1])
    plt.annotate(("Num1"),[num1[0],num1[1]])
#Definir la raíz
def racionalizar(r,ang,exp):
    k = 0
    for k in range(-1,(exp-1),1):
        raiz = (np.cos(((ang + 2*(k+1)*180)/exp)*gradArad))*r**(1/exp),(np.sin(((ang + 2*(k+1)*180)/exp)*gradArad))*r**(1/exp)
        k = k+1
        print("Para K=",k)
        print(raiz)
        ax.scatter(raiz[0],raiz[1])
        plt.annotate(("Raiz",k),[raiz[0],raiz[1]])
        ax.scatter(num1[0],num1[1])
        plt.annotate(("Num1"),[num1[0],num1[1]])
def racionalizarTaV(r,ang,exp):
    k = 0
    for k in range(-1,(exp-1),1):
        raiz = (np.cos(((ang + 2*(k+1)*180)/exp)*gradArad))*r**(1/exp),(np.sin(((ang + 2*(k+1)*180)/exp)*gradArad))*r**(1/exp)
        k = k+1
        raizV = convertirTaV(raiz[0],raiz[1])
        print("Para K=",k)
        print(raizV)
        ax.scatter(raizV[0],raizV[1])
        plt.annotate(("Raiz",k),[raizV[0],raizV[1]])
        ax.scatter(num1[0],num1[1])
        plt.annotate(("Num1"),[num1[0],num1[1]])
def mostrarGrafica():
    canvas = FigureCanvasTkAgg(fig,master=ventana)
    canvas.get_tk_widget().pack()
    canvas.draw()
def cerrarVentana():
    ventana.destroy()
    ventana.quit()
ventana.protocol("WM_DELETE_WINDOW",cerrarVentana)
botonPlt = tk.Button(ventana,text="Graficar",command=mostrarGrafica)
botonPlt.pack()
#Definir forma de la entrada
"""vectorial = 1
trigonométrica = 2"""
forma = float(input("¿Forma Vectorial o Trigonométrica?"))
if forma == 1:
    #Definir operación
    """suma = 1
    resta = 2
    multiplicación = 3
    división = 4
    potencia = 5
    raíz = 6"""
    operacion = float(input("¿Qué operación desea hacer?"))
    if operacion <= 4:
        pr1 = float(input("Ingrese el valor de la parte real del primer número"))
        pi1 = float(input("Ingrese el valor de la parte imaginaria del primer número"))
        pr2 = float(input("Ingrese el valor de la parte real del segundo número"))
        pi2 = float(input("Ingrese el valor de la parte imaginaria del segundo número"))
        num1 = [pr1,pi1]
        num2 = [pr2,pi2]
        if operacion == 1:
            suma = sumar(num1,num2)
            print(suma)
            plotSumar(num1,num2,suma)
        elif operacion == 2:
            rest = restar(num1,num2)
            print(rest)
            plotRestar(num1,num2,rest)
        elif operacion == 3:
            mult = multiplicar(num1,num2)
            print(mult)
            plotMultiplicar(num1,num2,mult)
        elif operacion == 4:
            div = dividir(num1,num2)
            print(div)
            plotDividir(num1,num2,div)
    elif operacion == 5 or operacion == 6:
        pr1 = float(input("Ingrese el valor de la parte real del número"))
        pi1 = float(input("Ingrese el valor de la parte imaginaria del número"))
        num1 = [pr1,pi1]
        rang = convertirVaT(num1)
        if operacion == 5:
            exp = int(input("Ingrese la potencia a elevar"))
            potenciaT = potenciar(rang[0],rang[1],exp)
            potenciaV = convertirTaV(potenciaT[0],(potenciaT[1]))
            print(potenciaV)
            plotPotenciar(num1,potenciaV)
        else:
            exp = int(input("Ingrese el exponente de la raíz"))
            raizV = racionalizarTaV(rang[0],rang[1],exp)
            #raizV = convertirTaV(raizT[0],raizT[1])
            print(raizV)
elif forma ==2:
    operacion = float(input("¿Qué operación desea hacer?"))
    if operacion <= 4:
        r1 = float(input("Ingrese el módulo del primer número"))
        ang1 = float(input("Ingrese el ángulo del primer número"))
        r2 = float(input("Ingrese el módulo del segundo número"))
        ang2 = float(input("Ingrese el ángulo del segundo número"))
        num1 = convertirTaV(r1,ang1)
        num2 = convertirTaV(r2,ang2)
        if operacion == 1:
            sumaV = sumar(num1,num2)
            sumaT = convertirVaT(sumaV)
            print(sumaT)
            plotSumar(num1,num2,sumaV)
        if operacion == 2:
            restV = restar(num1,num2)
            restT = convertirVaT(restV)
            print(restT)
            plotRestar(num1,num2,restV)
        if operacion == 3:
            multV = multiplicar(num1,num2)
            multT = convertirVaT(multV)
            print(multT)
            plotMultiplicar(num1,num2,multV)
        if operacion == 4:
            divV = dividir(num1,num2)
            divT = convertirVaT(divV)
            print(divT)
            plotDividir(num1,num2,divV)
    elif operacion == 5 or operacion == 6:
        r = float(input("Ingrese el módulo del primer número"))
        ang = float(input("Ingrese el ángulo del primer número"))
        num1 = convertirTaV(r,ang)
        if operacion == 5:
            exp = int(input("Potencia a elevar"))
            potencia = potenciar(r,ang,exp)
            print(potencia)
            plotPotenciar(num1,potencia)
        else:
            exp = int(input("Ingrese el exponente de la raíz"))
            raiz = racionalizar(r,ang,exp)
            print(raiz)
ventana.mainloop()
