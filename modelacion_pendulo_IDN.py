## Se resuelve a través de una ODE el sistema diferencial que caracteriza el péndulo
import numpy as np

L=1     #Largo de la barra
I=L/3   #Proporcional de inercia
g=9.81  #Constante de gravedad
K=g/2   #Proporcinal de elasticidad
C=0.5   #Proporcional de amortiguamiento
