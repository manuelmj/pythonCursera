



import calcular_indices as cal

def imprimirResultados(): 
    peso=float(input("ingrese el peso de la persona: "))
    altura=float(input("ingrese la altura de la persona: "))
    edad=int(input("ingrese la edad de la persona: "))
    valor_genero=float(input("ingrese el valor de genero de la persona: "))
    valor_actividad=float(input("ingrese el valor de actividad de la persona: "))
    caloriasActividad=cal.calcular_calorias_en_actividad(peso,altura,edad,valor_genero,valor_actividad)
    caloriasActividad=round(caloriasActividad,2)
    print("la cantidad de calorias en actividad de la persona es de: ",caloriasActividad)

imprimirResultados()  