Instrucciones para la utilizaci�n de las herramientas para extraer entidades con nombre de textos

Las siguientes instrucciones son para el manejo de los m�todos escritos en Python con el fin de obtener las entidades de archivos

La versi�n de Python utilizada es la 3.5.2, debido a las restricciones del instalador del toolkit.

El toolkit en cuesti�n es NLTK 3.0, que se puede encontrar en: http://www.nltk.org/install.html

Se debe descargar los corpus de NLTK por medio de: import nltk -> nltk.download() y descargar todo.

Archivos:

	Los archivos tag_util.py y chunkers.py fueron extra�dos del libro: "Python 3 Text Processing with Nltk 3 Cookbook"

	-. Ner.py: ejemplo b�sico del funcionamiento del NER.

	-. Training_tester.py: ejemplos de entrenamiento y test de taggers y chunkers.

	-. ProcesadorDeTexto.py: posee la clase del mismo nombre, encargada de guardar el nombre de un archivo y su ruta.
		Sus m�todos son:
			loadText: carga el texto y lo guarda.
			getText: retorna el texto guardado
	
	-. CustomTagChunk.py: archivo principal con la mayor parte de las funciones.
		clase TaggerEsp: entrena un tagger con un corpus adaptado para poder procesarlo. Recibe las sentencias con tags extra�das del corpus esp.train (por defecto)
				tag: que retorna los tags de un texto dado
				save: guarda el tagger en un directorio

		clase ChunkerEsp: entrega un chunker desde un corpus con formato apropiado. Recibe las sentencias con chunks extra�das del corpus esp.train (por defecto)
				parse: retorna el parse tree de sentencias taggeadas
				save: guarda el chunker en un directorio

		clase ParsedText: escribe entidades en un archivo a partir de un archivo dado. Recibe el nombre del archivo y su directorio
				write_entities: escribe las entidades con tags relevantes en el archivo

		clase DirectoryNer: procesa un directorio usando ParsedText. Recibe el directorio con los archivos a procesar y el lugar donde se guardar�n los archivos.
				ner: procesa cada archivo a trav�s de ParsedText

		clase CorpusAdapter: adapta los corpus extra�dos de wikipedia para su uso por NLTK
				write: escribe los archivos procesados en el lugar especficado

		m�todo saved_pickle: carga un clasificador previamente guardado. Recibe el lugar del clasificador

		m�todo parsed_tree: carga los clasificadores, procesa el texto, entrega el arbol de derivacion. Recibe el lugar donde se encuentran el tagger y chunker entrenados
		
		m�todo getNodes: imprime los nodos desde un �rbol con la etiqueta especificada. Recibe el �rbol y la etiqueta por extraer

		m�todo write_nodes: escribe los nodos desde un �rbol con la etiqueta especificada. Recibe el �rbol y la etiqueta por extraer

		m�todo extract_leaves: obtiene las hojas desde un �rbol y las transforma en texto plano