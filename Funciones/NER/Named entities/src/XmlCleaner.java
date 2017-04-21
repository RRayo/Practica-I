import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


/**
 * 
 * Clase para "limpiar" archivos en formato Xml.
 * 
 * @author "Raul Rayo"
 *
 */
public class XmlCleaner {
	private static String REGEX = "<[^>]*>";
	private static String REPLACE = "";
	
	/**
	 * 
	 * Metodo para escribir un nuevo archivo sin la estructura original de Xml.
	 * 
	 * @param inPath: input path del archivo.
	 * @param outPath: output path para el resultado.
	 * @param file: nombre del archivo.
	 * @param extension: extensión del archivo.
	 * @throws IOException
	 */
	private static void cleaner(String inPath,String outPath, String file, String extension) throws IOException {
		Pattern p = Pattern.compile(REGEX);
		
		FileReader in = null;
	    FileWriter out = null;
	    try {
	    	in = new FileReader(inPath);
			BufferedReader br = new BufferedReader(in);			
	    	out = new FileWriter(outPath+file+extension);
	    	String linea, output;
			while ((linea = br.readLine()) != null) {
				Matcher m = p.matcher(linea);
				output = m.replaceAll(REPLACE);
	    		out.write(output);
	    		out.write(System.lineSeparator());
	    	}
			br.close();
	    }finally {
	    	if (in != null) {
	    		in.close();
	    	}
	    	if (out != null) {
	    		out.close();
	    	}
	    }
	}
	
	/**
	 * 
	 * Metodo para limpiar un directorio completo con archivos en Xml.
	 * 
	 * @param folder: carpeta contenedora de los archivos.
	 * @param outputDir: directorio de destino para los archivos procesados.
	 * @throws IOException
	 */
	public static void cleanDir(File folder, String outputDir) throws IOException {
		for (final File fileEntry : folder.listFiles()) {
	        if (fileEntry.isDirectory()) {
	        	cleanDir(fileEntry, outputDir);
	        } else {
	            cleaner(fileEntry.getAbsolutePath(), outputDir, fileEntry.getName(), ".txt");
	        }
	    }
	}
	
	/**
	 * 
	 * main para ejemplificar el uso de la clase en un directorio.
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		String inDir = "C:\\Users\\Rayo1115\\Desktop\\Document classification\\tar suseso\\";
		String outDir = "C:\\Users\\Rayo1115\\Desktop\\Nueva carpeta\\";
		final File folder = new File(inDir);
		cleanDir(folder, outDir);
	}
}
