Intrucciones para la utilizaci�n de Named Entities Recognizer

Las siguientes instrucciones son para el manejo de las clases escritas en Java con el fin de extraer las entidades con nombres de los textos.
La versi�n de Java utilizada es la versi�n 8.

Primero se debe agregar al proyecto el los siguientes .jar:
	- stanford-corenlp-3.7.0-javadoc.jar
	- stanford-corenlp-3.7.0-models.jar
	- stanford-corenlp-3.7.0-sources.jar
	- stanford-corenlp-3.7.0.jar
	- stanford-spanish-corenlp-2016-10-31-models.jar
	- xom.jar

Los cuales se encuentran en el siguiente link: http://stanfordnlp.github.io/CoreNLP/download.html

-. Pipelines
	
	Son las clases encargadas de definir los analizadores de texto encargados de clasificar este.
	Se encuentran en el paquete "pipelines", donde se implementan por medio de una interfaz, contando con 2 pipes principales.
		
	1.- SimpleNer: Esta configurada con los anotadores para obtener las entidades en ingl�s.
	2.- SimpleSpanishNer: Esta configurada con los anotadores para obtener las entidades en espa�ol.

Clases:

	- FileClassifier: Recibe la ruta a el archivo a procesar y el pipe con el que se quiere trabajar.
		Posee 2 m�todos:
			classify: clasifica el archivo
			getSentences: retorna las sentencias
	
	- NerWriter: Recibe las sentencias (obtenidas desde FileClassifier) y la ruta donde escribir el archivo procesado.
		Posee 1 m�todo:
			write: escribe el archivo de salida con la informaci�n procesada.
		Nota: escribe solo aquellas palabras que est�n clasificadas como entidad. Si se desea obtener todas las palabras utilizar CompleteWriter, cuya funcionalidad es la misma.

	- DirectoryNerSpanish: Recibe la ruta de la carpeta que contiene los archivos a procesar y la ruta donde guardar los resultados.
		Trabaja con archivos en espa�ol.
		Basta con crear una nueva clase con dichos par�metros (ver main de la clase).

	- DirectoryNerEnglish: Recibe la ruta de la carpeta que contiene los archivos a procesar y la ruta donde guardar los resultados.
		Trabaja con archivos en ingl�s.
		Basta con crear una nueva clase con dichos par�metros (ver main de la clase).

	- XmlCleaner: Posee m�todos para limpiar archivos en formato XML, as� como carpetas con archivos en dicho formato.
		Ver el main para mayor detalles.

	