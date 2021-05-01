


import calcular_indices as cal

def imprimirResultados(): 
    peso=float(input("ingrese el peso de la persona: "))
    altura=float(input("ingrese la altura de la persona: "))
    edad=int(input("ingrese la edad de la persona: "))
    valor_genero=float(input("ingrese el valor de genero de la persona: "))
    str=cal.consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,valor_genero)
    print(str)

imprimirResultados()  