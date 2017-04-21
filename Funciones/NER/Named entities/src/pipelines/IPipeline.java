package pipelines;

import java.util.List;

import edu.stanford.nlp.util.CoreMap;

/**
 * 
 * Intefaz para el manejo de pipelines de CoreNLP.
 * 
 * @author Raul Rayo
 *
 */
public interface IPipeline {
	
	/**
	 * Carga el texto en el pipeline de CoreNLP.
	 */
	void loadText(String text);
	
	/**
	 * Devuelve una lista de sentencias para luego ser procesada.
	 * @return lista de sentencias.
	 */
	List<CoreMap> getSentences();
}
