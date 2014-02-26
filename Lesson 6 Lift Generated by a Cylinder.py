import numpy as np
import matplotlib.pyplot as plt
from math import *

N = 100
xStart,xEnd = -2.0,2.0
yStart,yEnd = -1.0,1.0
x = np.linspace(xStart,xEnd,N)
y = np.linspace(yStart,yEnd,N)
X,Y = np.meshgrid(x,y)

kappa = input('Doublet strength: ')
xDoublet,yDoublet = input('Doublet location x,y: ')
# Developing external free stream based on user input
Uinf = input('Enter freestream velocity: ')
alpha1 = input('Enter freestream angle of attack: ')
alpha = alpha1*(pi/180)
uFreestream = Uinf*np.cos(alpha)*np.ones((N,N),dtype=float) #Creates usable array
vFreestream = Uinf*np.sin(alpha)*np.ones((N,N),dtype=float) #Creates usable array
psiFreestream = Uinf*np.cos(alpha)*Y

def getfunctionsdoublet(strength,xd,yd,X,Y):
    u = -strength/(2*pi)*((xd-X)**2-(yd-Y)**2)/(((xd-X)**2+(yd-Y)**2)**2)
    v = -strength/(2*pi)*(2*(xd-X)*(yd-Y))/(((xd-X)**2+(yd-Y)**2)**2)
    psi = -strength/(2*pi)*(yd-Y)/((xd-X)**2+(yd-Y)**2)
    return u,v,psi
    
uDoublet,vDoublet,psiDoublet = getfunctionsdoublet(kappa,xDoublet,yDoublet,X,Y)

u = uDoublet + uFreestream
v = vDoublet + vFreestream
psi = psiDoublet + psiFreestream

# Determining stagnation points for general flow
xStag1,yStag2 =-sqrt(kappa/(2*pi*Uinf))+xDoublet,sin(alpha)*sqrt(kappa/(2*pi*Uinf))+yDoublet
xStag2,yStag1 =sqrt(kappa/(2*pi*Uinf))+xDoublet,sin(alpha+pi)*sqrt(kappa/(2*pi*Uinf))+yDoublet

# Determining radius
R = sqrt(kappa/(2*pi*Uinf))

# Plotting
size = 10
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.title('Cylinder in a Freestream')
plt.ylim(yStart,yEnd)
plt.xlim(xStart,xEnd)
plt.streamplot(X,Y,u,v,density=2.0,linewidth=1,color='#4fd5d6',arrowsize=1,arrowstyle='->')
circle = plt.Circle((xDoublet,yDoublet),radius=R,color='#ff0000')
plt.gca().add_patch(circle)
plt.scatter(xDoublet,yDoublet,c='#CDFFFF')
plt.scatter([xStag1,xStag2],[yStag1,yStag2],c='#400D12',s=80,marker='o')
plt.show()