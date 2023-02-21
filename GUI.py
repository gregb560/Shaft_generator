import tkinter as tk
from tkinter import messagebox

def Enter_data():
    EnginePower = DataEnginePower.get()
    NumberTeeth = DataNumberTeeth.get()
    RPM = DataRPM.get()
    GearBoxRatio = DataGearBoxRatio.get()
    print("Moc silnika: ",EnginePower,"Liczba zębów koła 1: ",NumberTeeth)
    print("RPM: ", RPM, "Całkowite przełożenie: ", GearBoxRatio)




root = tk.Tk()
#Set the geometry of frame
root.geometry("1200x600")

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


LabelDaneWejsciowe = tk.Label(root, text = "Dane wejściowe",font = ("Arial", 20),)
LabelDaneWejsciowe.grid(row = 0, column = 0)

#  MOC SILNIKA
frame1 = tk.LabelFrame(root,text="Moc wejściowa silnika",font = ("Arial", 14))
frame1.grid(row = 1, column = 0,padx = 20,pady = 20, ipadx = 20, ipady = 20)

LabelMocWejsciowa = tk.Label(frame1,text = "N",font = ("Arial", 12))
LabelMocWejsciowa.grid( row = 0, column = 0 , padx = 10, pady =10)
DataEnginePower = tk.IntVar()
TextBox = tk.Entry (frame1,textvariable = DataEnginePower)
TextBox.grid(row = 0, column = 1)

LabelJednostka = tk.Label(frame1,text = "[kW]",font = ("Arial", 12))
LabelJednostka.grid( row = 0, column = 2 , padx = 10, pady =10)

LabelDaneWejsciowe.grid( row = 0,column= 1,sticky = 'N')

#  LICZBA ZĘBÓW KOŁA 1


frame2 = tk.LabelFrame(root,text="Liczba zębów koła 1",font = ("Arial", 14))
frame2.grid(row = 2, column = 0,padx = 20,pady = 20, ipadx = 20, ipady = 20)

LabelGearTooth = tk.Label(frame2,text = "z1",font = ("Arial", 12))
LabelGearTooth.grid( row = 0, column = 0 , padx = 10, pady =10)

DataNumberTeeth = tk.IntVar()
TextBox = tk.Entry (frame2,textvariable = DataNumberTeeth)
TextBox.grid(row = 0, column = 2)


LabelJednostka = tk.Label(frame2,text = "[-]",font = ("Arial", 12))
LabelJednostka.grid( row = 0, column = 3 , padx = 10, pady =10)


# Liczba obrotów silnika

frame3 = tk.LabelFrame(root,text="Liczba obrotów silnika",font = ("Arial", 14))
frame3.grid(row = 2, column = 1,padx = 20,pady = 20, ipadx = 20, ipady = 20)

LabelEngineRPM = tk.Label(frame3,text = "n1",font = ("Arial", 12))
LabelEngineRPM.grid( row = 0, column = 0 , padx = 10, pady =10)

DataRPM = tk.IntVar()
TextBox = tk.Entry (frame3,textvariable = DataRPM)
TextBox.grid(row = 0, column = 1)


LabelJednostka = tk.Label(frame3,text = "[RPM]",font = ("Arial", 12))
LabelJednostka.grid( row = 0, column = 3 , padx = 10, pady =10)



# Przełozenie przekładni

frame4 = tk.LabelFrame(root,text="Przełożenie przekładni",font = ("Arial", 14))
frame4.grid(row = 1, column = 1,padx = 20,pady = 20, ipadx = 20, ipady = 20)

LabelGearBoxRatio = tk.Label(frame4,text = "i",font = ("Arial", 12))
LabelGearBoxRatio.grid( row = 0, column = 0 , padx = 10, pady =10)

DataGearBoxRatio = tk.IntVar()
TextBox = tk.Entry (frame4,textvariable = DataGearBoxRatio)
TextBox.grid(row = 0, column = 1)


LabelJednostka = tk.Label(frame4,text = "[-]",font = ("Arial", 12))
LabelJednostka.grid( row = 0, column = 3 , padx = 10, pady =10)

# Wporwadzenie danych

ButtonEnterData = tk.Button(root,command = Enter_data, text = "Wprowadz dane",font = ("Arial", 16))
ButtonEnterData.grid(row=3, column=1, sticky='W')

#Wywołanie okna
root.mainloop()
