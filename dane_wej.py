# Dane główne
N = 15
z1 = 17
n1 = 3000
i = 9

#Dane stali 55/C55
s55_Kgo = 90   #[MPa]
s55_kH = 600 #[MPa]

#Dane stali St7/E360
st7_Kgo = 85 #[MPa]
st7_Ksj = 85 #[MPa]

def dane():
    print(" Dane wejściowe: ")
    print("Moc silnika N: " + str(N) + "[kW]")
    print("Obroty silnika n: " + str(n1) + "[rpm]")
    print("Przełożenie całkowite przekładni i= " + str(i) + "[-]")
    print("Liczna zębów koła 1 " + str(z1) + "[-]")