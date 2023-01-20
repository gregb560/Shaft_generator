import decimal
import math
from sympy import symbols, solve, Eq
import math as mt
import dane_wej as dane
import sympy
from decimal import Decimal,getcontext
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
# Zamiana stopni na wartość liczbową deg

deg = mt.pi/180





# Współczynnik przeciążenia Cp oraz współczynnik nadwyżek dynamycznych Cd dobierane z kurmaza

Cp = 1.4
Cd = 1.5

# Obliczenie przełożenia pierwszej pary i12
def i12(zk,i):
    while True:
        if zk < 1.2:
           print("Błedny Zakres :zk 1.2 - 1.25")
           break
        elif zk >1.25:
            print("Błędny Zakres:  zk 1.2 - 1.25")
            break
        else:
            i12 = zk*mt.sqrt(i)
            return i12

# Obliczenie przelozen kolejnych par  x,y numery kol
def ixy(i,ixy_1):
    ixy = i/ixy_1
    return ixy

# Obliczenie liczby zebów kół zębtych:
def zy(ixy,zx):
    zy = ixy * zx
    if zy > decimal.Decimal(zy).quantize(Decimal('1')):
        zy = decimal.Decimal(zy).quantize(Decimal('1'))
        return decimal.Decimal(zy)
    else:
        zy = decimal.Decimal(zy).quantize(Decimal('1'))
        return decimal.Decimal(zy)
    # if zy > round(zy):
    #     zy = round(zy) + 1
    #     return zy
    # else:
    #     zy = round(zy)
    #     return zy

#Sprawdzenie przełożenia obliczeniowego  ispr <+-2%>

def ispr(i,zx1,zx2,zx3,zx4):
    ispr = (zx2*zx4)/(zx1*zx3)
    ispr  = abs(i-ispr)/i *100
    return ispr

# Wyznaczenie mocy obliczenieowej [KW]

def Nobl(Nx,Cp,Cd):
    Nobl = Nx * Cp * Cd
    return Nobl


# Wyznaczenie modułu  # x- numer dane koła #cos(beta=0)=1 c_beta=1 dla kół prostych współcznynniki równe są jeden; dla kół skośnych zmienić parametry

def m (Nobl,psi,_lambda,zx,n,Kgo,beta,c_beta):
    m = 267 * ((Nobl*mt.cos(beta*deg))/(psi * _lambda * zx * n * Kgo * c_beta))**(1/3)
    return m


# Wyznacznie zerowej odleglości od osi a0 # x,y- numery kół zębtaych #beta = 0 koła o zębach prostych,

def a0(zx,zy,m,beta):
    a0 = 0.5 * 1/(mt.cos(beta*deg))*(zx + zy) * m
    return a0



#Wyznaczenie kąta tocznego #alfa_0 przyjmowany kąt zarysu 20[stopni]

def alfa_r(a0, ar , alfa_0):
    eq1 = sympy.Function('eq1')
    alfa_r = sympy.symbols('alfa_r')
    eq1 = Eq(a0 * sympy.cos(alfa_0 * deg) / sympy.cos(alfa_r * deg), ar)
    sol = solve(eq1)
    sol = round(sol[0],3)
    return sol

# Wyznaczenie współczeynnika przesunięcia zarysu

def in_alfa_r(alfa_r):
    in_alfa_r = sympy.tan(alfa_r*deg) - alfa_r*deg
    in_alfa_r = float(in_alfa_r)
    in_alfa_r = decimal.Decimal(in_alfa_r).quantize(Decimal('1.000'))
    return Decimal(in_alfa_r)

def in_alfa_0(alfa_0):
    in_alfa_0 = sympy.tan(alfa_0*deg) - alfa_0*deg
    in_alfa_0 = float(in_alfa_0)
    in_alfa_0 = decimal.Decimal(in_alfa_0).quantize(Decimal('1.000'))
    return Decimal(in_alfa_0)


#Rodział sumy współczynnika przesunięcia zarysu. # Rozdział x1,x2. x12= x1 + x2

def x12(zx,zy,in_alfa_r,in_alfa_0,alfa_0):
    x12 = ((zx + zy)*(in_alfa_r - in_alfa_0))/(2 * sympy.tan(alfa_0*deg))
    x1 = 0.5 * x12
    x2 = x12 - x1
    list_x = [round(x12,3),round(x1,3),round(x2,3)]
    return list_x

# Wyznaczenie skorygowanej odłegości od osi

def ap(a0,x1,x2,m):
    ap = a0 + (x1 + x2)*m
    return ap

# Wyznaczenie wspołczynnika skórcenia zęba

def k(ap,ar,m):
    k = (ap - ar)/m
    return k

# Wyznaczenie parametrów geometrycznych koła zębatego o zębach prostych

def dg(m,zx,k,x):
    ha = m
    d = m * zx
    da = d + 2 * ha
    dax = da + 2 * x * m - 2 * k * m
    hf = 1.25 * m
    df = d - 2 * hf
    dfx = df + 2 * x * m
    dg_list = [ha,d,da,dax,hf,df,dfx]
    print("Wysokość głowy zęba ha = "+ str(ha) + " [mm]")
    print("Średnica podziałowa d = "+ str(d)+ " [mm]")
    print("Średnica wierzchołkowa  da = " + str(da) + " [mm]")
    print("Średnica wierzchołkowa korygowana dax = " + str(round(dax,3)) + " [mm]")
    print("Wysokość stopy zęba hf = " + str(hf) + " [mm]")
    print("Średnica stóp  df = " + str(df) + " [mm]")
    print("Średnica stóp korygowana dfx = " + str(round(dfx,3)) + " [mm]")

    return dg_list
# Wyznaczenie parametrów geometrycznych koła zębatego o zębach skośnych
def dg_s(m,mt,zx):
    ha = m
    d = mt * zx
    da = d + 2 * ha
    hf = 1.25 * m
    df = d - 2 * hf
    dg_s_list = [ha,d,da,hf,df]
    print("Wysokość głowy zęba ha = "+ str(ha) + " [mm]")
    print("Średnica podziałowa d = "+ str(d)+ " [mm]")
    print("Średnica wierzchołkowa  da = " + str(da) + " [mm]")
    print("Wysokość stopy zęba hf = " + str(hf) + " [mm]")
    print("Średnica stóp  df = " + str(df) + " [mm]")

    return dg_s_list

# Wyznaczenie szerokości wieńca pary kół zębatych
def b(psi,m):
    b = psi * m
    return b

# ---------------------Sprawdzenie zębów na naciski---------------------

#Obliczenie wskaźnika przyporu w przekroju czołowym εα

def C(ha,dx,dy,alfa_0,ar,m):
    C1 = (1/(2 * mt.pi)) * mt.sqrt((1+(2 * ha/dx)) ** 2 * (1 + mt.tan(alfa_0 * deg)**2 ) - 1)
    C2 = (1 / (2 * mt.pi)) * mt.sqrt((1 + (2 * ha / dy)) ** 2 * (1 + mt.tan(alfa_0 * deg) ** 2) - 1)
    C3 = (ar/(mt.pi * m)) * mt.sqrt((1/(mt.cos(alfa_0*deg))**2)-1)
    list_C =[C1,C2,C3]
    return list_C

def epsilon_alfa(zx,zy,C1,C2,C3):
    epsilon_alfa = zx * C1 + zy * C2 - C3
    return epsilon_alfa

Cm_alfa = 478.2

def sigma_Hmax(Cm_alfa,Nobl,b,epsilon_alfa,dx,nx,zx,zy):
    sigma_Hmax = 4270 * Cm_alfa* mt.sqrt((Nobl/(b*epsilon_alfa*(dx**2)*nx)*(1+(zx/zy))))
    return sigma_Hmax


#------------------------------------Obliczenia do kół o zębach skośnych------------------------------------

#Wyznaczenie zastępczej liczby zebow

def zrx(z,beta):
    zrx = z/(mt.cos(beta*deg)**3)
    return zrx

# Wyzanczenie obrotów na wale

def ny(nx,ixy):
    ny = nx/ixy
    return ny

# Obliczenie rzecyzwistego kąta β

def beta(m,a,zx,zy):
    beta = mt.acos(0.5*m/a*(zx+zy))/deg
    return beta

#Wyznaczenie poskokowego wskaźnika przekroju εβ

def epsilon_beta(b,beta,m):
    epsilon_beta = (b * mt.sin(beta*deg))/(mt.pi * m)
    return epsilon_beta

# wyznaczenie kąta czołowego αt

def alfa_t(alfa_n,beta):
    alfa_t = mt.atan(mt.tan(alfa_n*deg)/mt.cos(beta*deg))/deg
    return alfa_t

# Wyznaczenie modułu czołowego mt

def m_t(m,beta):
    m_t = m / mt.cos(beta * deg)
    return m_t




