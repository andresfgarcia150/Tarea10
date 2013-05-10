# ******************************************************************
# ******************** Universidad de los Andes ********************
# ********************   Fisica computacional   ********************
# ********************        Tarea 10          ********************
# ******************************************************************
# ***************   Andres Felipe Garcia Albarracin  ***************
# ***************         Andrea Rozo Mendez	     ***************
# ****************************************************************** 

# Librerias
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy
from scipy.fftpack import fft, fftfreq

PI = 3.141592
GM = 4.898e-12 #Kpc^3/anio^2
n1 = 12
n2 = 18
n3 = 24
n4 = 30
n5 = 36
# CONDICIONES INICIALES
# Vector de distancia al origen
R1 = [60]*n1
R2 = [70]*n2
R3 = [80]*n3
R4 = [90]*n4
R5 = [100]*n5
# Vector del angulo theta (azimutal)
T1 = [0]*n1
T2 = [0]*n2
T3 = [0]*n3
T4 = [0]*n4
T5 = [0]*n5
# Vector de velocidades (en el angulo theta)
V1 = [0]*n1
V2 = [0]*n2
V3 = [0]*n3
V4 = [0]*n4
V5 = [0]*n5

for i in range(len(R1)):
    T1[i] = 2*PI*i/n1
    V1[i] = (GM/R1[i])**0.5

for i in range(len(R2)):
    T2[i] = 2*PI*i/n2
    V2[i] = (GM/R2[i])**0.5

for i in range(len(R3)):
    T3[i] = 2*PI*i/n3
    V3[i] = (GM/R3[i])**0.5

for i in range(len(R4)):
    T4[i] = 2*PI*i/n4
    V4[i] = (GM/R4[i])**0.5

for i in range(len(R5)):
    T5[i] = 2*PI*i/n5
    V5[i] = (GM/R5[i])**0.5

# Grafica de posiciones inciales
fig1 = plt.figure()
pylab.axes(polar = True)
pylab.plot(T1,R1,'bo',T2,R2,'ro',T3,R3,'ko',T4,R4,'co',T5,R5,'yo')
pylab.xlabel('$Theta[deg]$')
pylab.ylabel('$Posicion[Kpc]$')
pylab.title('$Posicion$',fontsize = 18)
pylab.savefig('Graph1')

# Grafica de velocidades
fig2 = plt.figure()
pylab.plot(R1,V1,'bo',R2,V2,'ro',R3,V3,'ko',R4,V4,'co',R5,V5,'yo')
pylab.ylabel('$Velocidad[Kpc/a\~no]$')
pylab.xlabel('$Posicion[Kpc]$')
pylab.title('$Velocidad\ contra\ Posicion$',fontsize = 18)
pylab.savefig('Graph2')
