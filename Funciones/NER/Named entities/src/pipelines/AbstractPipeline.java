package pipelines;

import java.util.List;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;

/**
 * 
 * Clase abstracta para facilitar el manejo de pipes.
 * 
 * @author Raul Rayo
 *
 */
public abstract class AbstractPipeline implements IPipeline {
	
	protected StanfordCoreNLP pipeline;
	protected Annotation document;
	protected List<CoreMap> sentences;
	
	/**
	 * Carga el texto en el pipeline de CoreNLP.
	 */
	public void loadText(String texto) {
		document = new Annotation(texto);
        pipeline.annotate(document);
		sentences = document.get(SentencesAnnotation.class);
	}
	
	/**
	 * Devuelve una lista de sentencias para luego ser procesada.
	 * @return lista de sentencias.
	 */
	public List<CoreMap> getSentences() {
		return sentences;
	}


}
