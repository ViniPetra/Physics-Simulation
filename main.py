import math
import numpy as np
import matplotlib.pyplot as plt

#Quebra do componente Vy do vetor velocidade
def Vx(ang=0, v=0.0):
    a = math.radians(ang)
    return v * math.cos(a)

#Quebra do componente Vx do vetor velocidade
def Vy(ang=0, v=0.0, g=9.81, t=0.0, Var=True):
    a = math.radians(ang)
    v = v * math.sin(a)
    if Var:
        return v - g*t
    else:
        return v

#Cálculo da posição X em determinado tempo
def Px(Xi=0.0, Vx=0.0, t=0.0):
    return Xi + Vx * t

#Cálculo da posição Y em determinado tempo com ação da gravidade
def Py(Yi=0.0, Vy=0.0, g=9.81, t=0.0):
    return Yi + Vy * t - 0.5 * g * t**2

#Cálculo da velocidade total
def Vt(Vx=0.0, Vy=0.0):
    s = (Vx**2) + (Vy**2)
    return math.sqrt(s)

#Cálculo do angulo instantâneo
def Ang(Vx=0.0, Vy=0.0):
    return math.atan(Vy/Vx)

#Definições de angulo e velocidade inciais
ang = 70
v  = 13

vx = []
vy = []
vt = []
px = []
py = []
ag = []

print("Tempo,    Px,    Py,     Vx,     Vy,     Vel,    Anglulo")

for i in np.linspace(0.0, 2.5, dtype=float, num=10):
    vx1 = Vx(ang=ang,v=v)
    vx.append(vx1)
    vy1 = Vy(ang=ang,v=v,t=i)
    vy.append(vy1)
    vt1 = Vt(Vx=vx1,Vy=vy1)
    vt.append(vt1)

    px1 = Px(Vx=vx1,t=i)
    px.append(px1)
    py1 = Py(Vy=Vy(ang=ang,v=v,t=i, Var=False),t=i)
    py.append(py1)
    ag1 = Ang(Vx=vx1, Vy=vy1)
    ag.append(ag1)
    
    print("{time:7.3f} {px:7.3f} {py:7.3f} {vx:7.3f} {vy:7.3f} {vt:7.3f} {angle:7.3f}".format(
            time = i,
            px = px1,
            py = py1,
            vx = vx1,
            vy = vy1,
            vt = vt1,
            angle = np.degrees(ag1)
    ))

fig1, plot1 = plt.subplots()

plot1.plot(px, py, label = "Simulação Posições")
plot1.set_xlabel("Px")
plot1.set_ylabel("Py")
plot1.legend()

plt.show()

