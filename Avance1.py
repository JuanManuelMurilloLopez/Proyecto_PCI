import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt
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
    num1 = [float(nr1.get()), float(ni1.get())]
    num2 = [float(nr2.get()), float(ni2.get())]
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
    ax.scatter(resultado[0],resultado[1])
    ax.scatter(num1[0],num1[1])
    plt.annotate(("Num1"),[num1[0],num1[1]])
    ax.scatter(num2[0],num2[1])
    plt.annotate(("Num2"),[num2[0],num2[1]])
#Función para mostrar la gráfica
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
#Función para convertir de Vectorial a Trig
def convertirVaT():
    num1 = obtenerDatosVec()
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
    return r,angGrad
#Función para convertir de Trig a Vectorial
def convertirTaV():
    r, ang = obtenerDatosTrig()
    angRad = (ang*gradArad)
    nr = r*np.cos(angRad)
    ni = r*np.sin(angRad)
    return nr,ni
#Suma Vectorial
def sumarVec():
    global resultado
    num1, num2 = obtenerDatosVec()
    resultado = [num1[0]+num2[0],num1[1]+num2[1]]
    mostrarResultado()
    plt.annotate(("Suma"),[resultado[0],resultado[1]])
    graficarVec()
#Suma Trig **
def sumarTrig():
    global resultado 
#Resta Vec
def restarVec():
    global resultado
    num1, num2 = obtenerDatosVec()
    resultado = [num1[0]-num2[0],num1[1]-num2[1]]
    mostrarResultado()
    plt.annotate(("Resta"),[resultado[0],resultado[1]])
    graficarVec()
#Multiplicación Vec
def multiplicarVec():
     global resultado
     num1, num2 = obtenerDatosVec()
     resultado = num1[0]*num2[0]+num1[1]*num2[1]*-1,num1[0]*num2[1]+num1[1]*num2[0]
     mostrarResultado()
     plt.annotate(("Multiplicación"),[resultado[0],resultado[1]])
     graficarVec()
#División Vec
def dividirVec():
    global resultado
    num1, num2 = obtenerDatosVec()
    resultado = (num1[0]*num2[0]+num1[1]*num2[1])/((num2[0]**2)+(num2[1]**2)),((num2[0]*num1[1])-num1[0]*num2[1])/((num2[0]**2)+(num2[1]**2))
    mostrarResultado()
    plt.annotate(("División"),[resultado[0],resultado[1]])
    graficarVec()
#Potencia Trig
def potenciarTrig():
    global resultado
    r,ang,exp = obtenerDatosTrig()
    resultado = (r**exp)*(np.cos(ang*exp*gradArad)),(r**exp)*(np.sin(ang*exp*gradArad))
    mostrarResultado()
#Raíz Trig
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
#Ventana de la forma Vectorial
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
#Ventana de la forma Trigonométrica
def formaTrigonometrica():
    global salidaResultado, modulo, angulo, exponente
    global vfTrig
    vfTrig = tk.Toplevel(vForma)
    vfTrig.title("Calculadora de Números Complejos")
    vfTrig.resizable(0, 0)
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
#Botones de comando de la ventana de Forma
botonFVec = ttk.Button(vForma,text="Forma Vectorial",command=formaVectorial)
botonFVec.pack()
botonFTrig = ttk.Button(vForma,text="Forma Trigonométrica",command=formaTrigonometrica)
botonFTrig.pack()  
vForma.mainloop()
