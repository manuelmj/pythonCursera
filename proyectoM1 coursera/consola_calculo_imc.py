


import calcular_indices as cal





def pedirDatos():
    peso=float(input("ingrese el peso el peso de la persona: "))
    altura=float(input("ingrese la altura de la persona: "))
    imc=cal.calcular_IMC(peso,altura)
    imc=round(imc,2)
    print("el indice corporal de la persona es: ",imc)

pedirDatos()