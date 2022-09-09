import math

#Quebra do componente Vx do vetor velocidade
def Vx(ang=0, v=0.0):
    a = math.radians(ang)
    return v * math.cos(a)

#Quebra do componente Vy do vetor velocidade
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
