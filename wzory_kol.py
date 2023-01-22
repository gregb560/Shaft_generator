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
def Gear_ratio_first_pair(zk, i):
    """

    :param zk: Parametr zakres: 1.2 - 1.25
    :param i: Całkowite przełożenie przekładni
    :return: Przełozęnie pierwszej pary koł zębatych
    """
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
def Gear_ratio_next_pair(i, ixy_1):
    """

    :param i: Przełozenie całkowite przekładni
    :param ixy_1: Przełozenie poprzedniej pary kół zębatych
    :return: Przełożenie kolejnej pary kół zębatych
    """
    ixy = i/ixy_1
    return ixy

# Obliczenie liczby zebów kół zębtych:
def Gear_teeth_number(ixy, zx):
    """

    :param ixy: Przełożenie pary kół zębatch
    :param zx: Liczba zębów koła zębatego w danej parze
    :return: Liczba zębów koła zębatego
    """
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

def Transmission_ratio_check(i, zx1, zx2, zx3, zx4):
    """
    Wartość obliczonego przełozenia powinna mieścić sie w granicach +-2% względem założonego

    :param i: Całkowite założone przełożenie przekładni
    :param zx1: Liczba zębów koła zębatego piewszej pary
    :param zx2: Liczba zębów koła zębatego pierwzej pary
    :param zx3: Liczba zębów koła zębatego drugiej pary
    :param zx4: Liczba zębów koła zębatego drugiej pary
    :return: Zwraca wartość procentówą różnicy rzeczywistego przełożenia do założonego
    """
    ispr = (zx2*zx4)/(zx1*zx3)
    ispr  = abs(i-ispr)/i *100
    return ispr

# Wyznaczenie mocy obliczenieowej [KW]

def Maximum_load_power(Nx, Cp, Cd):
    """

    :param Nx: Moc silnika
    :param Cp: Współczynnik przeciążeń dynamicznych
    :param Cd: Współczynnik nadwyżek dynamicznych
    :return: Moc zastępcza/Maksymalna moc którą wytrzyma przekładnia
    """
    Nobl = Nx * Cp * Cd
    return Nobl


# Wyznaczenie modułu  # x- numer dane koła #cos(beta=0)=1 c_beta=1 dla kół prostych współcznynniki równe są jeden; dla kół skośnych zmienić parametry

def Module_gear (Nobl, psi, _lambda, zx, n, Kgo, beta, c_beta):
    """

    :param Nobl: Moc zastępcza(Maximum_load_power)
    :param psi: Współczynnik wieńca koła zębatego
    :param _lambda: Współczynnik wytrzymałości zęba i podstawy
    :param zx: Liczba zębów koła zębatego
    :param n: liczba obrotów na wale
    :param Kgo: Narpężenia dopuszczalne danej stali
    :param beta: Kąt β koła o zębach śrubowych. Dla obliczeń koła o zębach prostych β = 0
    :param c_beta: Współcznynnik koła o zębach śrubowych.Dla obliczeń koła o zębach prostych c_β = 1
    :return: Moduł koła zębatego
    """
    m = 267 * ((Nobl*mt.cos(beta*deg))/(psi * _lambda * zx * n * Kgo * c_beta))**(1/3)
    return m


# Wyznacznie zerowej odleglości od osi a0 # x,y- numery kół zębtaych #beta = 0 koła o zębach prostych,

def Zero_distance_from_gears_axis(zx, zy, m, beta):
    """

    :param zx: Liczba zębów koła 1 danej pary
    :param zy: Liczba zębów koła 2 danej pary
    :param m: Moduł danej pary kół zębatych
    :param beta:Kąt β koła o zębach śrubowych. Dla obliczeń koła o zębach prostych β = 0
    :return: Zerowa odległość od osi kół zębatych
    """
    a0 = 0.5 * 1/(mt.cos(beta*deg))*(zx + zy) * m
    return a0



#Wyznaczenie kąta tocznego #alfa_0 przyjmowany kąt zarysu 20[stopni]

def Pressure_angle(a0, ar, alfa_0):
    """

    :param a0: Zerowa odleglość od osi kół zębatych (Zero_distance_from_gears_axis)
    :param ar: Rzeczywsita odległość od osi kół zębatych przyjeta na podstawie zerowej odległości
    :param alfa_0: Przyjęty kąt zarysu (Przeważnie 20 stopni)
    :return: Obliczony kąt toczny
    """
    eq1 = sympy.Function('eq1')
    alfa_r = sympy.symbols('alfa_r')
    eq1 = Eq(a0 * sympy.cos(alfa_0 * deg) / sympy.cos(alfa_r * deg), ar)
    sol = solve(eq1)
    sol = round(sol[0],3)
    return sol

# Wyznaczenie współczeynnika przesunięcia zarysu

def Invert_pressure_angle(alfa_r):
    """

    :param alfa_r: Kąt toczny(Pressure_angle)
    :return:  Wartość odworconego kąta tocznego
    """
    in_alfa_r = sympy.tan(alfa_r*deg) - alfa_r*deg
    in_alfa_r = float(in_alfa_r)
    in_alfa_r = decimal.Decimal(in_alfa_r).quantize(Decimal('1.000'))
    return Decimal(in_alfa_r)

def Invert_incidence_angle(alfa_0):
    """

    :param alfa_0: Kąt zarysu koła zębatego (Przeażnie 20 stopni)
    :return:  Wartość odwróconego kąta zarysu
    """
    in_alfa_0 = sympy.tan(alfa_0*deg) - alfa_0*deg
    in_alfa_0 = float(in_alfa_0)
    in_alfa_0 = decimal.Decimal(in_alfa_0).quantize(Decimal('1.000'))
    return Decimal(in_alfa_0)


#Rodział sumy współczynnika przesunięcia zarysu. # Rozdział x1,x2. x12= x1 + x2

def Sum_of_the_displacement_factor(zx, zy, in_alfa_r, in_alfa_0, alfa_0):
    """

    :param zx: Liczba zębów koła 1 danej pary
    :param zy: Liczba zębów koła 2 danej pary
    :param in_alfa_r: Wartość odwróconego kąta tocznego
    :param in_alfa_0: Wartość odwórcoengo kąta zarysu
    :param alfa_0: Kąt zarysu
    :return: Suma współczynników przesuniecia zarysu/ x12- suma , x1- przesunięcie zarysu koła 1, x2 - przesunięcie zarysu koła 2
    """
    x12 = ((zx + zy)*(in_alfa_r - in_alfa_0))/(2 * sympy.tan(alfa_0*deg))
    x1 = 0.5 * x12
    x2 = x12 - x1
    list_x = [round(x12,3),round(x1,3),round(x2,3)]
    return list_x

# Wyznaczenie skorygowanej odłegości od osi

def Corrected_distance_from_gears_axis(a0, x1, x2, m):
    """

    :param a0: Zerowa odległość od osi
    :param x1: Przesunięcie zarysu koła 1 danej pary
    :param x2: Przesunięcie zarysu koła 2 danej pary
    :param m: Moduł danej pary
    :return:  Wyznaczona skorygowana odległość od osi
    """
    ap = a0 + (x1 + x2)*m
    return ap

# Wyznaczenie wspołczynnika skórcenia zęba

def Tooth_head_shortening_factor(ap, ar, m):
    """

    :param ap: Skorygowana odległość od osi
    :param ar: Rzeczywsita odległość od osi kół zębatych przyjeta na podstawie zerowej odległości
    :param m:  Moduł pary kół zębatych
    :return: Współczynnik skrócenia głowy zęba
    """
    k = (ap - ar)/m
    return k

# Wyznaczenie parametrów geometrycznych koła zębatego o zębach prostych

def Gear_wheel_parameters(m, zx, k, x):
    """

    :param m: Moduł pary kół zębatych
    :param zx: Liczba zębów kóła zębatego
    :param k: Współczynnik skrócenia głowy zęba
    :param x: Współczynnik przesuniecią zarysu koła
    :return: ha  [0] - Wysokość głowy zęba;
             d   [1] - Średnica podziałowa;
             da  [2]- Średnica wierzchołkowa;
             dax [3] - Średnica wierzchołkowa korygowana;
             hf  [4] - Wysokość stopy zęba;
             df  [5] - Średnica stóp;
             dfx [6] - Średnica stóp korygowana
    """
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
def Gear_helix_wheel_parameters(m, mt, zx):
    """

    :param m: Moduł pary kół zębatych
    :param mt: Moduł czołowy kół zębatych
    :param zx: Liczba zębów koła zębatego
    :return: ha [0] - Wysokość głowy zęba;
             d  [1] - Średnica podziałowa;
             da [2] - Średnica wierzchołkowa;
             hf [3] - Wyskość stopy zęba;
             df [4] - Średnica stóp
    """
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
def Toothed_wheel_rim(psi, m):
    b = psi * m
    return b

# ---------------------Sprawdzenie zębów na naciski---------------------

#Obliczenie wskaźnika przyporu w przekroju czołowym εα

def Edge_contact_factors(ha, dx, dy, alfa_0, ar, m):
    """

    :param ha: Wysokosć głowy zęba
    :param dx: Średnica podziałowa koła 1 danej pary
    :param dy: Średnica podziałowa koła 2 danej pary
    :param alfa_0: Kąt zarysu koła zębatego
    :param ar: Rzeczywsita odległość od osi kół zębatych przyjeta na podstawie zerowej odległości
    :param m: Moduł pary zębatej
    :return: C1 [0] - Wspólczynnik przyporu koła 1;
             C2 [1] - Współczynnik przyporu koła 2;
             C3 [2] - Współczynnik korekcji przyporu kół
    """
    C1 = (1/(2 * mt.pi)) * mt.sqrt((1+(2 * ha/dx)) ** 2 * (1 + mt.tan(alfa_0 * deg)**2 ) - 1)
    C2 = (1 / (2 * mt.pi)) * mt.sqrt((1 + (2 * ha / dy)) ** 2 * (1 + mt.tan(alfa_0 * deg) ** 2) - 1)
    C3 = (ar/(mt.pi * m)) * mt.sqrt((1/(mt.cos(alfa_0*deg))**2)-1)
    list_C =[C1,C2,C3]
    return list_C

def Edge_contact(zx, zy, C1, C2, C3):
    """

    :param zx: Liczba zębów koła 1
    :param zy: Liczba zębów koła 2
    :param C1: Wspólczynnik przyporu koła 1
    :param C2: Współczynnik przyporu koła 2
    :param C3: Współczynnik korekcji przyporu kół
    :return: Wskaźnik przyporu w przekroju czołowym
    """
    epsilon_alfa = zx * C1 + zy * C2 - C3
    return epsilon_alfa

Cm_alfa = 478.2

def Maximum_contact_stresses(Cm_alfa, Nobl, b, epsilon_alfa, dx, nx, zx, zy):
    """

    :param Cm_alfa: Współczynnik ale nie wiem skąd sie bierze, jego wartość przyjęta na "478.2"
    :param Nobl: Moc zastępcza(Maximum_load_power)
    :param b: Szerokość wieńca pary kół zębatych
    :param epsilon_alfa: Wskaźnik przyporu w przekroju czołowym
    :param dx: Średnica podziałowa koła 1
    :param nx: Liczba obrotów wału
    :param zx: Liczba obrotów koła zębatego 1
    :param zy: Liczba obrotów koła zębatego 2
    :return: Maksymalne naprężenia stykowe
    """
    sigma_Hmax = 4270 * Cm_alfa* mt.sqrt((Nobl/(b*epsilon_alfa*(dx**2)*nx)*(1+(zx/zy))))
    return sigma_Hmax


#------------------------------------Obliczenia do kół o zębach skośnych------------------------------------

#Wyznaczenie zastępczej liczby zebow

def Substitute_number_of_teeth_helix_gear(z, beta):
    """

    :param z: Liczba zębów koła o zębach skośnych
    :param beta: Kąt beta
    :return: Zastępcza liczba zębów koła o zębach skośnych (Potrzebna do wyznaczenia współczynnika wytrzymałości zęba u  podstawy)
    """
    zrx = z/(mt.cos(beta*deg)**3)
    return zrx

# Wyzanczenie obrotów na wale

def Shaft_rotation(nx, ixy):
    """

    :param nx: Liczba obrotów wału napędzającego
    :param ixy: Przełożenie danego stopnia
    :return: Liczba obrotów wału napędzanego
    """
    ny = nx/ixy
    return ny

# Obliczenie rzecyzwistego kąta β

def Beta_angel(m, a, zx, zy):
    """

    :param m: Moduł pary kół zębatych
    :param a: Rzeczywsita odległość od osi kół zębatych przyjeta na podstawie zerowej odległości
    :param zx: Liczba zębów koła 1
    :param zy: Liczba zębów koła 2
    :return: Kąt beta koła o zębach skośnych
    """
    beta = mt.acos(0.5*m/a*(zx+zy))/deg
    return beta

#Wyznaczenie poskokowego wskaźnika przekroju εβ

def Edge_contact_helix_gear(b, beta, m):
    """

    :param b: Szerokość wieńca koła zębatego
    :param beta: Kąt beta koła o zębach skośnych
    :param m: Moduł pary kół zębatych
    :return: Poskokowy wskaźnik przyporu
    """
    epsilon_beta = (b * mt.sin(beta*deg))/(mt.pi * m)
    return epsilon_beta

# wyznaczenie kąta czołowego αt

def Apparent_pressure_angle(alfa_n, beta):
    """

    :param alfa_n: Kąt zarysu koła zębatego o zębach skośnych
    :param beta: Kąt beta koła o zębach skośnych
    :return:  Kąt czołowy koła o zębach skośnych
    """
    alfa_t = mt.atan(mt.tan(alfa_n*deg)/mt.cos(beta*deg))/deg
    return alfa_t

# Wyznaczenie modułu czołowego mt

def Apparent_pressure_module(m, beta):
    """

    :param m: Moduł pary kół zębatych
    :param beta: Kąt beta koła o zębach skośnych
    :return: Moduł czołowy
    """
    m_t = m / mt.cos(beta * deg)
    return m_t




