import decimal
import wzory_kol as wk
import dane_wej as dane
import Obliczenia_kol as Ok
import wzory_waly as ww
from sympy import *
from matplotlib import pyplot as plt
import numpy as np


# Wyznaczanie danych:
N = Ok.Nobl
n1 = dane.n1
i12 = Ok.i12
i34  = Ok.i34
i = dane.i
z1 = dane.z1
z2 = Ok.z2
z3 = Ok.z3
z4 = Ok.z4
m12 = Ok.m_PN
m34 = Ok.m_PN34
d1 = Ok.d1 * 0.001
d2 = Ok.d2 * 0.001
d3 = Ok.d3 * 0.001
d4 = Ok.d4 *0.001
alfa_r = Ok.alfa_r
deg = wk.deg

#Przyjmuje długości wałów lx- długość odcinka wału, Lx- długość całkowita wału

#Wał 1
l1 = 197 * 0.001
l2 = 59 * 0.001
L1 = l1 + l2

#Wał 2
l3 = 123 * 0.001
l4 = 74 * 0.001
l5 = 59 * 0.001
L2 = l3 + l4 + l5

#Wał 3
l6 = 123 * 0.001
l7 = 133 * 0.001
L3 = l6 + l7

#--------------------Wałek 1-----------------------
# Obliczenia Wał 1
T1 = ww.Torque_input(N, n1)
Ft12 = ww.Force_Tangential(T1, d1)
Fr12 = ww.Force_Radius(Ft12, alfa_r)


#Obliczenie reakcji w podporach A i B

#płaszczyzna XZ

Rax = symbols('Rax')
Rbx = symbols('Rbx')
Raz = symbols("Raz")
eq1xz = Eq(Raz,0)
eq2xz= Eq(Rax - Ft12 +Rbx,0)
eq3xz = Eq(Ft12 * l1 - Rbx*(l1+l2),0)
solution1 = solve((eq1xz,eq2xz,eq3xz),(Rax,Raz,Rbx))

Raz = solution1[Raz]
Rax = solution1[Rax]
Rbx = solution1[Rbx]

#płaszczyzna YZ

Ray = symbols('Ray')
Rby = symbols('Rby')
Raz = symbols("Raz")
eq1yz = Eq(Raz,0)
eq2yz = Eq(Ray + Fr12 + Rby,0)
eq3yz = Eq(-Fr12 * l1 - Rby * (l1+l2),0)
solution2 = solve((eq1yz,eq2yz,eq3yz),(Ray,Raz,Rby))
Raz = solution2[Raz]
Ray = solution2[Ray]
Rby = solution2[Rby]

# Obliczneie momentów gnących MG
# płaszczyzna XZ
Mgxz1 = 0
Mgxz2 = round(Rax * l1,2)
Mgxz3 = round(Rax *(l1+l2) -Ft12*l2,2)

value_L1 =[0,l1,l1+l2]
value_Mgxz = [Mgxz1,Mgxz2,Mgxz3]
fig, ax = plt.subplots()
plt.plot(value_L1, value_Mgxz)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany MgXZ")
plt.grid()
for i in range(len(value_L1)):
    ax.text(value_L1[i], value_Mgxz[i], value_Mgxz[i])
plt.savefig('Shaft1_MgXZ.png')

# płaszczyzna YZ

Mgyz1 = 0
Mgyz2 = round(-Ray * l1,2)
Mgyz3 = round(-Ray *(l1+l2) -Fr12*l2,2)

value_L1 =[0,l1,l1+l2]
value_Mgyz = [Mgyz1,Mgyz2,Mgyz3]
fig, ax = plt.subplots()
plt.plot(value_L1, value_Mgyz)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany MgYZ")
plt.grid()
for i in range(len(value_L1)):
    ax.text(value_L1[i], value_Mgyz[i], value_Mgyz[i])
plt.savefig('Shaft1_MgYZ.png')
#Wykres momentu moment skrecajacy

value_L1_ms =[0,l1,l1,l1+l2]
value_T1 = [T1,T1,0,0]
fig, ax = plt.subplots()
plt.plot(value_L1_ms, value_T1)
plt.xlabel("L [m]")
plt.ylabel("Moment skręcający [Nm]")
plt.title("Moment skręcający T1")
plt.grid()
for i in range(len(value_L1_ms)):
    ax.text(value_L1_ms[i], value_T1[i], value_T1[i])
plt.savefig('Shaft1_T1.png')


# Obliczenie współczynnika α potrzebnego do wyiczenia moemntów zastępczych

alfa = ww.Torque_Factor(dane.st7_Kgo, dane.st7_Ksj)

#Obliczneie momnetów gnących

Mg1 = ww.Torque_Bending(Mgxz1, Mgyz1)
Mg2 = ww.Torque_Bending(Mgxz2, Mgyz2)
Mg3 = ww.Torque_Bending(Mgxz3, Mgyz3)

value_L1 =[0,l1,l1+l2]
value_Mg = np.round([Mg1,Mg2,Mg3],2)
fig, ax = plt.subplots()
plt.plot(value_L1, value_Mg)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany Mg")
plt.grid()
for i in range(len(value_L1)):
    ax.text(value_L1[i], value_Mg[i], value_Mg[i])
plt.savefig('Shaft1_Mg.png')

# Obliczenie zastępczych momentów zredukowanych
Mz1 = ww.Torque_Reduced(Mg1, alfa, T1)
Mz2 = ww.Torque_Reduced(Mg2, alfa, T1)
Mz3 = ww.Torque_Reduced(Mg2, alfa, 0)
Mz4= ww.Torque_Reduced(Mg3, alfa, 0)

value_L1_Mz =[0,l1,l1,l1+l2]
value_Mz = [round(Mz1,2),round(Mz2,2),round(Mz3,2),round(Mz4,2)]
fig, ax = plt.subplots()
plt.plot(value_L1_Mz, value_Mz)
plt.xlabel("L [m]")
plt.ylabel("Moment zastępczy [Nm]")
plt.title("Moment zastępczy gnący zredukowany Mz")
plt.grid()
for i in range(len(value_L1_Mz)):
    ax.text(value_L1_Mz[i], value_Mz[i], value_Mz[i])
plt.savefig('Shaft1_Mz.png')

# Podzielenie moementów na równe cześci/ zastosowanie prawa Talesa

t = [0, 1/5, 2/5, 3/5, 4/5, 5/5] #Podzielenie na 5 równych odcinków z prawa Talesa

Mzt1 = np.array(Mz2-Mz1) * np.array(t) + np.array(Mz1)
Mzt2 = np.array(Mz3) * np.array(t[::-1])

#Wyznaczenie średnić rzeczywistych
dt1 = ww.Real_shaft_diameter(Mzt1, dane.st7_Kgo)
dt2 = ww.Real_shaft_diameter(Mzt2, dane.st7_Kgo)

# Podzielenie długości wałka na równe częsci / zastoswanie prawa Talesa
lt1 = np.array(l1) * np.array(t)
lt2 = np.array(l2) * np.array(t) + np.array(l1)
L1_t = np.round([*lt1,*lt2],2)
D1_t = np.round([*dt1,*dt2],2)
D1_t = np.array(D1_t)/2

fig, ax = plt.subplots()
plt.plot(L1_t*10**3, D1_t,L1_t*10**3,-D1_t)
plt.xlabel("L [mm]")
plt.ylabel("Średnica [mm]")
plt.title("Wyznaczenie zarysu rzeczywistego wałka 1")
plt.grid()
plt.savefig('Shaft1_diameter.png')

#---------------------Wałek 2------------#
T2 = ww.Torque_shaft(T1, i12)
Ft21 = -Ft12
Fr21 = -Fr12
Ft34 = ww.Force_Tangential(T2, d3)
Fr34 = ww.Force_Radius(Ft34, Ok.alfa_t)
Fw34 = ww.Force_Longitudinal(Ft34, Ok.beta_rz)

#Obliczenie reakcji w podporach C i D

#płaszczyzna XZ

Rcx = symbols('Rcx')
Rdx = symbols('Rdx')
Rcz = symbols("Rcz")
eq1xz = Eq(Rcz - Fw34,0)
eq2xz= Eq(Rcx - Fr34 + Ft21 + Rdx,0)
eq3xz = Eq(Fr34 * l3 - Fw34 * (0.5*d3) - Ft21 * (l3+l4) - Rdx * (L2) ,0)
solution3 = solve((eq1xz,eq2xz,eq3xz),(Rcx,Rcz,Rdx))
Rcz = solution3[Rcz]
Rcx = solution3[Rcx]
Rdx = solution3[Rdx]

# #płaszczyzna YZ

Rcy = symbols('Rcy')
Rdy = symbols('Rdy')
Rcz = symbols("Rcz")
eq1yz = Eq(Rcz - Fw34,0)
eq2yz = Eq(Rcy + Ft34 - Fr21 + Rdy,0)
eq3yz = Eq((-Ft34) * l3 + Fr21 * (l3+l4) - Rdy * L2,0)
solution4 = solve((eq1yz,eq2yz,eq3yz),(Rcy,Rcz,Rdy))
Rcz = solution4[Rcz]
Rcy = solution4[Rcy]
Rdy = solution4[Rdy]


# # Obliczneie momentów gnących MG
# # płaszczyzna XZ
Mgxz1_2 = 0
Mgxz2_2= round(Rcx * l3,2)
Mgxz3_2 = round(Rcx * (l3+l4) - Fr34 * l4 - Fw34 * 0.5 * d3,2)
Mgxz4_2 = round(Rcx * (L2) - Fr34 * (l4+l5) - Fw34 * 0.5 * d3 + Ft21 * (l5) ,2)

value_L2 =[0,l3,l3+l4,L2]
value_Mgxz_2 = [Mgxz1_2,Mgxz2_2,Mgxz3_2,Mgxz4_2]
fig, ax = plt.subplots()
plt.plot(value_L2, value_Mgxz_2)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany MgXZ")
plt.grid()
for i in range(len(value_L2)):
    ax.text(value_L2[i], value_Mgxz_2[i], value_Mgxz_2[i])
plt.savefig('Shaft2_MgXZ.png')

# # płaszczyzna YZ

Mgyz1_2 = 0
Mgyz2_2= round(Rcy * l3,2)
Mgyz3_2 = round(Rcy * (l3+l4) + Ft34 * l4,2)
Mgyz4_2 = round(Rcy * (L2) + Ft34 * (l4+l5) - Fr21 * l5 ,2)


value_Mgyz_2 = [Mgyz1_2,Mgyz2_2,Mgyz3_2,Mgyz4_2]
fig, ax = plt.subplots()
plt.plot(value_L2, value_Mgyz_2)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany MgYZ")
plt.grid()
for i in range(len(value_L2)):
    ax.text(value_L2[i], value_Mgyz_2[i], value_Mgyz_2[i])
plt.savefig('Shaft2_MgYZ.png')
#
# #Wykres momentu moment skrecajacy

value_L2_ms =[0,l3,l3,l3+l4,l3+l4,L2]
value_T2 = [0,0,T2,T2,0,0]
fig, ax = plt.subplots()
plt.plot(value_L2_ms, value_T2)
plt.xlabel("L [m]")
plt.ylabel("Moment skręcający [Nm]")
plt.title("Moment skręcający T2")
plt.grid()
for i in range(len(value_L2_ms)):
    ax.text(value_L2_ms[i], value_T2[i], value_T2[i])
plt.savefig('Shaft2_T2.png')
#
#
#
# # Obliczenie współczynnika α potrzebnego do wyiczenia moemntów zastępczych
#

#
# #Obliczneie momnetów gnących

Mg1_2 = ww.Torque_Bending(Mgxz1_2, Mgyz1_2)
Mg2_2 = ww.Torque_Bending(Mgxz2_2, Mgyz2_2)
Mg3_2 = ww.Torque_Bending(Mgxz3_2, Mgyz3_2)
Mg4_2 = ww.Torque_Bending(Mgxz4_2, Mgyz4_2)

value_L2 =[0,l3,l3+l4,L2]
value_Mg_2 = np.round([Mg1_2,Mg2_2,Mg3_2,Mg4_2],2)
fig, ax = plt.subplots()
plt.plot(value_L2, value_Mg_2)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany Mg")
plt.grid()
for i in range(len(value_L1)):
    ax.text(value_L2[i], value_Mg_2[i], value_Mg_2[i])
plt.savefig('Shaft2_Mg.png')
#
# # Obliczenie zastępczych momentów zredukowanych
Mz1_2 = ww.Torque_Reduced(Mg1_2, alfa, 0)
Mz2_2 = ww.Torque_Reduced(Mg2_2, alfa, 0)
Mz3_2 = ww.Torque_Reduced(Mg2_2, alfa, T2)
Mz4_2 = ww.Torque_Reduced(Mg3_2, alfa, T2)
Mz5_2 = ww.Torque_Reduced(Mg3_2, alfa, 0)
Mz6_2 = ww.Torque_Reduced(Mg4_2, alfa, 0)

value_L2_Mz =[0,l3,l3,l3+l4,l3+l4,L2]
value_Mz_2 = [round(Mz1_2,2),round(Mz2_2,2),round(Mz3_2,2),round(Mz4_2,2),round(Mz5_2,2),round(Mz6_2,2)]
fig, ax = plt.subplots()
plt.plot(value_L2_Mz, value_Mz_2)
plt.xlabel("L [m]")
plt.ylabel("Moment zastępczy [Nm]")
plt.title("Moment zastępczy gnący zredukowany Mz")
plt.grid()
for i in range(len(value_L2_Mz)):
    ax.text(value_L2_Mz[i], value_Mz_2[i], value_Mz_2[i])
plt.savefig('Shaft2_Mz.png')
#
#
# # Podzielenie moementów na równe cześci/ zastosowanie prawa Talesa
#
t = [0, 1/5, 2/5, 3/5, 4/5, 5/5] #Podzielenie na 5 równych odcinków z prawa Talesa

Mzt1_2 = np.array(Mz2_2) * np.array(t)
Mzt2_2 = np.array(Mz4_2 - Mz3_2) * np.array(t) + np.array(Mz3_2)
Mzt3_2 = np.array(Mz5_2) * np.array(t[::-1])


# #Wyznaczenie średnić rzeczywistych
dt1_2 = ww.Real_shaft_diameter(Mzt1_2, dane.st7_Kgo)
dt2_2 = ww.Real_shaft_diameter(Mzt2_2, dane.st7_Kgo)
dt3_2 = ww.Real_shaft_diameter(Mzt3_2, dane.st7_Kgo)

# # Podzielenie długości wałka na równe częsci / zastoswanie prawa Talesa
lt3 = np.array(l3) * np.array(t)
lt4 = np.array(l4) * np.array(t) + np.array(l3)
lt5 = np.array(l5) * np.array(t) + np.array(l4) + np.array(l3)
L2_t = np.round([*lt3,*lt4,*lt5],2)
D2_t = np.round([*dt1_2,*dt2_2,*dt3_2],2)
D2_t = np.array(D2_t)/2

fig, ax = plt.subplots()
plt.plot(L2_t*10**3, D2_t,L2_t*10**3,-D2_t)
plt.xlabel("L [mm]")
plt.ylabel("Średnica [mm]")
plt.title("Wyznaczenie zarysu rzeczywistego wałka 2")
plt.grid()
plt.savefig('Shaft2_diameter.png')

#--------------------Wałek 3-----------------------
# Obliczenia Wał 3
T3 = ww.Torque_shaft(T2, i34)
Ft43 = -Ft34
Fr43 = -Fr34
Fw43 = -Fw34


#Obliczenie reakcji w podporach E i F

#płaszczyzna XZ

Rex = symbols('Rex')
Rfx = symbols('Rfx')
Rez = symbols("Rez")
eq1xz_3 = Eq(Rez + Fw43,0)
eq2xz_3 = Eq(Rex + Fr43 + Rfx,0)
eq3xz_3 = Eq(-Fr43 * l6 + Fw43 * 0.5 * d4 - Rfx * L3 ,0)
solution5 = solve((eq1xz_3,eq2xz_3,eq3xz_3),(Rex,Rez,Rfx))

Rez = solution5[Rez]
Rex = solution5[Rex]
Rfx = solution5[Rfx]

#płaszczyzna YZ

Rey = symbols('Rey')
Rfy = symbols('Rfy')
Rez = symbols("Rez")
eq1yz_3 = Eq(Rez +Fw43,0)
eq2yz_3 = Eq(Rey - Ft43 + Rfy,0)
eq3yz_3 = Eq(Ft43 * l6 - Rfy * (L3),0)
solution6 = solve((eq1yz_3,eq2yz_3,eq3yz_3),(Rey,Rez,Rfy))
Rez = solution6[Rez]
Rey = solution6[Rey]
Rfy = solution6[Rfy]


# Obliczneie momentów gnących MG
# płaszczyzna XZ
Mgxz1_3 = 0
Mgxz2_3 = round(Rex *  l6,2)
Mgxz3_3 = round(Rex *(L3) + Fr43 * l7 + Fw43 * 0.5 * d4,2)

value_L3 =[0,l6,L3]
value_Mgxz_3 = [Mgxz1_3,Mgxz2_3,Mgxz3_3]
fig, ax = plt.subplots()
plt.plot(value_L3, value_Mgxz_3)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany MgXZ")
plt.grid()
for i in range(len(value_L3)):
    ax.text(value_L3[i], value_Mgxz_3[i], value_Mgxz_3[i])
plt.savefig('Shaft3_MgXZ.png')
# płaszczyzna YZ

Mgyz1_3 = 0
Mgyz2_3 = round(Rey * l6,2)
Mgyz3_3 = round(Rey *(L3) -Ft43 * l7,2)


value_Mgyz_3 = [Mgyz1_3,Mgyz2_3,Mgyz3_3]
fig, ax = plt.subplots()
plt.plot(value_L3, value_Mgyz_3)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany MgXZ")
plt.grid()
for i in range(len(value_L3)):
    ax.text(value_L3[i], value_Mgyz_3[i], value_Mgyz_3[i])
plt.savefig('Shaft3_MgYZ.png')

#Wykres momentu moment skrecajacy

value_L3_ms =[0,l6,l6,L3]
value_T3 = [T3,T3,0,0]
fig, ax = plt.subplots()
plt.plot(value_L3_ms, value_T3)
plt.xlabel("L [m]")
plt.ylabel("Moment skręcający [Nm]")
plt.title("Moment skręcający T3")
plt.grid()
for i in range(len(value_L3_ms)):
    ax.text(value_L3_ms[i], value_T3[i], value_T3[i])
plt.savefig('Shaft3_T3.png')

#Obliczneie momnetów gnących

Mg1_3 = ww.Torque_Bending(Mgxz1_3, Mgyz1_3)
Mg2_3 = ww.Torque_Bending(Mgxz2_3, Mgyz2_3)
Mg3_3 = ww.Torque_Bending(Mgxz3_3, Mgyz3_3)


value_Mg_3 = np.round([Mg1_3,Mg2_3,Mg3_3],2)
fig, ax = plt.subplots()
plt.plot(value_L3, value_Mg_3)
plt.xlabel("L [m]")
plt.ylabel("Moment gnący [Nm]")
plt.title("Moment gnący zredukowany Mg")
plt.grid()
for i in range(len(value_L3)):
    ax.text(value_L3[i], value_Mg_3[i], value_Mg_3[i])
plt.savefig('Shaft3_Mg.png')

# Obliczenie zastępczych momentów zredukowanych
Mz1_3 = ww.Torque_Reduced(Mg1_3, alfa, T3)
Mz2_3 = ww.Torque_Reduced(Mg2_3, alfa, T3)
Mz3_3 = ww.Torque_Reduced(Mg2_3, alfa, 0)
Mz4_3 = ww.Torque_Reduced(Mg3_3, alfa, 0)

value_L3_Mz =[0,l6,l6,L3]
value_Mz_3 = [round(Mz1_3,2),round(Mz2_3,2),round(Mz3_3,2),round(Mz4_3,2)]
fig, ax = plt.subplots()
plt.plot(value_L3_Mz, value_Mz_3)
plt.xlabel("L [m]")
plt.ylabel("Moment zastępczy [Nm]")
plt.title("Moment zastępczy gnący zredukowany Mz")
plt.grid()
for i in range(len(value_L3_Mz)):
    ax.text(value_L3_Mz[i], value_Mz_3[i], value_Mz_3[i])
plt.savefig('Shaft3_Mz.png')
# Podzielenie moementów na równe cześci/ zastosowanie prawa Talesa

t = [0, 1/5, 2/5, 3/5, 4/5, 5/5] #Podzielenie na 5 równych odcinków z prawa Talesa

Mzt1_3 = np.array(Mz2_3-Mz1_3) * np.array(t) + np.array(Mz1_3)
Mzt2_3 = np.array(Mz3_3) * np.array(t[::-1])

#Wyznaczenie średnić rzeczywistych
dt1_3 = ww.Real_shaft_diameter(Mzt1_3, dane.st7_Kgo)
dt2_3 = ww.Real_shaft_diameter(Mzt2_3, dane.st7_Kgo)

# Podzielenie długości wałka na równe częsci / zastoswanie prawa Talesa
lt1_3 = np.array(l6) * np.array(t)
lt2_3 = np.array(l7) * np.array(t) + np.array(l6)
L3_t = np.round([*lt1_3,*lt2_3],2)
D3_t = np.round([*dt1_3,*dt2_3],2)
D3_t = np.array(D3_t)/2

fig, ax = plt.subplots()
plt.plot(L3_t*10**3, D3_t,L3_t*10**3,-D3_t)
plt.xlabel("L [mm]")
plt.ylabel("Średnica [mm]")
plt.title("Wyznaczenie zarysu rzeczywistego wałka 3")
plt.grid()
plt.savefig('Shaft3_diameter.png')
#----------------------------Obliczenia łożysk----------------------------

# Wyznaczenie reakcji wypadkowych w podporach A i B

print()

print("Obliczenie reakcji w podporach A i B")
Ra = round(ww.Total_Force_Reaction(Rax, Ray, Raz), 2)
print("Reakcja w podpoporze Ra:")
print("Ra = " +str(Ra) + " [N]")
Rb = round(ww.Total_Force_Reaction(Rbx, Rby, 0), 2)
print("Reakcja w podpoporze Rb:")
print("Rb = " +str(Rb) + " [N]")

print()

print("Wyznaczenie obciążenia zastępczego dla łożysk w podporach A i B")

#Przyjmuje współczynniki do wyliczenia obciążęnia zastępczego

V = 1
X = 1
Y = 0
fd = 1.8
ft = 0.75

Fa = round(ww.Real_load(V, X, Y, Ra, 0, fd, ft), 2)
print("Obciążenie zastępczego dla podpory A Fa:")
print("Fa = " + str(Fa) + " [N]")
Fb = round(ww.Real_load(V, X, Y, Rb, 0, fd, ft), 2)
print("Obciążenie zastępczego dla podpory B Fb:")
print("Fb = " + str(Fb) + " [N]")


#Przyjecie liczby przepracowanych godzin
lh = 10000
print()
print("Przyjmuje że łożsyka będą pracować minimum: "+str(lh)+" [h]")

print()
print("Wyznaczam nośność obliczeniową lóżysk:")
Caobl =round(ww.Bearing_load_capacity (Fa, lh, n1, 1 / 3) * 0.001, 2)
print("Caobl = "+ str(Caobl) +" [kN]")
Cbobl = round(ww.Bearing_load_capacity (Fb, lh, n1, 1 / 3) * 0.001, 2)
print("Cbobl = "+ str(Cbobl) +" [kN]")


print()

print("Obliczenie reakcji w podporach C i D")
Rc = round(ww.Total_Force_Reaction(Rcx, Rcy, Rcz), 2)
print("Reakcja w podpoporze Rc:")
print("Rc = " +str(Rc) + " [N]")
Rd = round(ww.Total_Force_Reaction(Rdx, Rdy, 0), 2)
print("Reakcja w podpoporze Rd:")
print("Rd = " +str(Rd) + " [N]")

print()

print("Wyznaczenie obciążenia zastępczego dla łożysk w podporach C i D")

#przyjmuje z normy współczynniki obciążęnia wzdłużnego
Yc = 1.5
ec = 0.4
Yd = 1.5
ed = 0.4

Sc = round(ww.Supplementary_Force_Longitudinal(ec, Rc), 2)
Fwc = Sc + Fw34
Sd = round(ww.Supplementary_Force_Longitudinal(ed, Rd), 2)
Fwd = Sd
print(Sc)
Fc = round(ww.Real_load(V, X, Yc, Rc, Fwc, fd, ft), 2)
print("Obciążenie zastępczego dla podpory C Fa:")
print("Fc = " + str(Fc) + " [N]")
Fd = round(ww.Real_load(V, X, Yd, Rd, Fwd, fd, ft), 2)
print("Obciążenie zastępczego dla podpory D Fb:")
print("Fd = " + str(Fd) + " [N]")


print()
print("Wyznaczam nośność obliczeniową lóżysk:")
Ccobl =round(ww.Bearing_load_capacity (Fc, lh, Ok.n2, 3 / 10) * 0.001, 2)
print("Ccobl = "+ str(Ccobl) +" [kN]")
Cdobl = round(ww.Bearing_load_capacity (Fd, lh, Ok.n2, 3 / 10) * 0.001, 2)
print("Cdobl = "+ str(Cdobl) +" [kN]")

print()

# print("Wyznaczenie obciążenia zastępczego dla łożysk w podporach C i D")
#
# #przyjmuje z normy współczynniki obciążęnia wzdłużnego
# Yc = 1.5
# ec = 0.4
# Yd = 1.5
# ed = 0.4
#
# Sc = round(ww.S(ec,Rc),2)
# Fwc = Sc + Fw34
# Sd = round(ww.S(ed,Rd),2)
# Fwd = Sd
# print(Sc)
# Fc = round(ww.F(V,X,Yc,Rc,Fwc,fd,ft),2)
# print("Obciążenie zastępczego dla podpory A Fa:")
# print("Fc = " + str(Fc) + " [N]")
# Fd = round(ww.F(V,X,Yd,Rd,Fwd,fd,ft),2)
# print("Obciążenie zastępczego dla podpory B Fb:")
# print("Fd = " + str(Fd) + " [N]")
#
#
# print()
# print("Wyznaczam nośność obliczeniową lóżysk:")
# Ccobl =round(ww.Cobl (Fc,lh,Ok.n2) * 0.001,2)
# print("Ccobl = "+ str(Ccobl) +" [kN]")
# Cdobl = round(ww.Cobl (Fd,lh,Ok.n2) * 0.001,2)
# print("Cdobl = "+ str(Cdobl) +" [kN]")
#
# print()

print("Obliczenie reakcji w podporach E i F")
Re = round(ww.Total_Force_Reaction(Rex, Rey, Rez), 2)
print("Reakcja w podpoporze Re:")
print("Re = " +str(Re) + " [N]")
Rf = round(ww.Total_Force_Reaction(Rfx, Rfy, 0), 2)
print("Reakcja w podpoporze Rf:")
print("Rf = " +str(Rf) + " [N]")

print()

print("Wyznaczenie obciążenia zastępczego dla łożysk w podporach E i F")

#przyjmuje z normy współczynniki obciążęnia wzdłużnego
Ye = 1.5
ee = 0.4
Yf = 1.5
ef = 0.4

Se = round(ww.Supplementary_Force_Longitudinal(ee, Re), 2)
Fwe = Se
Sf = round(ww.Supplementary_Force_Longitudinal(ef, Rf), 2)
Fwf = Sf + Fw43

Fe = round(ww.Real_load(V, X, Ye, Re, Fwe, fd, ft), 2)
print("Obciążenie zastępczego dla podpory E Fe:")
print("Fe = " + str(Fe) + " [N]")
Ff = round(ww.Real_load(V, X, Yf, Rf, Fwf, fd, ft), 2)
print("Obciążenie zastępczego dla podpory F Ff:")
print("Ff = " + str(Ff) + " [N]")


print()
print("Wyznaczam nośność obliczeniową lóżysk:")
Ceobl =round(ww.Bearing_load_capacity (Fe, lh, wk.Shaft_rotation(Ok.n2, i34), 3 / 10) * 0.001, 2)
print("Ceobl = "+ str(Ceobl ) +" [kN]")
Cfobl = round(ww.Bearing_load_capacity (Ff, lh, wk.Shaft_rotation(Ok.n2, i34), 3 / 10) * 0.001, 2)
print("Cfobl = "+ str(Cfobl ) +" [kN]")

print()

