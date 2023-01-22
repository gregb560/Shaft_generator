import dane_wej
import math as mt
from wzory_kol import deg


# Wyznaczenie momentu walu 1/silnika
def Torque_input(N, nx):
    """

    :param N: Moc silnika
    :param nx: Ilość obrotów na wale
    :return: Moment na wale napędzającym
    """
    x = 9550 * (N/nx)
    return x

# Wyznaczenie momentów na kolejnych wałach

def Torque_shaft(T, ixy):
    """

    :param T: Moment na wale napędzającym
    :param ixy: Przełożęnie na danym stopniu
    :return: Moment na wale napędzanym
    """
    x = T * ixy
    return x


# Obliczenie Siły obwodowej Ftxy

def Force_Tangential(Tx, dx):
    """

    :param Tx: Moment na danym wale
    :param dx: Średnica podziałowa koła zębatego
    :return: Siła obwodowa koła zębatego
    """
    x = 2 * Tx/dx
    return x

# Obliczenie Siły promieniowej Frxy

def Force_Radius(Ftxy, alfa_r):
    """

    :param Ftxy: Siła obwodowa koła zębatego
    :param alfa_r: Kąt toczny
    :return: Siła promieniowa
    """
    x = Ftxy * mt.tan(alfa_r * deg)
    return x

# Obliczenie siły wzdłużnej

def Force_Longitudinal(Ftxy, beta):
    """

    :param Ftxy: Siła obwodowa koła zębateg
    :param beta: Kąt β koła zębatach o zębach skośnych
    :return:  Siła wzdłużna
    """
    x = Ftxy * mt.tan(beta* deg)
    return x

# Obliczenie współczynnika α potrzebnego do wyiczenia moemntów zastępczych

def Torque_Factor(Kgo, Ksj):
    """

    :param Kgo: Parametr Kgo danej stali
    :param Ksj: Parametr Ksj danej stali
    :return: Parametr do wyznaczania momentów zastępczych
    """
    x = Kgo/(2*Ksj)
    return x

# Obliczenie momentów gnących Mg

def Torque_Bending(Mgxz, Mgyz):
    """

    :param Mgxz: Moment gnący płaszczyzna XZ
    :param Mgyz: Moment gnący płaszczyzna YZ
    :return: Zredukowany moment gnący
    """
    x = mt.sqrt(Mgxz**2 + Mgyz**2)
    return x
#Wyznaczenie momentów zastępczych zredukowanych Mz

def Torque_Reduced(Mg, alfa, T):
    """
    :param Mg: Całkowity moment gnący
    :param alfa: Parametr do wyznaczania momentów zastępczyc
    :param T: Moment skręcający wału
    :return: Zredukowany zastępczy moment
    """
    x = mt.sqrt((Mg ** 2) + (alfa*T)**2)
    return x

# Wyznaczenie rzeczywistej średnicy wałów
def Real_shaft_diameter(Mz, Kgo):
    """

    :param Mz: Zredukowany zastępczy moment
    :param Kgo: Parametr Kgo danej stali
    :return: Minimalna średnica wału
    """
    x = 1.15 * (((32*10**3*Mz)/(mt.pi * Kgo))**(1/3))
    return x

# Wyznaczenie wypadkowej siły w podporze

def Total_Force_Reaction(Rx, Ry, Rz):
    """

    :param Rx: Reakcja w podporze oś X
    :param Ry: Reakcja w podporze oś Y
    :param Rz: Reakcja w podporze oś Z
    :return: Wypadkowa reakcja w podporze
    """
    x = mt.sqrt(Rx ** 2 + Ry ** 2 + Rz ** 2)
    return x

# Wyznaczenie obciążenia zastępczego
def Real_load(V, X, Y, R, Fw, fd, ft):
    """

    :param V: Współczynnik przypadku obciążenia dla obracjącego sie wału
    :param X: Wpółczynnik obciążenia poprzecznego
    :param Y: Współczynnik obciążenia wzdłużnego
    :param R: Wartość wypadkowej siły w podporze
    :param Fw: Siła wzdłużna
    :param fd: Współczynnik uwzględniający charakter obciążenia
    :param ft: Współczynnik uwzględniający charakter temperatury
    :return: Obciążenie zastępcze promieniowe dła łożsyka obciążonego siła wzdłużną
    """
    x = (V * X * R + Y * Fw) * ft * fd
    return x
# Wyznaczenie dodatkowej siły wzdłużnej

def Supplementary_Force_Longitudinal(e, R):
    """

    :param e: parametr dobierany w zależności od łożyska
    :param R: Wypadkowa reakcja w podporze
    :return: Dodatkowa siła wzdłużna od promieniowej reakcji w podporze
    """
    x = 0.83 * e * R
    return x

# Wyznaczenie nośności teoretycznej dla łożsyk
def Bearing_load_capacity(F, lh, nx, pow):
    """

    :param F: Obciążenie zastępcze promienowe
    :param lh: Minimalna liczba godzin pracy łożyska
    :param nx: Liczba obrótów na wale
    :param pow: Parametr określający jaki stopień ma pierwiastek. Dla łozysk kulkowych pow = 3, Dła łożsyk obciążonych siła wzdłużna pow = 3/10
    :return:
    """
    x = F * (((lh * nx* 60)/10**6) )** pow
    return x