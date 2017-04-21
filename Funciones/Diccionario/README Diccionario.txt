Instrucciones para la utilizaci�n de las herramientas para buscar en un Diccionario

Las siguientes instrucciones son para el manejo de los m�todos escritos en Python con el fin de obtener los t�rminos de un texto presentes en un diccionario.

La versi�n de Python utilizada es la 3.5.2, debido a las restricciones del instalador del toolkit.

El toolkit en cuesti�n es NLTK 3.0, que se puede encontrar en: http://www.nltk.org/install.html

En general basta utilizar DirectoryDict de la forma ejemplificada al final del archivo

Archivos:

	-. ProcesadorDeTexto.py: posee la clase del mismo nombre, encargada de guardar el nombre de un archivo y su ruta.
		Sus m�todos son:
			loadText: carga el texto y lo guarda.
			getText: retorna el texto guardado

	-. Diccionario.py: extiende a la clase ProcesadorDeTexto, recibiendo los mismos par�metros. Sirve para obtener los t�rminos del diccionario y guardarlos en orden alfab�tico en un arreglo.
		Sus m�todos son:
			clean: pasa el texto a lowercase
			loadWords: separa los t�rminos del texto en un arreglo y las ordena
			getWords: devuelve la lista de t�rminos
	
	-. Texto.py: extiende a la clase ProcesadorDeTexto, recibiendo los mismos par�metros. Sirve para obtener las palabras de textos que se comparar�n con un diccionario.
		Sus m�todos son:
			clean: "limpia" el texto y lo pasa a lowercase
			loadWords: guarda las palabras del texto en un arreglo
			getWords: devuelve la lista de palabras

	-. Funcionespy: conjunto de funciones para trabajar los textos.
		Los m�todos importantes son:
			binarySearchDicc: recibe un arreglo de palabras extra�das de un texto,
						 la posici�n de partida en dicho arreglo, 
						 un arreglo con t�rminos de un diccionario diccionario,
						 un arreglo para guardar los t�rminos encontrados,
						 una funci�n para comparar.
					guarda en una lista los terminos de un diccionario (en forma de arreglo) presentes en un texto (tambien como arreglo), por medio de un m�todo comparador partiendo desde una posici�n en el texto
			buscarCerca: Utilizada por binarySearchDicc, busca los t�rminos semejantes a los encontrados
			continuarRevisando: Utilizada por binarySearchDicc, sigue comparando las palabras siguientes en el texto para compararlas con un t�rmino de m�ltiples palabras
			normalizar: mediante reglas se reducen las palabras por medio de regex

	-. ComparadorDirecto.py: posee una clase para comparar directamente un Texto y un Diccionario. Recibe arreglo con t�rminos de diccionario y areglo con las palabras de un texto
		m�todos:
			coincidencias: guarda en una lista las coincidencias
			getMatches: devuelve las coincidencias ordenadas en forma de lista
    			nombre: retorna el nombre de la clase
    			getStemsText: devuelve el texto en forma de arreglo
			getStemsDict: devuelve el diccionario en forma de arreglo
		comparador: compara 2 strings con equals

	-. ComparadorStems.py: posee una clase para comparar por medio del Stemmer de NLTK un Texto y un Diccionario. Recibe arreglo con t�rminos de diccionario y areglo con las palabras de un texto
		m�todos:
			coincidencias: guarda en una lista las coincidencias
			getMatches: devuelve las coincidencias ordenadas en forma de lista
    			nombre: retorna el nombre de la clase
    			getStemsText: devuelve el texto procesado en forma de arreglo
			getStemsDict: devuelve el diccionario procesado en forma de arreglo
		comparador: compara 2 strings con equals
		stemArray: entrega la lista original con las palabras recortadas seg�n las reglas en el stemmer

	-. ComparadorCustomStems: posee una clase para comparar por medio de reglas personalizadas un Texto y un Diccionario. Recibe arreglo con t�rminos de diccionario y areglo con las palabras de un texto
		m�todos:
			coincidencias: guarda en una lista las coincidencias
			getMatches: devuelve las coincidencias ordenadas en forma de lista
    			nombre: retorna el nombre de la clase
    			getStemsText: devuelve el texto procesado en forma de arreglo
			getStemsDict: devuelve el diccionario procesado en forma de arreglo
		comparador: compara 2 strings con startswith
		stemArray: entrega la lista original con las palabras recortadas seg�n las reglas personalizadas

	-. DirectoryDict: posee una clase para procesar un directorio a trav�s de los 3 m�todos previamente definidos
		m�todos:
			procesar: procesa todos los archivos con los m�todos y los escribe en el destino especificado
				recibe los siguientes argumentos opcionales:
					out_stems: nombre opcional para subcarpeta que guarda los archivos con el m�todo de NLTK
    					out_custom: nombre opcional para subcarpeta que guarda los archivos con el m�todo de personalizado
    					out_directo: nombre opcional para subcarpeta que guarda los archivos con el m�todo directo
    

