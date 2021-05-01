
def calcular_IMC(peso :float, altura: float)->float:
    return (peso/(altura**2))

def calcular_porcentaje_grasa(peso:float,altura :float,edad:int,valor_genero:float)->float:
    imc=calcular_IMC(peso,altura)
    gc=(1.2*imc)+(0.23*edad)-5.4-valor_genero
    return(gc)    

def calcular_calorias_en_reposo(peso:float,altura:float,edad:int,valor_genero:float)->float:
    tmb=(10*peso)+(6.25*(altura))-(5*edad)+valor_genero
    return(tmb)    

def calcular_calorias_en_actividad(peso:float,altura:float,edad:int,valor_genero:float,valor_actividad:float)->float:
    tmb=calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    tmb_=tmb*valor_actividad
    return(tmb_)    

def consumo_calorias_recomendado_para_adelgazar(peso:float,altura:float,edad:int,valor_genero:float)->str:
   tmb=calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
   consumo_inferior=tmb-(tmb*0.15)
   consumo_inferior=str(consumo_inferior)
   consumo_superior=tmb-(tmb*0.2)
   consumo_superior=str(consumo_superior)
   return('Para adelgazar es recomendado que consumas entre: '+ consumo_superior+' y '+consumo_inferior +'  calorías al día.')    

