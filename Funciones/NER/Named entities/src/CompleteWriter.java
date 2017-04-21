import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations.NamedEntityTagAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.PartOfSpeechAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TextAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.util.CoreMap;

/**
 * 
 * Recibe las sentencias obtenidas desde FileClassifier y escribe las palabras y sus tags en un nuevo archivo.
 * 
 * @author "Raul Rayo"
 *
 */
public class CompleteWriter {
	
	private List<CoreMap> sentences;
	FileWriter outFile;
	
	/**
	 * 
	 * @param sentences: Sentencias obtenidas con FileClassifier.
	 * @param path: Ruta para el archivo que se creara.
	 * @throws IOException
	 */
	CompleteWriter(List<CoreMap> sentences, String path) throws IOException {
		this.sentences = sentences;
		outFile = new FileWriter(path);
	}
	
	/**
	 * Escribe las palabras con sus tags en el archivo.
	 * @throws IOException
	 */
	public void write() throws IOException {
		try {
			for(CoreMap sentence: sentences) {
		    	// traversing the words in the current sentence
		    	// a CoreLabel is a CoreMap with additional token-specific methods
		    	for (CoreLabel token: sentence.get(TokensAnnotation.class)) {
		    		// this is the text of the token
		    		String word = token.get(TextAnnotation.class);
		    		// this is the POS tag of the token
		    		String pos = token.get(PartOfSpeechAnnotation.class);
		    		// this is the NER label of the token
		    		String ner = token.get(NamedEntityTagAnnotation.class);
		    		
		    		outFile.write(word);
		    		outFile.write(" ");
		    		outFile.write(pos);
		    		outFile.write(" ");
		    		outFile.write(ner);
		    		outFile.write(System.lineSeparator());
		    	}
		    }
		} catch (Exception e){
			e.printStackTrace();
		} finally {
			if (outFile != null) {
				outFile.close();
			}
		}
	}
	
}
