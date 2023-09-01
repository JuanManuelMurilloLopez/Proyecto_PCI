# Proyecto_PCI
Proyecto en Python para "Pensamiento Computacional para la Ingeniería
# CONTEXTO 
Los números complejos tienen propiedades diferentes a los números reales y no se pueden realizar sus operaciones en una calculadora convencional. Un programa para idear una calculadora de números complejos facilitaría y aumentaría la eficiencia al momento de hacer cálculos con este tipo de números. Los números complejos son de suma importancia y uso en diferentes ramas de la ingeniería, por ejemplo para análisis de señales, teoremas de residuos, geometría compleja, etc.

# ENTRADAS
pr1 = float<br>
pi1 = float<br>
pr2 = float<br>
pi2 = float<br>
r1 = float<br>
ang1 = float<br>
r2 = float<br>
ang2 = float<br>
exp = int<br>

# ALGORITMO
1.	Pedir al usuario el primer valor<br>
2.	Pedir al usuario el segundo valor<br>
3.	Pedir al usuario el tipo de operación deseada (suma, resta, multiplicación, división, potencia o raíz)<br>
4.	Si el usuario elige suma<br>
a.	Si el usuario ingresa los datos en forma binomial<br>
i.	Sumar partes reales entre ellas y sumar las partes imaginarias<br>
ii.	Mandar el resultado<br>
b.	Si el usuario ingresa uno o dos datos en forma trigonométrica<br>
i.	Transformar los números a forma binomial<br>
ii.	Sumar partes reales entre ellas y sumar las partes imaginarias<br>
iii.	Mandar el resultado<br>
5.	Si el usuario elige resta<br>
a.	Si el usuario ingresa los datos en forma binomial<br>
i.	Restar partes reales entre ellas y restar las partes imaginarias<br>
ii.	Mandar el resultado<br>
b.	Si el usuario ingresa uno o dos datos en forma trigonométrica<br>
i.	Transformar los números a forma binomial<br>
ii.	Restar partes reales entre ellas y restar las partes imaginarias<br>
iii.	Mandar el resultado<br>
6.	Si el usuario elige multiplicación<br>
a.	Si el usuario ingresa los datos en forma binomial<br>
i.	Multiplicar los binomios<br>
ii.	Sumar todos los reales, sumar todos los imaginarios<br>
iii.	El valor con “i2” sumarlo con los números reales<br>
iv.	Mandar el resultado<br>
b.	Si el usuario ingresa uno o dos datos de forma trigonométrica<br>
i.	Transformar los números a forma binomial<br>
ii.	Multiplicar los binomios<br>
iii.	Sumar todos los reales, sumar todos los imaginarios<br>
iv.	El valor con “i2” sumarlo con los números reales<br>
v.	Mandar el resultado<br>
7.	Si el usuario elige división<br>
a.	Si el usuario ingresa los datos de forma binomial<br>
i.	Multiplicar ambas partes de la fracción por el conjugado del segundo término<br>
ii.	Sumar las partes reales entre ellas, sumar las partes imaginarias<br>
iii.	El valor con “i2” sumarlo con los números reales<br>
iv.	Mandar el resultado<br>
b.	Si el usuario ingresa uno o dos datos de forma trigonométrica<br>
i.	Transformar los números a forma binomial<br>
ii.	Multiplicar ambas partes de la fracción por el conjugado del segundo término<br>
iii.	Sumar las partes reales entre ellas, sumar las partes imaginarias<br>
iv.	El valor con “i2” sumarlo con los números reales<br>
v.	Mandar el resultado<br>
8.	Si el usuario elige potencia<br>
a.	Si el usuario ingresa uno o dos datos de forma binomial<br>
i.	Transformar los datos a forma trigonométrica<br>
ii.	Pedir la potencia a la que se va a elevar<br>
iii.	Utilizar la fórmula para obtener el resultado<br>
iv.	Mandar el resultado<br>
b.	Si el usuario ingresa los datos de forma trigonométrica<br>
i.	Pedir la potencia a la que se va a elevar<br>
ii.	Utilizar la fórmula para obtener el resultado<br>
iii.	Mandar el resultado<br>
9.	Si el usuario elige raíz<br>
a.	Si el usuario ingresa uno o dos datos de forma binomial<br>
i.	Transformar los datos a forma trigonométrica<br>
ii.	Pedir la raíz<br>
iii.	Crear las “K” utilizando el número de la raíz y restándole 1 hasta llegar a 0<br>
iv.	Utilizar la fórmula para obtener las raíces<br>
v.	Mandar los resultados dependiendo del número de la raíz<br>
b.	Si el usuario ingresa los datos de forma trigonométrica<br>
i.	Pedir la raíz<br>
ii.	Crear las “K” utilizando el número de la raíz y restándole 1 hasta llegar a 0<br>
iii.	Utilizar la fórmula para obtener las raíces<br>
iv.	Mandar los resultados dependiendo del número de la raíz<br>

# SALIDAS
sumaV = array float<br>
restaV = array float<br>
multV  = array float<br>
divV = array float<br>
potenciaV = array float<br>
raizV = array float<br>
sumaT = array float<br>
restaT = array float<br>
multT = array float<br>
divT = array float<br>
potenciaT = array float<br>
raizT = array float<br>
