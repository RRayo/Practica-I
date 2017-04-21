import java.io.File;
import java.io.IOException;

import pipelines.IPipeline;
import pipelines.SimpleNer;

/**
 * 
 * Clase para obtener las entidades con nombre de todo un directorio (con archivos en ingles).
 * 
 * @author "Raul Rayo"
 *
 */
public class DirectoryNerEnglish {
	private IPipeline ner;
	private FileClassifier f;
	private NerWriter nerWriter;
	
	/**
	 * 
	 * @param inPath: Ruta de la carpeta con los archivos en ingles.
	 * @param outPath: Ruta donde se almacenaran los archivos procesados.
	 * @throws IOException
	 */
	DirectoryNerEnglish(String inPath, String outPath) throws IOException {
		 ner = new SimpleNer();
		 File folder = new File(inPath);
		 File[] listOfFiles = folder.listFiles();
		 for (File file : listOfFiles) {
			 if ( ! file.isDirectory()) {
				 String name = file.getName();
				 if (name.endsWith(".txt")) {
					 f = new FileClassifier(inPath+name, ner);
					 f.classify();
					 nerWriter = new NerWriter(f.getSentences(),outPath + name);
					 nerWriter.write();
				 }
			 }
		 }
	}
	
	/**
	 * Main con ejemplo de como utilizar la clase.
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		String inPath = "C:\\Users\\Rayo1115\\Desktop\\Document classification\\Test archivos NER\\raw data - traducida\\";
		String outPath = "C:\\Users\\Rayo1115\\Desktop\\Document classification\\Test archivos NER\\a\\";
		new DirectoryNerEnglish(inPath, outPath);
	}
}
