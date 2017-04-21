
import re
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("spanish")
expresionExperimental_1 = "ción;miento;sión;es;s"


#normaliza terminos del diccionario para buscarlos en el texto
#   el orden de las expresiones regulares importa
def normalizar(texto, expresiones = expresionExperimental_1):
    arreglo = expresiones.split(";")

    for ex in arreglo:
        texto= re.sub(ex + r" "," ",texto)
        texto= re.sub(ex + r"$","",texto)
    return texto

#entrega la lista original con las palabras recortadas según las reglas en el
#stemmer
def stemArray(words):
    lista = []
    for word in words:
        palabras = word.split()
        termino = ""
        for palabra in palabras:
            termino += stemmer.stem(palabra) + " "
        termino = termino[:-1]
        lista.append(termino)
    return lista

#entrega la lista original con las palabras recortadas según las reglas en la
# funcion normalizar
def customStems(words):
    lista = []
    for word in words:
        palabras = word.split()
        termino = ""
        for palabra in palabras:
            termino += normalizar(palabra) + " "
        termino = termino[:-1]
        lista.append(termino)
    return lista

#entrega indice del diccionario si hay coincidencia, sino -1
# inicial por default 0
# final por default len(dicc-1)
def binarySearchDicc(texto, posicion, dicc, lista, comp):
    inicial = 0
    final = len(dicc)-1
    encontrado = -1
    arreglo = []
    while inicial<=final and encontrado == -1:
        medio = (inicial + final)//2
        #conceptoNorm = normalizar(dicc[medio])  -> se normaliza antes
        arreglo = dicc[medio].split(" ")
        
        if comp(texto[posicion],arreglo[0]):
            encontrado = medio
        else:
            if texto[posicion] < arreglo[0]:
                final = medio -1
            elif texto[posicion] > arreglo[0]:
                inicial = medio +1
    #continua comparando si encuentra coincidencias con la primera palabra
    #return encontrado
    if encontrado != -1:
        buscarCerca(texto, encontrado, dicc, lista, posicion, -1, comp)
        buscarCerca(texto, encontrado, dicc, lista, posicion, 0, comp)
        buscarCerca(texto, encontrado, dicc, lista, posicion, 1, comp)



#tras encontrar una coincidencia busca otras coincidencias en los términos
#cercanos
def buscarCerca(texto, posicionDicc, dicc, lista, posicionTexto, direccion, comp):
    posicionDicc+=direccion

    #si se pasa de los limites, retorna
    if posicionDicc < 0 or posicionDicc >= len(dicc):
        return
    arreglo = dicc[posicionDicc].split(" ")

    #por el orden del diccionario, si se encuentra el primer termino retorna
    #   el diccionario posee la palabra base y luego las compuestas
    if len(arreglo)==1 and comp(texto[posicionTexto],arreglo[0]):
        lista.append(posicionDicc)
        return
    while comp(texto[posicionTexto],arreglo[0]):
        if continuarRevisando(arreglo, texto, posicionTexto, comp):
            lista.append(posicionDicc)
        posicionDicc+=direccion
        if posicionDicc < 0 or posicionDicc >= len(dicc) or direccion == 0:
            return
        arreglo = dicc[posicionDicc].split(" ")


#tras encontrar coincidencias continúa comparando el termino del diccionario
#con las siguientes palabras del texto si el termino tiene más de una palabra 
def continuarRevisando(arreglo, texto, posicion, comp):
    if len(arreglo)>1:        
        for i in range(1,len(arreglo)):
            if (posicion+i >= len(texto)):
                return False
            condicion = comp(texto[posicion+i],(arreglo[i]))
            if condicion == False:
                return False
    return True




