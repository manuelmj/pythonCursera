"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """   
    diccionario={"nombre":nombre,"genero":genero,"duracion":duracion,"anio":anio,"clasificacion":clasificacion,"hora":hora,"dia":dia} 
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return (diccionario)

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    resultado=None 
    if p1["nombre"]==nombre_pelicula: 
        resultado=p1
    elif p2["nombre"]==nombre_pelicula:
        resultado=p2
    elif p3["nombre"]==nombre_pelicula:
        resultado=p3
    elif p4["nombre"]==nombre_pelicula:
        resultado=p4
    elif p5["nombre"]==nombre_pelicula:
        resultado=p5 
                          
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return (resultado)

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    mayor=p1["duracion"]
    diccionario=p1
    if p2["duracion"]>mayor: 
        mayor=p2["duracion"]
        dicionario=p2
    if p3["duracion"]>mayor: 
        mayor=p3["duracion"]
        dicionario=p3
    if p4["duracion"]>mayor: 
        mayor=p4["duracion"]
        dicionario=p4
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return(dicionario)

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    promedio=p1["duracion"]+p2["duracion"]+p3["duracion"]+p4["duracion"]
    promedio=promedio//4
    horas=promedio//60 
    minutos=promedio-(horas*60)
    formato=str(horas)+":"+str(minutos)
     
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return (formato)


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    nombre1="-"
    nombre2="-"
    nombre3="-"
    nombre4="-"
    nombre5="-"
    if p1["anio"]>anio: 
        nombre1=p1["nombre"]
    if p2["anio"]>anio:
        nombre2=p2["nombre"]
    if p3["anio"]>anio: 
        nombre3=p3["nombre"]
    if p4["anio"]>anio: 
        nombre4=p4["nombre"]
    if p5["anio"]>anio: 
        nombre5=p5["nombre"]

    nombre=nombre1+' '+nombre2+' '+nombre3+' '+nombre4+' '+nombre5
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return (nombre)

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '"18+"+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '"18+"+'
    """
    numero=0
    if p1["clasificacion"]>"18+":
        numero+=1
    if p2["clasificacion"]>"18+": 
        numero+=1
    if p3["clasificacion"]>"18+": 
        numero+=1
    if p4["clasificacion"]>"18+": 
        numero+=1
    if p5["clasificacion"]>"18+": 
        numero+=1
 
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return(numero)

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    if control_horario==True:   
        
        if  (p1["dia"]==nuevo_dia  and p1["hora"]== nueva_hora)or(p2["dia"]==nuevo_dia  and p2["hora"]== nueva_hora)or(p3["dia"]==nuevo_dia  and p3["hora"]== nueva_hora)or(p4["dia"]==nuevo_dia  and p4["hora"]== nueva_hora)or(p5["dia"]==nuevo_dia  and p5["hora"]== nueva_hora):
                resultado=False 
        elif(p1["genero"]=="Documental"  and p1["hora"]>=2200)or(p2["genero"]=="Documental"  and p2["hora"]>=2200)or(p3["genero"]=="Documental"  and p3["hora"]>=2200)or(p4["genero"]=="Documental"  and p4["hora"]>=2200)or(p5["genero"]=="Documental"  and p5["hora"]>=2200) : 
            resultado=False
        elif (p1["genero"]=="drama"  and p1["dia"]=="Viernes")or (p2["genero"]=="drama" and p2["dia"]=="Viernes")or  (p3["genero"]=="Drama" and p3["dia"]=="Viernes") or (p4["genero"]=="Drama"and p4["dia"]=="Viernes") or (p5["genero"]=="Drama" and p5["dia"]=="Viernes") : 
            resultado=False   
        elif ("lunes" or "martes" or "miercoles" or "jueves" or "viernes") in p1["dia"] and (p1["hora"]>2300 or p1["hora"]<600):
                resultado=False    
        elif ("lunes" or "martes" or "miercoles" or "jueves" or "viernes") in p2["dia"] and (p2["hora"]>2300 or p2["hora"]<600):
                resultado=False                   
        elif ("lunes" or "martes" or "miercoles" or "jueves" or "viernes") in p3["dia"] and (p3["hora"]>2300 or p3["hora"]<600):
                resultado=False                   
        elif ("lunes" or "martes" or "miercoles" or "jueves" or "viernes") in p4["dia"] and (p4["hora"]>2300 or p4["hora"]<600):
            resultado=False                   
        elif ("lunes" or "martes" or "miercoles" or "jueves" or "viernes") in p5["dia"] and (p5["hora"]>2300 or p5["hora"]<600):
                resultado=False  
        else : 
            resultado=True                               
    elif (p1["dia"]==nuevo_dia  and p1["hora"]== nueva_hora)or(p2["dia"]==nuevo_dia  and p2["hora"]== nueva_hora)or(p3["dia"]==nuevo_dia  and p3["hora"]== nueva_hora)or(p4["dia"]==nuevo_dia and p4["hora"]== nueva_hora)or(p5["dia"]==nuevo_dia and p5["hora"]== nueva_hora):
        resultado=False
    else : 
        resultado=True           
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
  
    return (resultado)
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    resultado=False  
    if edad_invitado>=18: 
        resultado=True
    else :  
        if edad_invitado<15 and peli["genero"]=="Terror": 
            resultado=False 
        elif edad_invitado<=10  and peli["genero"]!="Familiar": 
            resultado=False 
        elif not(str(edad_invitado) in peli["clasificacion"]) and (autorizacion_padres==True or peli["genero"]=="Documental"):
            resultado=True             
        
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return resultado









