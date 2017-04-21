package pipelines;
import java.util.List;
import java.util.Properties;

import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations.NamedEntityTagAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.PartOfSpeechAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TextAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;

/**
 * 
 * Clase para el uso del pipeline configurado para extraer las entidades con nombre de archivos en ingles.
 * 
 * @author "Raul Rayo"
 *
 */
public class SimpleNer extends AbstractPipeline{
	
	private Properties props;
	
	/**
	 * Configura las propiedades del pipeline con POS tags, lematizacion y NER.
	 */
	public SimpleNer() {		
		props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, pos, lemma, ner");
		props.setProperty("ner.model", "edu/stanford/nlp/models/ner/english.muc.7class.distsim.crf.ser.gz");
		pipeline = new StanfordCoreNLP(props);
	}
	
	/**
	 * main para ejemplificar las acciones de este pipe.
	 * @param args
	 */
	public static void main(String[] args) {
		
		// creates a StanfordCoreNLP object, with POS tagging, lemmatization, NER, parsing, and coreference resolution
        Properties props = new Properties();
        props.setProperty("annotators", "tokenize, ssplit, pos, lemma, ner");
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        // read some text in the text variable
        String text = "hola mundo";

        // create an empty Annotation just with the given text
        Annotation document = new Annotation(text);

        // run all Annotators on this text
        pipeline.annotate(document);
        
	    // these are all the sentences in this document
	    // a CoreMap is essentially a Map that uses class objects as keys and has values with custom types
	    List<CoreMap> sentences = document.get(SentencesAnnotation.class);
	
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
	    		
	    		System.out.println(word);
	    		System.out.println(pos);
	    		System.out.println(ner);
	    	}
	    }
        

	}

}
