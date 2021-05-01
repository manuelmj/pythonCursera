

import calcular_indices as cal

def imprimirResultados(): 
    peso=float(input("ingrese el peso de la persona: "))
    altura=float(input("ingrese la altura de la persona: "))
    edad=int(input("ingrese la edad de la persona: "))
    valor_genero=float(input("ingrese el valor de genero de la persona: "))
    calReposo=cal.calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    calReposo=round(calReposo,2)
    print("la cantidad de calorias en reposo de la persona es de: ",calReposo,"cal")

imprimirResultados()