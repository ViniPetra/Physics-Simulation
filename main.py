import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import PhysicsLib as pl

#Definições de angulo e velocidade inciais
ang = 20
v  = 50

vx = []
vy = []
vt = []
px = []
py = []
ag = []

for i in np.linspace(0.0, 10, dtype=float, num=100):
    vx1 = pl.Vx(ang=ang,v=v)
    vx.append(vx1)
    vy1 = pl.Vy(ang=ang,v=v,t=i)
    vy.append(vy1)
    vt1 = pl.Vt(Vx=vx1,Vy=vy1)
    vt.append(vt1)

    px1 = pl.Px(Vx=vx1,t=i)
    px.append(px1)
    py1 = pl.Py(Vy=pl.Vy(ang=ang,v=v,t=i, Var=False),t=i)
    py.append(py1)
    ag1 = pl.Ang(Vx=vx1, Vy=vy1)
    ag.append(ag1)

    if(py1<0):
        break
    
data = {"Vx" : vx, 
        "Vy" : vy, 
        "Vt" : vt, 
        "Px" : px, 
        "Py" : py, 
        "Ag" : ag
        }

df = pd.DataFrame(data)

print(df)

fig1, plot1 = plt.subplots()

plot1.plot(px, py, label = "Simulação Posições")
plot1.set_xlabel("Px")
plot1.set_ylabel("Py")
plot1.legend()

plt.show()

