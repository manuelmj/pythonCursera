

import calcular_indices as cal

def imprimirResultados(): 
    peso=float(input("ingrese el peso de la persona: "))
    altura=float(input("ingrese la altura de la persona: "))
    edad=int(input("ingrese la edad de la persona: "))
    valor_genero=float(input("ingrese el valor de genero de la persona: "))
    porcentaje=cal.calcular_porcentaje_grasa(peso,altura,edad,valor_genero)
    porcentaje=round(porcentaje,2)
    print("el porcentaje de grasa de la persona es:",porcentaje,"%")


imprimirResultados()  