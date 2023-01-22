import decimal
import wzory_kol as wk
import dane_wej as dane
from wzory_kol import deg


print("Dane:")
print("Moc silnika N = " +str(dane.N)+ " [kW]")
print("Liczba zębów koła 1 z1 = "+str(dane.z1) + " [-]")
print("Prędkość obrotowa na wale 1/silnika n1 = "+str(dane.n1) + " [rpm]")
print("Całkowite przełożenie redukotra i = "+str(dane.i) + " [-]")
print()


print("-------------Obliczenia do kół zębatych------------- ")

print("Obliczam przełożenie pierwszej pary kół zębatych i12: ")
i12 = round(wk.Gear_ratio_first_pair(1.2, dane.i), 1)
print("i12 = "+str(i12)+" [-]")

print("Obliczam przełożenie drugiej pary kół zębatych i34: ")
i34 = round(wk.Gear_ratio_next_pair(dane.i, i12), 1)
print("i34 = "+str(i34)+" [-]")


#z3 = input("Przyjmuje liczbe zębów koła 3 z3 =  ")
z3 = 17
print("z3 = "+str(z3)+" [-]")

print("Obliczam liczbe zębów koła 2 z2: ")
#z2 = 61
z2 = wk.Gear_teeth_number(i12, dane.z1)
z2 = float(z2)
print("z2 = "+str(z2)+" [-]")

print("Obliczam liczbe zębów koła 4 z4: ")
z4 = wk.Gear_teeth_number(i34, z3)
z4 = float(z4)
print("z4 = "+str(z4)+" [-]")

print()

print("Sprawdzednie czy rzeczywiste przełożenie mieści sie w tolerancji wzgledem teoretycznego +-2%")
spr = round(wk.Transmission_ratio_check(dane.i, dane.z1, z2, z3, z4), 3)
print("Sprawdzenie :" + str(spr)+ " [%]")
print()

print("-------------Obliczenie pary 1-2------------- ")
print("Przyjmuje współczynik wieńca dla pary 1-2 Ψ: ")
psi12 = 10
print("Ψ = "+str(psi12)+" [-]")

print()

print("Przyjmuje materiał na pare 1-2: Stal 55/C55 ")

print()

print("Przyjmuje współczynik wytrzymałości zęba u podstawy dla pary 1-2 λ: ")
lambda12 = 0.3575
print("λ = "+str(lambda12)+" [-]")

print()

print("Przyjmuje współczynnik przeciążenia Cp oraz współczynnik nadwyżek dynamycznych Cd: ")
Cp12 = 1.4
Cd12 = 1.5
print("Cp = "+str(Cp12)+" [-]")
print("Cd = "+str(Cd12)+" [-]")

print()

print("Wyznaczam moc obliczeniową Nobl:")
Nobl = wk.Maximum_load_power(dane.N, Cp12, Cd12)
print("Nobl = "+str(Nobl)+" [kW]")

print()

print("Wyznaczam moduł pary 1-2:")
m = round(wk.Module_gear(Nobl, psi12, lambda12, dane.z1, dane.n1, dane.s55_Kgo, 0, 1), 2)
print("m = "+str(m)+" [mm]")

print()

print("Przyjmuje wartość modułu z normy PN par 1-2")
m_PN = 4
print("m_PN = "+str(m_PN)+" [mm]")

print()

print("Wyznaczam zerową odległość od osi a0:")
a0 = wk.Zero_distance_from_gears_axis(dane.z1, z2, m_PN, 0)
print("a0 = " +str(a0)+ " [mm]")

print()

print("Przyjmuje odległość rzeczywistą ar na podstawie zerowej odległości a0:")
ar = 160
print("ar = " +str(ar)+ " [mm]")

print()

print("Przyjmuje kąt zarysu α0:")
alfa_0 = 20
print("α0 = " +str(alfa_0)+ " [°]")

print()

print("Wyznaczanm kąt toczny αr:")
alfa_r = round(wk.Pressure_angle(a0, ar, alfa_0), 3)
print("αr = " +str(alfa_r)+ " [°]")

print()

print("Wyznaczam współczynniki przesunięcia zarysu:")
in_alfa_r = wk.Invert_pressure_angle(alfa_r)
in_alfa_r = float(in_alfa_r)
in_alfa_0 = wk.Invert_incidence_angle(alfa_0)
in_alfa_0 = float(in_alfa_0)
x12 = wk.Sum_of_the_displacement_factor(dane.z1, z2, in_alfa_r, in_alfa_0, alfa_0)
x1 = x12[1]
x2 = x12[2]
print("x1 = "+ str(x1)+ " [mm]")
print("x2 = "+ str(x2)+ " [mm]")

print()

print("Wyznaczenie skorygowanej odległości od osi")
ap = round(wk.Corrected_distance_from_gears_axis(a0, x1, x2, m_PN), 3)
print("ap = " +str(ap)+ " [mm]")

print()

print("Wyznaczenie wspólczynnika skrócenia głowy zęba")
k = round(wk.Tooth_head_shortening_factor(ap, ar, m_PN), 3)
print("k = " +str(k)+ " [mm]")

print()

print("Wyznaczenie prarametrów koła 1:")
kolo1 = wk.Gear_wheel_parameters(m_PN, dane.z1, k, x1)
ha1 = kolo1[0]
d1 = kolo1[1]
da1 = kolo1[2]
dax1 = kolo1[3]
hf1 = kolo1[4]
df1 = kolo1[5]
dfx1 = kolo1[6]

print()

print("Wyznaczenie prarametrów koła 2:")
kolo2 = wk.Gear_wheel_parameters(m_PN, z2, k, x2)
ha2 = kolo2[0]
d2 = kolo2[1]
da2 = kolo2[2]
dax2 = kolo2[3]
hf2 = kolo2[4]
df2 = kolo2[5]
dfx2 = kolo2[6]

print()

print("Wyznaczenie szerokości wieńca pary kół 1-2")
b12 = wk.Toothed_wheel_rim(psi12, m_PN)
print("b = "+str(b12)+" [mm]")

print()

print("------------Sprawdzednie pary kół 1-2 na naciski powierzhcniowe------------")
print("Wyznaczenie wskaznika przyporu czołowego εα: ")

C = wk.Edge_contact_factors(ha1, d1, d2, alfa_0, ar, m_PN)
C1 = round(C[0],3)
print("C1 = " +str(C1)+ " [-]")
C2 = round(C[1],3)
print("C2 = " +str(C2)+ " [-]")
C3 = round(C[2],3)
print("C3 = " +str(C3)+ " [-]")

print()

epsilon_alfa = round(wk.Edge_contact(dane.z1, z2, C1, C2, C3), 2)
print("εα = "+str(epsilon_alfa)+" [-]")

print()
print("Sprawdzenie zębów na naciski powierzchniowe σ.Hmax")
sigma_Hmax = round(wk.Maximum_contact_stresses(wk.Cm_alfa, Nobl, b12, epsilon_alfa, d1, dane.n1, dane.z1, z2), 3)
print("σ.Hmax = "+str(sigma_Hmax)+" [MPa]")

if sigma_Hmax <= dane.s55_kH:
    print("Warunek σ.Hmax:"+str(sigma_Hmax)+" <= "+"kH:" +str(dane.s55_kH)+" został spełniony")
else:
    print("Warunek σ.Hmax:"+str(sigma_Hmax)+" <= "+"kH:" +str(dane.s55_kH)+" nie został spełniony")

print()

print("Obliczam przełożenie drugiej pary kół zębatych i34(para o zębach skośnych): ")

print()

print("Przyjmuje kąt zarysu αn:")
alfa_n = 20
print("αn = "+str(alfa_n)+" [°]")

print("Przyjumje współczynnik wieńca pary kół 3-4 Ψ :")
psi34 = 15
print("Ψ = "+str(psi34)+" [-]")

print("Przyjmuje kąt β :")
beta = 15
print("β = "+str(beta)+" [°]")

print("Przyjmuje współczynnik przeciążeń dynamicznych Cβ :")
c_beta = 1.3
print("Cβ = "+str(c_beta)+" [-]")

print()

print("Wyznaczam zastępcza liczbę zębów zr3:")
zr3_1 = wk.Substitute_number_of_teeth_helix_gear(z3, beta)
print("zr3 = " +str(zr3_1)+" [-]")
print("Przyjmuje zaokrągloną wartość liczby zębów zr3: ")
zr3 = round(zr3_1)
print("zr3 = " +str(zr3)+" [-]")

print()

print("Na podstawie zatępczej liczby zębów zr3 dobieram wartość współczynnika wytrzymałości zęba u podstawy λzast")
lambda34 = 0.369
print("λzast = "+str(lambda34)+" [-]")

print()

print("Wyznaczam ilość obrtów wału 2")
n2 = round(wk.Shaft_rotation(dane.n1, i12), 2)
print("n2 = " +str(n2)+ " [rpm]")

print()

print("Wyznaczam moduł pary 3-4:")
m34 = round(wk.Module_gear(Nobl, psi34, lambda34, z3, n2, dane.s55_Kgo, beta, c_beta), 2)
print("m = "+str(m34)+" [mm]")

print()

print("Przyjmuje wartość modułu z normy PN par 1-2")
m_PN34 = 5
print("m_PN34 = "+str(m_PN34)+" [mm]")

print()

print("Wyznaczam zerową odległość od osi a034:")
a0_34_1 = round(wk.Zero_distance_from_gears_axis(z3, z4, m_PN34, 15), 3)
print("a034 = " +str(a0_34_1)+ " [mm]")
print("Przyjmuje zerową odległość od osi a034")
a0_34 = 160
print("a034 ="+str(a0_34)+" [mm]")
print()

print("Wyzacznam rzeczywisty kąt β:")
beta_rz = round(wk.Beta_angel(m_PN34, a0_34, z3, z4), 3)
print("β = "+str(beta_rz)+" [°]")

print()

print("Wyznaczam szerokość wieńca pary 3-4")
b34 = wk.Toothed_wheel_rim(psi34, m_PN34)
print("b = "+str(b34)+" [mm]")

print()


print("Wyznaczenie kąta czołowego αt")
alfa_t = round(wk.Apparent_pressure_angle(alfa_n, beta_rz), 3)
print("αt = "+str(alfa_t)+ " [°]")

print()

print("Wyznaczenie modułu czołowego mt")
m_t34 = round(wk.Apparent_pressure_module(m_PN34, beta_rz), 2)
print("mt34 = "+str(m_t34)+ " [mm]")

print()

print("Wyznaczenie prarametrów koła 3:")
kolo3 = wk.Gear_helix_wheel_parameters(m_PN34, m_t34, z3)
ha3 = kolo3[0]
d3 = kolo3[1]
da3 = kolo3[2]
hf3 = kolo3[3]
df3 = kolo3[4]

print()

print("Wyznaczenie prarametrów koła 4:")
kolo4 = wk.Gear_helix_wheel_parameters(m_PN34, m_t34, z4)
ha4 = kolo4[0]
d4 = kolo4[1]
da4 = kolo4[2]
hf4 = kolo4[3]
df4 = kolo4[4]

print()
print("Wyznaczenie wskaznika przyporu czołowego εα: ")
C_34 = wk.Edge_contact_factors(ha3, d3, d4, alfa_t, a0_34, m_t34)
C1_34 = round(C_34[0],3)
print("C1 = " +str(C1_34)+ " [-]")
C2_34 = round(C_34[1],3)
print("C2 = " +str(C2_34)+ " [-]")
C3_34 = round(C_34[2],3)
print("C3 = " +str(C3_34)+ " [-]")

print()

epsilon_alfa_34 = round(wk.Edge_contact(z3, z4, C1_34, C2_34, C3_34), 2)
print("εα = "+str(epsilon_alfa_34)+" [-]")

print()

print("Wyznaczenie poskokowego wskaźnika przekroju εβ")
epsilon_beta = round(wk.Edge_contact_helix_gear(b34, beta_rz, m_PN34), 3)
print("εβ = "+str(epsilon_beta)+ " [-]")

print()

print("Wyznaczam całkowity wskzaźnik przyporu εγ")
epsilon_gamma = epsilon_alfa_34 + epsilon_beta
print("εγ = "+str(epsilon_gamma)+ " [-]")

print()

print("Sprawdzenie zębów na naciski powierzchniowe σ.Hmax")
sigma_Hmax_34 = round(wk.Maximum_contact_stresses(wk.Cm_alfa, Nobl, b34, epsilon_gamma, d3, n2, z3, z4), 3)
print("σ.Hmax = "+str(sigma_Hmax_34)+" [MPa]")

if sigma_Hmax_34 <= dane.s55_kH:
    print("Warunek σ.Hmax:"+str(sigma_Hmax_34)+" <= "+"kH:" +str(dane.s55_kH)+" został spełniony")
else:
    print("Warunek σ.Hmax:"+str(sigma_Hmax_34)+" <= "+"kH:" +str(dane.s55_kH)+" nie został spełniony")