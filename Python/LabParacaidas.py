import matplotlib.pyplot as plt
import numpy as np

lista1 = [0]
lista2 = [0.0]
lista3 = [0.0]
m = float(input("Su masa (en kg): ")) * 1000
g = 9.98
c = 12500
e = 2.7182
vi = 0
ti = 0

a = 0.5
b = 1
ca = 2

tiempo = np.arange(a, b, ca)

for t in tiempo:
    x = ( (m*g/c) * (1-e**(-(c/m)*t)) )
    lista1.append(t)
    lista2.append(x)

for tf in tiempo:
    vi = vi + (g-(c/m)*vi)*(tf-ti)
    ti = tf
    lista3.append(vi)

plt.plot(lista1, lista2)
plt.plot(lista1, lista3)
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Gráfico de Velocidad en Función del Tiempo')
plt.legend(['Calculo 1', 'Calculo 2'])
plt.show()