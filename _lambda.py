def Line_ax_plus_b(z1,z2,z3,lambda1,lambda3):
    """

    :param z1: Ilość zębów koła - liczba zaczynjący przedział wartości
    :param z2: Ilość zębów dla koła szukanego
    :param z3: Ilość zębów koła - liczba kończąca przedział wartości
    :param lambda1: Wspołczynnik λ zaczynjący przedział wartości
    :param lambda3: Wspołczynnik λ kończący przedział wartości
    :return: Szukana wartość λ dla koła o liczbie zebów z2
    """
    lambda2 = ((z2 - z1) * (lambda3-lambda1)/(z3-z1)) + lambda1
    return lambda2




Factor_Maag = {
                0.352 : 16,
                0.363 : 18,
                0.375: 20,
                0.397 : 25,
                0.410 : 30,
                0.435 : 40,
                0.445 : 50,
                0.456 : 60,
                0.469 : 80,
                0.481 : 100,
                0.495 : 150,
                0.505 : 200
              }
# Szukanie po value
def found_factor(Factor_Maag,value):

        for keys in Factor_Maag:
            if Factor_Maag[keys] == value:
                foundKey = []
                foundKey.append(keys)
                return foundKey[0]
            elif value <= 14:
                return 0
            elif value == 15:
                return Line_ax_plus_b(14, value, Factor_Maag.pop(0.352), 0, 0.352)
            elif value > 16 and value < 18 :
                return Line_ax_plus_b(Factor_Maag.pop(0.352), value, Factor_Maag.pop(0.363), 0.352, 0.363)
            elif value > 18 and value < 20:
                return Line_ax_plus_b(Factor_Maag.pop(0.363), value, Factor_Maag.pop(0.375), 0.363, 0.375)
            elif value > 20 and value < 25:
                return Line_ax_plus_b(Factor_Maag.pop(0.375), value, Factor_Maag.pop(0.397), 0.375, 0.397)
            elif value > 25 and value < 30:
                return Line_ax_plus_b(Factor_Maag.pop(0.397), value, Factor_Maag.pop(0.410), 0.397, 0.410)
            elif value > 30 and value < 40:
                return Line_ax_plus_b(Factor_Maag.pop(0.410), value, Factor_Maag.pop(0.435), 0.410, 0.435)
            elif value > 40 and value < 50:
                return Line_ax_plus_b(Factor_Maag.pop(0.435), value, Factor_Maag.pop(0.445), 0.435, 0.445)
            elif value > 50 and value < 60:
                return Line_ax_plus_b(Factor_Maag.pop(0.445), value, Factor_Maag.pop(0.456), 0.445, 0.456)
            elif value > 60 and value < 80:
                return Line_ax_plus_b(Factor_Maag.pop(0.456), value, Factor_Maag.pop(0.469), 0.456, 0.469)
            elif value > 80 and value < 100:
                return Line_ax_plus_b(Factor_Maag.pop(0.469), value, Factor_Maag.pop(0.481), 0.469, 0.481)
            elif value > 100 and value < 150:
                return Line_ax_plus_b(Factor_Maag.pop(0.481), value, Factor_Maag.pop(0.495), 0.481, 0.495)
            elif value > 150 and value < 200:
                return Line_ax_plus_b(Factor_Maag.pop(0.495), value, Factor_Maag.pop(0.505), 0.495, 0.505)



Factor_Maag1 = {
                 16: 0.352 ,
                 18: 0.363,
                 20: 0.375,
                 25: 0.397,
                 30: 0.410,
                 40: 0.435,
                 50: 0.445,
                 60: 0.456,
                 80: 0.469,
                 100: 0.481,
                 150: 0.495,
                 200: 0.505
              }

# Szukanie po key (kluczu)
def found_factor1(Factor_Maag1,key):

        if key in Factor_Maag1:
            return(Factor_Maag1[key])




print(found_factor1(Factor_Maag1,17))

