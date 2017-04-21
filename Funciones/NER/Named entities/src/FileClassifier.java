import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import edu.stanford.nlp.util.CoreMap;

import pipelines.IPipeline;

/**
 * 
 * Clase para procesar un archivo mediante un pipeline especifico.
 * 
 * @author "Raul Rayo"
 *
 */
public class FileClassifier {
	
	private IPipeline classifier;
	private InputStreamReader inFile;
	private BufferedReader br;
	
	private List<CoreMap> sentences;
	
	/**
	 * 
	 * @param path: path del archivo a procesar.
	 * @param pipe: pipeline con la que se proocesara el texto.
	 * @throws IOException
	 */
	public FileClassifier(String path, IPipeline pipe) throws IOException {
		classifier = pipe;
		sentences = new ArrayList<CoreMap>();
		try {
			inFile = new InputStreamReader(new FileInputStream(path), "UTF8");
			br = new BufferedReader(inFile);
			
		} catch (Exception e){
			e.printStackTrace();
		}
	}
	
	/**
	 * 
	 * Obtiene las sentencias a traves del pipeline y las guarda en una lista.
	 * 
	 * @throws IOException
	 */
	public void classify() throws IOException {
		String linea;
		while ((linea = br.readLine()) != null) {
			classifier.loadText(linea);
			sentences.addAll(classifier.getSentences()); //TODO eficiencia -> O(n)
		}
		br.close();
		inFile.close();
	}
	
	/**
	 * 
	 * @return: retorna la lista con las sentencias obtenidas previamente.
	 */
	public List<CoreMap> getSentences() {
		return sentences;
	}
	
}
