



def leerArchivo(archivo:str)->list: 
    """(1)
    lee un archivo en formato csv y guarda toda la informacion
    organizada en una lista de diccionarios
    """
    ListaCanciones=[]  
    DatosArchivo=open(archivo)
    titulo=DatosArchivo.readline().split(",")
    i=0
    linea=DatosArchivo.readline()
    while len(linea) > 0:
        Datos=linea.split(",")
        informacionCanciones={}
        for i in range(0,len(Datos)):
            informacionCanciones[titulo[i]]=Datos[i]
        ListaCanciones.append(informacionCanciones)
        linea=DatosArchivo.readline()
    DatosArchivo.close()
    
    return (ListaCanciones)


def informacionCancion(listacanciones:list,nombreCancion:str,anio:int)->dict:
    """(2)
    esta funcion devuelve la informacion de una cancion que se encuentre en el 
    ranking de el año ingresado"""
    informacionCancion={}
    anio=str(anio) 
    for informacion in listacanciones:      
        if informacion["Song"] == nombreCancion and informacion["Year"] == anio:
            informacionCancion=informacion   
        else : 
            informacionCanion=None
    return informacionCancion

def cancionesAnio(listacanciones:list,anio:int)->list: 
    """(3)
    devuelve la informacion de las canciones que hacen parte del 
    ranking de un año en especifico"""
    listacancionesanio=[]
    for informacion in listacanciones: 
        llaves=list(informacion.keys())
        if informacion["Year"]==str(anio):
            diccionarioCancionesAnio={}
            diccionarioCancionesAnio[llaves[0]]=informacion[llaves[0]]
            diccionarioCancionesAnio[llaves[1]]=informacion[llaves[1]]
            diccionarioCancionesAnio[llaves[2]]=informacion[llaves[2]]
            diccionarioCancionesAnio[llaves[3]]=informacion[llaves[3]]
            listacancionesanio.append(diccionarioCancionesAnio) 
    return(listacancionesanio)



def cancionesArtistaAnio(listacanciones:list,nombre:str,anioInicio:int,anioFinal:int)->list: 
    """(4)
        devuelve todas las canciones que haya interpretado un artista en un tiempo definido
        entre dos años
                        """
    listacancionesanio=[]
    for informacion in listacanciones: 
        llaves=list(informacion.keys())
        anio=int(informacion[llaves[3]]) 
        if informacion[llaves[2]]==nombre and (anio<= anioFinal and anio>=anioInicio):
            diccionarioCancionesAnio={}
            diccionarioCancionesAnio[llaves[0]]=informacion[llaves[0]]
            diccionarioCancionesAnio[llaves[1]]=informacion[llaves[1]]
            diccionarioCancionesAnio[llaves[2]]=informacion[llaves[2]]
            diccionarioCancionesAnio[llaves[3]]=informacion[llaves[3]]
            listacancionesanio.append(diccionarioCancionesAnio) 
    return(listacancionesanio)




def cancionesArtista(listacanciones:list,nombre:str)->list: 
    """(5)
        devuelve la informacion de las canciones que haya interpretado el artista 
    """
    listacancionesanio=[] 
    for informacion in listacanciones: 
        llaves=list(informacion.keys())
        if informacion[llaves[2]]==nombre:
            diccionarioCancionesAnio={}
            diccionarioCancionesAnio[llaves[0]]=informacion[llaves[0]]
            diccionarioCancionesAnio[llaves[1]]=informacion[llaves[1]]
            diccionarioCancionesAnio[llaves[2]]=informacion[llaves[2]]
            diccionarioCancionesAnio[llaves[3]]=informacion[llaves[3]]
            listacancionesanio.append(diccionarioCancionesAnio) 
    return(listacancionesanio)


def cancionesNombreArtista(listacanciones:list,nombre:str)->list: 
    """(6)
        devuelve el nombre de los artistas que hayan interpretado una cancion
        a lo largo de todos los años dentro del archivo
        """
    listacancionesanio=[]
    for informacion in listacanciones: 
        llaves=list(informacion.keys())
        if informacion[llaves[1]]==nombre:
            listacancionesanio.append(informacion[llaves[2]]) 
    return(listacancionesanio)

def numeroCancionesArtista(listacanciones:list,numero:int)->dict: 
    """(7)
        devuelve la informacion de los artistas que hayan interpretado 
        canciones mayores o iguales a un numero determinado 
        """
    numeroCancionesArtista={}
    numeroCancionesArtistaMayorA={}
    
    for informacion in listacanciones:
        llaves=list(informacion.keys())
        nombre=informacion[llaves[2]]
        veces=numeroCancionesArtista.get(nombre,0)
        numeroCancionesArtista[nombre]=veces+1 
        
        numeroEntero=int(numeroCancionesArtista[nombre])
        if numeroEntero>=numero: 
            numeroCancionesArtistaMayorA[nombre]=numeroCancionesArtista[nombre]
                
    return (numeroCancionesArtistaMayorA)

def ArtistaConMasCanciones(listacanciones:list)->dict: 
    """(8)
        devuelve el nombre de la  persona que ha interpretado mas canciones
        dentro del documento
        a lo largo de los años 
        """
    numeroCancionesArtista={}
    artistaMayorNumeroCanciones={}
    numero=0
    for informacion in listacanciones:
        llaves=list(informacion.keys())
        nombre=informacion[llaves[2]]
        veces=numeroCancionesArtista.get(nombre,0)
        numeroCancionesArtista[nombre]=veces+1 
        
    for informacionDic in numeroCancionesArtista.keys(): 
        numeroEntero=int(numeroCancionesArtista[informacionDic])
        if  numeroEntero> numero: 
            llaves=informacionDic
            numero=numeroCancionesArtista[informacionDic]
    artistaMayorNumeroCanciones[llaves]=numero
             
    return (artistaMayorNumeroCanciones)

def listaCancionesArtista(listacanciones:list)->dict:
    """(9)
    devuelve un diccionario con la lista de canciones que ha interpretado cada artista """
    diccionarioCantantes={}
        
    for informacion in listacanciones:
        llaves=list(informacion.keys())
        nombre=informacion[llaves[2]]
        valor=diccionarioCantantes.get(nombre,0)
        if valor == 0:
            listaCancionesArtistas=[]
            for informacion1 in listacanciones: 
                nombre1=informacion1[llaves[2]]
                cancion=informacion1[llaves[1]]
            
                if nombre == nombre1:
                    listaCancionesArtistas.append(cancion)
            diccionarioCantantes[nombre]=listaCancionesArtistas        

        
    return diccionarioCantantes


def promedioCancionesArtistas(listacanciones:list)->float: 
    promedio=0 
    nombresArtista={}
    cancionesArtista={}
    artistasDiferentes=0
    cancionesDiferentes=0
    for informacion in listacanciones: 
        llaves=list(informacion.keys())
        nombre=informacion[llaves[2]]
        cancion=informacion[llaves[1]]
        vecesnombre=nombresArtista.get(nombre,0)
        vecescanciones=cancionesArtista.get(nombre,0)
        
        if vecesnombre==0: 
            nombresArtista[nombre]=1
            artistasDiferentes+=1
        if vecescanciones==0: 
            cancionesArtista[cancion]=1
            cancionesDiferentes+=1
    promedio=cancionesDiferentes/artistasDiferentes
              
    return round(promedio,3)


#Canciones=leerArchivo("billboard.csv")
#print(informacionCancion(Canciones,"wooly bully",1965))
#print(cancionesAnio(Canciones,2016))
#print(cancionesArtistaAnio(Canciones,"daughtry",1965,2007))
#print(cancionesArtista(Canciones,"daughtry"))
#print(cancionesNombreArtista(Canciones,"in the end"))
#print(numeroCancionesArtista(Canciones,25))
#print(ArtistaConMasCanciones(Canciones))
#print(listaCancionesArtista(Canciones))
#print(promedioCancionesArtistas(Canciones))