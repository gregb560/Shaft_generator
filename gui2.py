import tkinter as tk
from tkinter import ttk
import wzory_kol as wk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Przykładowa aplikacja")
        self.geometry("700x500")

        # Utworzenie widżetu Notebook (zakładek)
        self.notebook = tk.ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Utworzenie pierwszej karty z tekstem
        self.first_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.first_frame, text="Pierwsza karta")

        #Dane wejsciowe
        self.LabelDaneWejsciowe = tk.Label(self.first_frame, text="Dane wejściowe", font=("Arial", 20), )
        self.LabelDaneWejsciowe.grid(row=0, column=0)
        self.LabelDaneWejsciowe.grid(row=0, column=1, sticky='N')

        #Moc silnika
        self.DataFrame = tk.LabelFrame(self.first_frame, text="Moc wejściowa silnika", font=("Arial", 14))
        self.DataFrame.grid(row=1, column=0, padx=20, pady=20, ipadx=20, ipady=20)
        self.LabelData = tk.Label(self.DataFrame, text="N =", font=("Arial", 12))
        self.LabelData.grid(row=0, column=0, padx=10, pady=10)

        self.DataEnginePower = tk.IntVar()

        self.TextBox = tk.Entry(self.DataFrame, textvariable=self.DataEnginePower)
        self.TextBox.grid(row=0, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[kW]", font=("Arial", 12))
        self.LabelJednostka.grid(row=0, column=2, padx=10, pady=10)

        #Koło zębate 1
        self.DataFrame = tk.LabelFrame(self.first_frame, text="Liczba zębów koła 1", font=("Arial", 14))
        self.DataFrame.grid(row=2, column=0, padx=20, pady=20, ipadx=20, ipady=20)
        self.LabelData = tk.Label(self.DataFrame, text="z1 =", font=("Arial", 12))
        self.LabelData.grid(row=0, column=0, padx=10, pady=10)

        self.DataNumberTeeth = tk.IntVar()

        self.TextBox = tk.Entry(self.DataFrame, textvariable=self.DataNumberTeeth)
        self.TextBox.grid(row=0, column=2)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-]", font=("Arial", 12))
        self.LabelJednostka.grid(row=0, column=3, padx=10, pady=10)

        #Liczba obrotów silnika
        self.DataFrame = tk.LabelFrame(self.first_frame, text="Liczba obrótw silnika ", font=("Arial", 14))
        self.DataFrame.grid(row=2, column=1, padx=20, pady=20, ipadx=20, ipady=20)
        self.LabelData = tk.Label(self.DataFrame, text="n1 =", font=("Arial", 12))
        self.LabelData.grid(row=0, column=0, padx=10, pady=10)

        self.DataRPM = tk.IntVar()

        self.TextBox = tk.Entry(self.DataFrame, textvariable=self.DataRPM)
        self.TextBox.grid(row=0, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[RPM]", font=("Arial", 12))
        self.LabelJednostka.grid(row=0, column=3, padx=10, pady=10)

        #Przełożenie przekladni
        self.DataFrame = tk.LabelFrame(self.first_frame, text="Całkowite przełozenie", font=("Arial", 14))
        self.DataFrame.grid(row=1, column=1, padx=20, pady=20, ipadx=20, ipady=20)
        self.LabelData = tk.Label(self.DataFrame, text="i =", font=("Arial", 12))
        self.LabelData.grid(row=0, column=0, padx=10, pady=10)

        self.DataGearBoxRatio = tk.IntVar()

        self.TextBox = tk.Entry(self.DataFrame, textvariable=self.DataGearBoxRatio)
        self.TextBox.grid(row=0, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-]", font=("Arial", 12))
        self.LabelJednostka.grid(row=0, column=3, padx=10, pady=10)

        #Przycisk wprowadzenia danych
        self.ButtonEnterData = tk.Button(self.first_frame, command=self.Enter_data, text="Wprowadz dane", font=("Arial", 16))
        self.ButtonEnterData.grid(row=3, column=1, sticky='W')







        #Utworzenie drugiej karty z tłem
        self.second_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.second_frame, text="Obliczenia")

        # Kalkulacja danych
        self.ButtonGearCalculate = tk.Button(self.second_frame, command=self.Gears_Calculation, text="Oblicz",
                                             font=("Arial", 16))
        self.ButtonGearCalculate.grid(row=3, column=1, sticky='W')


        # Obliczenia
        self.DataFrame = tk.LabelFrame(self.second_frame,text = "Obliczenie kół zębatych",font = ("Arial",14))
        self.DataFrame.grid(row=1, column=1, padx=20, pady=20, ipadx=20, ipady=20)








        self.i12 = tk.IntVar()

        #Przełożenie 1-2
        self.LabelData = tk.Label(self.DataFrame, text=f"Przełożenie pary i12: {self.i12}", font=("Arial", 12))
        self.LabelData.grid(row=0, column=0, padx=10, pady=10)

        self.TextBox = tk.Entry(self.DataFrame, textvariable=self.Gears_Calculation)
        self.TextBox.grid(row=0, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-] - Przełozenie pary 12", font=("Arial", 12))
        self.LabelJednostka.grid(row=0, column=3, padx=10, pady=10)

        #Przełożenie 3-4
        self.LabelData = tk.Label(self.DataFrame, text="i34 =", font=("Arial", 12))
        self.LabelData.grid(row=1, column=0, padx=10, pady=10)

        self.TextBox = tk.Entry(self.DataFrame, textvariable=2)
        self.TextBox.grid(row=1, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-] - Przełozenie pary 3-4", font=("Arial", 12))
        self.LabelJednostka.grid(row=1, column=3, padx=10, pady=10)


        # Przyjęcie liczby zębów koła 3

        self.LabelData = tk.Label(self.DataFrame, text="z3 =", font=("Arial", 12))
        self.LabelData.grid(row=3, column=0, padx=10, pady=10)

        self.TextBox = tk.Entry(self.DataFrame, textvariable=2)
        self.TextBox.grid(row=3, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-] - Liczba zębów koła 3", font=("Arial", 12))
        self.LabelJednostka.grid(row=3, column=3, padx=10, pady=10)

        #Obliczenie liczby zębów koła 2

        self.LabelData = tk.Label(self.DataFrame, text="z2 =", font=("Arial", 12))
        self.LabelData.grid(row=2, column=0, padx=10, pady=10)

        self.TextBox = tk.Entry(self.DataFrame, textvariable=2)
        self.TextBox.grid(row=2, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-] - Liczba zębów koła 2", font=("Arial", 12))
        self.LabelJednostka.grid(row=2, column=3, padx=10, pady=10)

        # Obliczenie zębów koła 4

        self.LabelData = tk.Label(self.DataFrame, text="z4 =", font=("Arial", 12))
        self.LabelData.grid(row=4, column=0, padx=10, pady=10)

        self.TextBox = tk.Entry(self.DataFrame, textvariable=2)
        self.TextBox.grid(row=4, column=1)

        self.LabelJednostka = tk.Label(self.DataFrame, text="[-] - Liczba zębów koła 4", font=("Arial", 12))
        self.LabelJednostka.grid(row=4, column=3, padx=10, pady=10)





    def Enter_data(self):
            self.EnginePower = self.DataEnginePower.get()
            self.NumberTeeth = self.DataNumberTeeth.get()
            self.RPM = self.DataRPM.get()
            self.GearBoxRatio = self.DataGearBoxRatio.get()

            self.i12 = round(wk.Gear_ratio_first_pair(1.2, self.GearBoxRatio), 1)
            print("Moc silnika: ", self.EnginePower, "Liczba zębów koła 1: ", self.NumberTeeth)
            print("RPM: ", self.RPM, "Całkowite przełożenie: ", self.GearBoxRatio)

    def Gears_Calculation(self):
        self.i12 = round(wk.Gear_ratio_first_pair(1.2, self.GearBoxRatio), 1)
        # self.i34 = round(wk.Gear_ratio_next_pair(self.GearBoxRatio, self.i12), 1)
        # self.GearNumber = self.DataGear3Number.get()
        # self.z2 = wk.Gear_teeth_number(self.GearBoxRatio, self.NumberTeeth)
        # self.z4 = wk.Gear_teeth_number(self.i34, self.GearNumber)






if __name__ == "__main__":
    app = Application()
    app.mainloop()