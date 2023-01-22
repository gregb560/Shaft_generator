from fpdf import FPDF
import dane_wej as dane
import Obliczenia_kol as Ok
import Obliczenia_waly as Ow

pdf = FPDF("P",'mm','A4')

pdf.add_page()
pdf.add_font('DejaVu', '', 'C:\Windows\Fonts\DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu','',14)

def a (x,y,z):
    pdf.cell(110, 12, x)
    pdf.cell(20, 12, y)
    pdf.cell(15, 12, z, 0, 1)
def a1 (x,y,z):
    pdf.cell(60, 12, x)
    pdf.cell(20, 12, y)
    pdf.cell(15, 12, z, 0, 1)

def a2(x, y, z):
        pdf.cell(110, 12, x)
        pdf.cell(20, 12, y)
        pdf.cell(15, 12, z, 0, 1)

def a3(x, y, z,q,w,e):
    pdf.cell(50, 12, x)
    pdf.cell(20, 12, y)
    pdf.cell(15, 12, z)
    pdf.cell(15, 12, q)
    pdf.cell(20, 12, w)
    pdf.cell(30, 12, e, 0, 1)

def b(x):
    pdf.multi_cell(0, 12,x, 0, 1, "L", False)

pdf.cell(0,16,"Schemat reduktora ",1,1,"C",False)
pdf.image('Reduktor_schemat.png', 40, 30, 200)

pdf.add_page()

pdf.cell(0,16,"Dane wejściowe ",1,1,"C",False)

a("Moc silnika N : ",str(dane.N)," [kW]")
a("Liczba zębów koła 1 z1 : ",str(dane.z1)," [-]")
a("Prędkość obrotowa na wale 1/silnika n1 : ",str(dane.n1)," [rpm]")
a("Całkowite przełożenie redukotra i : ",str(dane.i)," [-]")

pdf.cell(0,16,"Obliczenia do kół zębatych ",1,1,"C",False)
b("Obliczam przełożenie pierwszej pary kół zębatych i12:")
a1("i12 = ",str(Ok.i12)," [-]")
b("Obliczam przełożenie drugiej pary kół zębatych i34:")
a1("i34 = ",str(Ok.i34)," [-]")
b("Przyjmuje liczbe zębów koła 3 z3:")
a1("z3 = ",str(Ok.z3)," [-]")
b("Obliczam liczbe zębów koła 2 z2: ")
a1("z2 = ",str(Ok.z2)," [-]")
b("Obliczam liczbe zębów koła 4 z5: ")
a1("z4 = ",str(Ok.z4)," [-]")
b("Sprawdzednie czy rzeczywiste przełożenie mieści sie w tolerancji wzgledem teoretycznego +-2%")
a1("Sprawdzenie :" , str(Ok.spr), " [%]")
pdf.add_page()

pdf.cell(0,16,"Obliczenie pary 1-2 ",1,1,"C",False)

b("Przyjmuje współczynik wieńca dla pary 1-2 Ψ: ")
a1("Ψ = ",str(Ok.psi12)," [-]")
b("Przyjmuje materiał na pare 1-2: Stal 55/C55 ")
b("Przyjmuje współczynik wytrzymałości zęba u podstawy dla pary 1-2 λ:")
a1("λ = ",str(Ok.lambda12)," [-]")
b("Przyjmuje współczynnik przeciążenia Cp oraz współczynnik nadwyżek dynamycznych Cd: ")
a1("Cp = ",str(Ok.Cp12)," [-]")
a1("Cp = ",str(Ok.Cd12)," [-]")
b("Wyznaczam moc obliczeniową Nobl:")
a1("Nobl = ",str(Ok.Nobl)," [kW]")
b("Wyznaczam moduł pary 1-2:")
a1("m = ",str(Ok.m)," [mm]")
b("Przyjmuje wartość modułu z normy PN par 1-2")
a1("m_PN = ",str(Ok.m_PN)," [mm]")
b("Wyznaczam zerową odległość od osi a0:")
a1("a0 = " ,str(Ok.a0), " [mm]")
b("Przyjmuje odległość rzeczywistą ar na podstawie zerowej odległości a0:")
a1("a0 = " ,str(Ok.ar), " [mm]")
pdf.add_page()
b("Przyjmuje kąt zarysu α0:")
a1("α0 = " ,str(Ok.alfa_0), " [°]")
b("Wyznaczanm kąt toczny αr:")
a1("αr = " ,str(Ok.alfa_r), " [°]")
b("Wyznaczam współczynniki przesunięcia zarysu:")
a1("x1 = ", str(Ok.x1), " [mm]")
a1("x2 = ", str(Ok.x2), " [mm]")
b("Wyznaczenie skorygowanej odległości od osi ap:")
a1("ap = " ,str(Ok.ap), " [mm]")
b("Wyznaczenie wspólczynnika skrócenia głowy zęba k:")
a1("k = " ,str(Ok.k), " [mm]")

pdf.add_page()

b("Wyznaczenie parametrów koła 1:")
a2("Wysokość głowy zęba ha = " , str(Ok.ha1) , " [mm]")
a2("Średnica podziałowa d = " , str(Ok.d1) , " [mm]")
a2("Średnica wierzchołkowa  da = " , str(Ok.da1) , " [mm]")
a2("Średnica wierzchołkowa korygowana dax = " , str(round(Ok.dax1, 3)) , " [mm]")
a2("Wysokość stopy zęba hf = " , str(Ok.hf1) , " [mm]")
a2("Średnica stóp  df = " , str(Ok.df1) , " [mm]")
a2("Średnica stóp korygowana dfx = " , str(round(Ok.dfx1, 3)) , " [mm]")

a1 ( "","" ,"")

b("Wyznaczenie parametrów koła 2:")
a2("Wysokość głowy zęba ha = " , str(Ok.ha2) , " [mm]")
a2("Średnica podziałowa d = " , str(Ok.d2) , " [mm]")
a2("Średnica wierzchołkowa  da = " , str(Ok.da2) , " [mm]")
a2("Średnica wierzchołkowa korygowana dax = " , str(round(Ok.dax2, 3)) , " [mm]")
a2("Wysokość stopy zęba hf = " , str(Ok.hf2) , " [mm]")
a2("Średnica stóp  df = " , str(Ok.df2) , " [mm]")
a2("Średnica stóp korygowana dfx = " , str(round(Ok.dfx2, 3)) , " [mm]")
b("Wyznaczenie szerokości wieńca pary kół 1-2 b:")
a1("b = ",str(Ok.b12)," [mm]")

pdf.add_page()

pdf.cell(0,16,"Sprawdzednie pary kół 1-2 na naciski powierzhcniowe ",1,1,"C",False)
b("Wyznaczenie wskaznika przyporu czołowego εα:")
a1("C1 = " ,str(Ok.C1), " [-]")
a1("C2 = " ,str(Ok.C2), " [-]")
a1("C3 = " ,str(Ok.C3), " [-]")
a1("εα = ",str(Ok.epsilon_alfa)," [-]")
b("Sprawdzenie zębów na naciski powierzchniowe σ.Hmax")
a1("σ.Hmax = ",str(Ok.sigma_Hmax)," [MPa]")
if Ok.sigma_Hmax <= Ok.dane.s55_kH:
    a3("Warunek σ.Hmax:",str(Ok.sigma_Hmax)," <= ","kH:" ,str(Ok.dane.s55_kH)," został spełniony")
else:
    a3("Warunek σ.Hmax:",str(Ok.sigma_Hmax)," <= ","kH:" ,str(Ok.dane.s55_kH)," nie został spełniony")
pdf.add_page()

pdf.cell(0,16,"Obliczam przełożenie drugiej pary kół zębatych i34(para o zębach skośnych): ",1,1,"C",False)
b("Przyjmuje kąt zarysu αn:")
a1("αn = ",str(Ok.alfa_n)," [°]")
b("Przyjumje współczynnik wieńca pary kół 3-4 Ψ :")
a1("Ψ = ",str(Ok.psi34)," [-]")
b("Przyjmuje kąt β :")
a1("β = ",str(Ok.beta)," [°]")
b("Przyjmuje współczynnik przeciążeń dynamicznych Cβ :")
a1("Cβ = ",str(Ok.c_beta)," [-]")
b("Wyznaczam zastępcza liczbę zębów zr3:")
a1("zr3 = " ,str(round(Ok.zr3_1,3))," [-]")
b("Przyjmuje zaokrągloną wartość liczby zębów zr3:")
a1("zr3 = " ,str(Ok.zr3)," [-]")
b("Na podstawie zatępczej liczby zębów zr3 dobieram wartość współczynnika wytrzymałości zęba u podstawy λzast")
a1("λzast = ",str(Ok.lambda34)," [-]")
b("Wyznaczam ilość obrtów wału 2")
a1("n2 = " ,str(Ok.n2), " [rpm]")
b("Wyznaczam moduł pary 3-4:")
a1("m = ",str(Ok.m34)," [mm]")
b("Przyjmuje wartość modułu z normy PN par 1-2:")
a1("m_PN34 = ",str(Ok.m_PN34)," [mm]")
b("Wyznaczam zerową odległość od osi a034:")
a1("a034 = " ,str(Ok.a0_34_1)," [mm]")
b("Przyjmuje zerową odległość od osi a034:")
a1("a034 =",str(Ok.a0_34)," [mm]")
b("Wyznacznam rzeczywisty kąt β:")
a1("β = ",str(Ok.beta_rz)," [°]")
b("Wyznaczam szerokość wieńca pary 3-4")
a1("b = ",str(Ok.b34)," [mm]")
b("Wyznaczenie kąta czołowego αt:")
a1("αt = ",str(Ok.alfa_t), " [°]")
b("Wyznaczenie modułu czołowego mt:")
a1("mt34 = ",str(Ok.m_t34), " [mm]")

pdf.add_page()
b("Wyznaczenie parametrów koła 3:")
a2("Wysokość głowy zęba ha = " , str(Ok.ha3) , " [mm]")
a2("Średnica podziałowa d = " , str(Ok.d3) , " [mm]")
a2("Średnica wierzchołkowa  da = " , str(Ok.da3) , " [mm]")
a2("Wysokość stopy zęba hf = " , str(Ok.hf3) , " [mm]")
a2("Średnica stóp  df = " , str(Ok.df3) , " [mm]")

b("Wyznaczenie parametrów koła 4:")
a2("Wysokość głowy zęba ha = " , str(Ok.ha4) , " [mm]")
a2("Średnica podziałowa d = " , str(Ok.d4) , " [mm]")
a2("Średnica wierzchołkowa  da = " , str(Ok.da4) , " [mm]")
a2("Wysokość stopy zęba hf = " , str(Ok.hf4) , " [mm]")
a2("Średnica stóp  df = " , str(Ok.df4) , " [mm]")
pdf.add_page()
pdf.cell(0,16,"Sprawdzednie pary kół 3-4 na naciski powierzhcniowe ",1,1,"C",False)

a1("C1 = " ,str(Ok.C1_34), " [-]")
a1("C2 = " ,str(Ok.C2_34), " [-]")
a1("C3 = " ,str(Ok.C3_34), " [-]")

b("Wyznaczenie wskaznika przyporu czołowego εα:")
a1("εα = ",str(Ok.epsilon_alfa_34)," [-]")

b("Wyznaczenie poskokowego wskaźnika przekroju εβ")
a1("εβ = ",str(Ok.epsilon_beta)," [-]")

b("Wyznaczenie całkowitego wskaźnika przyporu εγ :")
a1("εγ = ",str(Ok.epsilon_gamma)," [-]")

if Ok.sigma_Hmax_34 <= Ok.dane.s55_kH:
    a3("Warunek σ.Hmax:",str(Ok.sigma_Hmax_34)," <= ","kH:" ,str(Ok.dane.s55_kH)," został spełniony")
else:
    a3("Warunek σ.Hmax:",str(Ok.sigma_Hmax_34)," <= ","kH:" ,str(Ok.dane.s55_kH)," nie został spełniony")

pdf.add_page()

pdf.cell(0,16,"Wałek 1 ",1,1,"C",False)

b("Wyznaczenie momentu obrotowego na wale 1:")
a1("T1= ",str(Ow.T1)," [Nm]")
b("Wyznaczenie siły obwodowej Ft12:")
a1("Ft12= ",str(round(Ow.Ft12,2))," [N]")
b("Wyznaczenie siły promieniowej Fr12:")
a1("Fr12= ",str(round((Ow.Fr12),2))," [N]")

b("Obliczenie reakcji w podporach A i B")
b("Płaszczyzna XZ")
a1("Rax= ",str(round((Ow.Rax),2))," [N]")
a1("Rbx= ",str(round((Ow.Rbx),2))," [N]")
a1("Raz= ",str(round((Ow.Raz),2))," [N]")
b("Płaszczyzna YZ")
a1("Ray= ",str(round((Ow.Ray),2))," [N]")
a1("Rby= ",str(round((Ow.Rby),2))," [N]")
a1("Raz= ",str(round((Ow.Raz),2))," [N]")

pdf.add_page()
pdf.cell(0,16,"Wykresy Wałek 1 ",1,1,"C",False)
pdf.image('Shaft1_MgXZ.png', 40, 25,120)
pdf.image('Shaft1_MgYZ.png', 40, 115,120)
pdf.image('Shaft1_Mg.png', 40, 205,120)

pdf.add_page()

pdf.image('Shaft1_T1.png', 40, 25,120)
pdf.image('Shaft1_Mg.png', 40, 115,120)
pdf.image('Shaft1_Mz.png', 40, 205,120)

pdf.add_page()

pdf.cell(0,16,"Zarys rzeczywisty wałka 1 ",1,1,"C",False)
pdf.image('Shaft1_diameter.png', 40, 35,120)

pdf.add_page()

pdf.cell(0,16,"Wałek 2 ",1,1,"C",False)

b("Wyznaczenie momentu obrotowego na wale 2:")
a1("T2= ",str(Ow.T2)," [N]")
b("Wyznaczenie siły obwodowej Ft21:")
a1("Ft21= ",str(round(Ow.Ft21,2))," [N]")
b("Wyznaczenie siły promieniowej Fr21:")
a1("Fr21= ",str(round((Ow.Fr21),2))," [N]")
b("Wyznaczenie siły obwodowej Ft34:")
a1("Ft34= ",str(round(Ow.Ft34,2))," [N]")
b("Wyznaczenie siły promieniowej Fr34:")
a1("Fr34= ",str(round((Ow.Fr34),2))," [N]")
b("Wyznaczenie siły wzdłużnej Fw34:")
a1("Fw34= ",str(round((Ow.Fw34),2))," [N]")

b("Obliczenie reakcji w podporach C i D")
b("Płaszczyzna XZ")
a1("Rcx= ",str(round((Ow.Rcx),2))," [N]")
a1("Rdx= ",str(round((Ow.Rdx),2))," [N]")
a1("Rcz= ",str(round((Ow.Rcz),2))," [N]")
b("Płaszczyzna YZ")
a1("Rcy= ",str(round((Ow.Rcy),2))," [N]")
a1("Rdy= ",str(round((Ow.Rdy),2))," [N]")
a1("Rcz= ",str(round((Ow.Rcz),2))," [N]")

pdf.add_page()
pdf.cell(0,16,"Wykresy Wałek 2 ",1,1,"C",False)
pdf.image('Shaft2_MgXZ.png', 40, 25,120)
pdf.image('Shaft2_MgYZ.png', 40, 115,120)
pdf.image('Shaft2_Mg.png', 40, 205,120)

pdf.add_page()

pdf.image('Shaft2_T2.png', 40, 25,120)
pdf.image('Shaft2_Mg.png', 40, 115,120)
pdf.image('Shaft2_Mz.png', 40, 205,120)

pdf.add_page()

pdf.cell(0,16,"Zarys rzeczywisty wałka 2 ",1,1,"C",False)
pdf.image('Shaft2_diameter.png', 40, 35,120)

pdf.add_page()

pdf.cell(0,16,"Wałek 3 ",1,1,"C",False)

b("Wyznaczenie momentu obrotowego na wale 3:")
a1("T3= ",str(Ow.T3)," [N]")
b("Wyznaczenie siły obwodowej Ft43:")
a1("Ft43= ",str(round(Ow.Ft43,2))," [N]")
b("Wyznaczenie siły promieniowej Fr43:")
a1("Fr43= ",str(round((Ow.Fr43),2))," [N]")
b("Wyznaczenie siły wzdłużnej Fw34:")
a1("Fw43= ",str(round((Ow.Fr43),2))," [N]")

b("Obliczenie reakcji w podporach C i D")
b("Płaszczyzna XZ")
a1("Rex= ",str(round((Ow.Rex),2))," [N]")
a1("Rfx= ",str(round((Ow.Rfx),2))," [N]")
a1("Rez= ",str(round((Ow.Rez),2))," [N]")
b("Płaszczyzna YZ")
a1("Rey= ",str(round((Ow.Rey),2))," [N]")
a1("Rfy= ",str(round((Ow.Rfy),2))," [N]")
a1("Rez= ",str(round((Ow.Rez),2))," [N]")

pdf.add_page()
pdf.cell(0,16,"Wykresy Wałek 3 ",1,1,"C",False)
pdf.image('Shaft3_MgXZ.png', 40, 25,120)
pdf.image('Shaft3_MgYZ.png', 40, 115,120)
pdf.image('Shaft3_Mg.png', 40, 205,120)

pdf.add_page()

pdf.image('Shaft3_T3.png', 40, 25,120)
pdf.image('Shaft3_Mg.png', 40, 115,120)
pdf.image('Shaft3_Mz.png', 40, 205,120)

pdf.add_page()

pdf.cell(0,16,"Zarys rzeczywisty wałka 3 ",1,1,"C",False)
pdf.image('Shaft3_diameter.png', 40, 35,120)


pdf.output('Raport.pdf')


