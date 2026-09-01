import matplotlib.pyplot as plt
import numpy as np

with open('Lab 1\g7_21.txt', 'r') as archivo:
    lineas21 = [line.rstrip() for line in archivo]
with open('Lab 1\g7_60.txt', 'r') as archivo:
    lineas60 = [line.rstrip() for line in archivo]
with open('Lab 1\g7_90.txt', 'r') as archivo:
    lineas90 = [line.rstrip() for line in archivo]


tiempo21, tiempo60, tiempo90 = [], [], []
theta21, theta60, theta90 = [], [], []

for i in lineas21[1:]:
    tiempo21.append(float(i.split(',')[0]))
    theta21.append(float(i.split(',')[1]))

for i in lineas60[1:]:
    tiempo60.append(float(i.split(',')[0]))
    theta60.append(float(i.split(',')[1]))

for i in lineas90[1:]:
    tiempo90.append(float(i.split(',')[0]))
    theta90.append(float(i.split(',')[1]))

plt.plot(tiempo90[502:], np.deg2rad(theta90[502:]))
print(theta90[502])
plt.show()

#De manera analítica se calcula el factor de amortiguamiento a través del decremento logarítmico con X_1=-90 y X_30=-30.6 al paso de 55.7 segundos.
L=(25 * 25.4 + 17.7)*10**-3
m=L/3
k=9.807/2
decremento_1= np.log(90/30.6)
chi_1=decremento_1/np.sqrt((4*np.pi**2)+(decremento_1**2))
C=2*chi_1*np.sqrt(k*m)
print("El proporcional de amortiguamiento_1 debería ser al rededor de: ", C)
#pruebo con otro pq como q no me dio
decremento_2= np.log(1.445133/0.5527785)
chi_2=decremento_2/np.sqrt((4*np.pi**2)+(decremento_2**2))
C_2=2*chi_2*np.sqrt(k*m)
print('El proporcional de amortiguamiento_2 debería ser al rededor de: ', C_2)
