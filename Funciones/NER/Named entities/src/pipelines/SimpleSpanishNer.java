package pipelines;
import java.util.List;

import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations.NamedEntityTagAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.PartOfSpeechAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TextAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;
import edu.stanford.nlp.util.PropertiesUtils;

/**
 * 
 * Clase para el uso del pipeline configurado para extraer las entidades con nombre de archivos en español.
 * 
 * @author "Raul Rayo"
 *
 */
public class SimpleSpanishNer extends AbstractPipeline{
	
	/**
	 * Configura las propiedades del pipeline con POS tags, lematizacion y NER.
	 */
	public SimpleSpanishNer() {		
		pipeline = new StanfordCoreNLP(
        		PropertiesUtils.asProperties(
        				"annotators", "tokenize,ssplit,pos,ner",
        				"pos.model", "edu/stanford/nlp/models/pos-tagger/spanish/spanish-distsim.tagger",
        				"ner.model", "edu/stanford/nlp/models/ner/spanish.ancora.distsim.s512.crf.ser.gz",
        				"ner.applyNumericClassifiers", "false",
        				"ner.useSUTime", "false",
        				"tokenize.language", "es")        		
        		);
	}
	
	/**
	 * main para ejemplificar las acciones de este pipe.
	 * @param args
	 */
	public static void main(String[] args) {
		
		SimpleSpanishNer pipeline = new SimpleSpanishNer();        

        // read some text in the text variable
        String text = "un árbol en América en una fotografía cantó música";


        // run all Annotators on this text
        pipeline.loadText(text);
        
	    // these are all the sentences in this document
	    // a CoreMap is essentially a Map that uses class objects as keys and has values with custom types
	    List<CoreMap> sentences = pipeline.getSentences();
	
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
	    		if ( ! ner.equals("O")){
		    		System.out.println(word);
		    		System.out.println(pos);
		    		System.out.println(ner);
	    		}
	    	}
	    }
        

	}

}
