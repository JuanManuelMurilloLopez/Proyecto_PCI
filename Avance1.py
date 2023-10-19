#Librería tkinter para interfaz gráfica
import tkinter as tk
#Importar ttk de tkinter para diseño de la interfaz
from tkinter import ttk
#Librería numpy para cálculos
import numpy as np
#Librería matplotlib.pyplot para graficación
from matplotlib import pyplot as plt
#Librería matplotlib.patches para crear los arcos
from matplotlib import patches as pat
#Backend de matplotlib para poder crear la gráfica dentro de una ventana de tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Configuración de la ventana principal de Tkinter
vForma = tk.Tk()
vForma.title("Calculadora de Números Complejos")
vForma.resizable(0,0)
#Configurarción del PLT
plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#Función radianes a grados
radAgrad = 180/np.pi
#Función grados a radianes
gradArad = np.pi/180
#Función para mosrar el resultado en la entrada de texto
def mostrarResultado():
    salidaResultado.config(state="normal")
    salidaResultado.delete(0, tk.END)
    salidaResultado.insert(0,[resultado[0],",",resultado[1]])
    salidaResultado.config(state="readonly")
#Función para recuperar los datos de las entradas en la ventana Vectorial
def obtenerDatosVec():
    global nr1,ni1,nr2,ni2,num1,num2
    num1 = [float(nr1.get()),float(ni1.get())]
    num2 = [float(nr2.get()),float(ni2.get())]
    return num1,num2
#Función para recuperar los datos de las entradas en la ventana Trig
def obtenerDatosTrig():
    global modulo, angulo, exponente
    r = float(modulo.get())
    ang = float(angulo.get())
    exp = int(exponente.get())
    return r, ang, exp
#Función para graficación
def graficarVec():
    global arcNum1,arcNum2
    r1,ang1 = convertirVaT(num1)
    r2,ang2 = convertirVaT(num2)
    numTrig1 = [r1,ang1]
    numTrig2 = [r2,ang2]
    #Grafica el plano cartesiano proporcional al tamaño de los vectores
    if r1 > r2:
        global i 
        i = r1
    elif r2>r1:
        i = r2
    plt.plot([0,0],[-i,i],color="grey")
    plt.plot([-i,i],[0,0],color="grey")
    ax.scatter(0,0)
    #Vector Número 1
    plt.plot([0,num1[0]],[0,num1[1]],marker=(3,0,numTrig1[1]))
    #Vector Número 2
    plt.plot([0,num2[0]],[0,num2[1]],marker=(3,0,numTrig2[1]))
    #Vector Resultado (Cambiar el ángulo de "ang1" (último valor del marker) al ángulo del resultado)
    plt.plot([0,resultado[0]],[0,resultado[1]],marker=(3,0,ang1))
    #Etiqueta Vector N1
    plt.annotate(f"Num1 ({round(num1[0])},{round(num1[1])})",[num1[0],num1[1]])
    #Etiqueta Vector N2
    plt.annotate(f"Num2 ({round(num2[0])},{round(num2[1])})",[num2[0],num2[1]])
    arcNum1 = pat.Arc([0,0],r1/2,r1/2,angle=0,theta1=0,theta2=ang1,color='green')
    arcNum2 = pat.Arc([0,0],r2/2,r2/2,angle=0,theta1=0,theta2=ang2,color='blue')
    #Genera los arcos del ángulo de los números
    ax.add_patch(arcNum1)
    ax.add_patch(arcNum2)  
#Función para mostrar la gráfica
def graficarTrig():
    #Recuperar los datos trigonométricos
    modulo,angulo, exponente = obtenerDatosTrig()
    num = [modulo*np.cos(angulo*gradArad),modulo*np.sin(angulo*gradArad)]
    resultadoVec = [resultado[0]*np.cos(resultado[1]*gradArad),resultado[0]*np.sin(resultado[1]*gradArad)]
    k=modulo*2
    #Grafica el plano cartesiano proporcional al tamaño de los vectores
    plt.plot([0,0],[-k,k,],color="grey")
    plt.plot([-k,k],[0,0],color="grey")
    ax.scatter(0,0)
    #Graficar los números y el resultado
    plt.plot([0,num[0]],[0,num[1]],marker=(3,0,angulo))
    plt.annotate(f"Num ({round(num[0])},{round(num[1])})",[num[0],num[1]])
    plt.plot([0,resultadoVec[0]],[0,resultadoVec[1]],marker=(3,0,resultado[1]))
    plt.annotate(f"Resultado ({round(resultado[0])},{round(resultado[1])})",[resultadoVec[0],resultadoVec[1]])
    #Corregir punto de inicio de inicio del arco, inicia en 180.
    arcRes = pat.Arc([0,0],resultado[0]/2,resultado[0]/2,angle=0,theta1=0,theta2=resultado[1],color='green')
    arcNum = pat.Arc([0,0],modulo/2,modulo/2,angle=0,theta1=0,theta2=angulo,color='blue')
    ax.add_patch(arcNum)
    ax.add_patch(arcRes)
    plt.annotate(f"θ = {angulo}",[num[0]/2,num[1]/5])
#Funcion que genera la ventana con la gráfica de matplotlib
def mostrarGrafica():
    ventanaCanvas = tk.Toplevel(vForma)
    canvas = FigureCanvasTkAgg(fig,master=ventanaCanvas)
    canvas.get_tk_widget().pack()
    canvas.draw()
#Función para protocolo de cerrar ventana
def cerrarVentana():
    vForma.destroy()
    vForma.quit()
vForma.protocol("WM_DELETE_WINDOW",cerrarVentana)
#Función para convertir de Vectorial a Trigonométrico
def convertirVaT(num1):
    #Ajustar el ángulo dependiendo de su cuadrante
    if num1[0]<0:
        r = -(np.sqrt((num1[0]**2)+(num1[1]**2)))
        angRad = np.arctan((num1[1]/num1[0]))
        angGrad = (angRad*radAgrad)
        if r<0:
            r = np.abs(r)
            angGrad = angGrad + 180
        else:
            if angGrad<0:
                angGrad = angGrad + 360
    else: 
        r = (np.sqrt((num1[0]**2)+(num1[1]**2)))
        angRad = np.arctan((num1[1]/num1[0]))
        angGrad = (angRad*radAgrad)
        if r<0:
            r = np.abs(r)
            angGrad = angGrad + 180
        else:
            if angGrad < 0:
                angGrad = angGrad + 360
    return r,angGrad
#Función para convertir de Trigonométrico a Vectorial
def convertirTaV(r,ang):
    angRad = (ang*gradArad)
    nr = r*np.cos(angRad)
    ni = r*np.sin(angRad)
    return nr,ni
#Función para la suma de números en forma vectorial
def sumarVec():
    global resultado
    num1, num2 = obtenerDatosVec()
    resultado = [num1[0]+num2[0],num1[1]+num2[1]]
    mostrarResultado()
    plt.annotate(f"Suma ({round(resultado[0])},{round(resultado[1])})",[resultado[0],resultado[1]])
    graficarVec()
#Función para la resta de números en forma vectorial
def restarVec():
    global resultado
    num1, num2 = obtenerDatosVec()
    resultado = [num1[0]-num2[0],num1[1]-num2[1]]
    mostrarResultado()
    plt.annotate(f"Resta ({round(resultado[0])},{round(resultado[1])})",[resultado[0],resultado[1]])
    graficarVec()
#Función para la multiplicación de números en forma vectorial
def multiplicarVec():
     global resultado
     num1, num2 = obtenerDatosVec()
     resultado = num1[0]*num2[0]+num1[1]*num2[1]*-1,num1[0]*num2[1]+num1[1]*num2[0]
     mostrarResultado()
     plt.annotate(f"Multiplicación ({round(resultado[0])},{round(resultado[1])})",[resultado[0],resultado[1]])
     graficarVec()
#Función para la división de números en forma vectorial
def dividirVec():
    global resultado
    num1, num2 = obtenerDatosVec()
    resultado = (num1[0]*num2[0]+num1[1]*num2[1])/((num2[0]**2)+(num2[1]**2)),((num2[0]*num1[1])-num1[0]*num2[1])/((num2[0]**2)+(num2[1]**2))
    mostrarResultado()
    plt.annotate(f"Division ({round(resultado[0])},{round(resultado[1])})",[resultado[0],resultado[1]])
    graficarVec()
#Función para la potencia de números en forma trigonométrica
def potenciarTrig():
    global resultado
    r,ang,exp = obtenerDatosTrig()
    resultado = (r**exp)*(np.cos(ang*exp*gradArad)),(r**exp)*(np.sin(ang*exp*gradArad))
    mostrarResultado()
    graficarTrig()
#Función para pa raíz de números en forma trigonométrica
def racionalizar():
    global resultado
    r, ang, exp = obtenerDatosTrig()
    k = int(0)
    resultado = exp
    for k in range(-1,(exp-1),1):
        raiz = (np.cos(((ang + 2*(k+1)*180)/exp)*gradArad))*r**(1/exp),(np.sin(((ang + 2*(k+1)*180)/exp)*gradArad))*r**(1/exp)
        k = k+1
        label1 = ttk.Label(vfTrig,text=["Para K =",k])
        label1.pack()
        label2 = ttk.Label(vfTrig,text=raiz)
        label2.pack()
        graficarTrig()
#Ventana de opciones para operaciones en forma vecorial
def formaVectorial():
    global salidaResultado, nr1,ni1,nr2,ni2
    vfVec = tk.Toplevel(vForma)
    vfVec.title("Calculadora de Números Complejos")
    vfVec.resizable(0, 0)
    label1 = ttk.Label(vfVec, text="Ingresa la parte real del primer número")
    label1.pack()
    nr1 = ttk.Entry(vfVec)
    nr1.pack()
    label2 = ttk.Label(vfVec, text="Ingresa la parte imaginaria del primer número")
    label2.pack()
    ni1 = ttk.Entry(vfVec)
    ni1.pack()
    label3 = ttk.Label(vfVec, text="Ingresa la parte real del segundo número")
    label3.pack()
    nr2 = ttk.Entry(vfVec)
    nr2.pack()
    label4 = ttk.Label(vfVec, text="Ingresa la parte imaginaria del segundo número")
    label4.pack()
    ni2 = ttk.Entry(vfVec)
    ni2.pack()
    botonSuma = ttk.Button(vfVec, text="Suma", command=sumarVec)
    botonSuma.pack()
    botonResta = ttk.Button(vfVec,text="Resta",command=restarVec)
    botonResta.pack()
    botonMult = ttk.Button(vfVec, text="Multiplicación", command=multiplicarVec)
    botonMult.pack()
    botonDiv = ttk.Button(vfVec,text="División",command=dividirVec)
    botonDiv.pack()
    salidaResultado = ttk.Entry(vfVec, state="readonly")
    salidaResultado.pack()
    botonPlot = ttk.Button(vfVec,text="Graficar",command=mostrarGrafica)
    botonPlot.pack()
#Ventana de opciones para las operaciones en forma trigonométrica
def formaTrigonometrica():
    global salidaResultado, modulo, angulo, exponente
    global vfTrig
    vfTrig = tk.Toplevel(vForma)
    vfTrig.title("Calculadora de Números Complejos")
    vfTrig.resizable(0,0)
    label1 = ttk.Label(vfTrig,text="Ingrese el módulo")
    label1.pack()
    modulo = ttk.Entry(vfTrig)
    modulo.pack()
    label2 = ttk.Label(vfTrig, text="Ingrese el ángulo")
    label2.pack()
    angulo = ttk.Entry(vfTrig)
    angulo.pack()
    label3 = ttk.Label(vfTrig,text="Ingrese el exponente")
    label3.pack()
    exponente = ttk.Entry(vfTrig)
    exponente.pack()
    botonPot = ttk.Button(vfTrig,text="Potencia",command=potenciarTrig)
    botonPot.pack()
    botonRaiz = ttk.Button(vfTrig,text="Raíz",command=racionalizar)
    botonRaiz.pack()
    salidaResultado = ttk.Entry(vfTrig, state="readonly")
    salidaResultado.pack()
    botonPlot = ttk.Button(vfTrig,text="Graficar",command=mostrarGrafica)
    botonPlot.pack()
#Botones de comando de la ventana de Forma
botonFVec = ttk.Button(vForma,text="Forma Vectorial",command=formaVectorial)
botonFVec.pack()
botonFTrig = ttk.Button(vForma,text="Forma Trigonométrica",command=formaTrigonometrica)
botonFTrig.pack()  
vForma.mainloop()
