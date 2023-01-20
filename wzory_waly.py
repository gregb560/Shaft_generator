import dane_wej
import math as mt
from wzory_kol import deg


# Wyznaczenie momentu walu 1/silnika
def T1(N,nx):
    x = 9550 * (N/nx)
    return x

# Wyznaczenie momentów na kolejnych wałach

def Tx(T,ixy):
    x = T * ixy
    return x


# Obliczenie Siły obwodowej Ftxy

def Ftxy(Tx,dx):
    x = 2 * Tx/dx
    return x

# Obliczenie Siły promieniowej Frxy

def Frxy(Ftxy,alfa_r):
    x = Ftxy * mt.tan(alfa_r * deg)
    return x

# Obliczenie siły wzdłużnej

def Fwxy(Ftxy,beta):
    x = Ftxy * mt.tan(beta* deg)
    return x

# Obliczenie współczynnika α potrzebnego do wyiczenia moemntów zastępczych

def alfa(Kgo,Ksj):
    x = Kgo/(2*Ksj)
    return x

# Obliczenie momentów gnących Mg

def Mg(Mgxz,Mgyz):
    x = mt.sqrt(Mgxz**2 + Mgyz**2)
    return x
#Wyznaczenie momentów zastępczych zredukowanych Mz

def Mz(Mg,alfa,T):
    x = mt.sqrt((Mg ** 2) + (alfa*T)**2)
    return x

# Wyznaczenie rzeczywistej średnicy wałów
def dt(Mz,Kgo):
    x = 1.15 * (((32*10**3*Mz)/(mt.pi * Kgo))**(1/3))
    return x

# Wyznaczenie wypadkowej siły w podporze

def R(Rx,Ry,Rz):
    x = mt.sqrt(Rx ** 2 + Ry ** 2 + Rz ** 2)
    return x

# Wyznaczenie obciążenia zastępczego
def F(V,X,Y,R,Fw,fd,ft):
    x = (V * X * R + Y * Fw) * ft * fd
    return x
# Wyznaczenie dodatkowej siły wzdłużnej
def S(e,R):
    x = 0.83 * e * R
    return x

# Wyznaczenie nośności teoretycznej dla łożsyk
def Cobl(F,lh,nx,pow):
    x = F * (((lh * nx* 60)/10**6) )** pow
    return x