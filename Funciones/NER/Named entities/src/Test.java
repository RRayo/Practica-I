import java.io.IOException;

import pipelines.IPipeline;
import pipelines.SimpleSpanishNer;

/**
 * 
 * Test general para el funcionamiento de CoreNLP.
 * 
 * @author "Raul Rayo"
 *
 */
public class Test {
	public static void main(String[] args) throws IOException {
		String root = "C:\\Users\\Rayo1115\\Desktop\\Document classification\\";
		String outPath = "C:\\Users\\Rayo1115\\Desktop\\Document classification\\";
		IPipeline ner = new SimpleSpanishNer();
		FileClassifier f = new FileClassifier(root+"Ideas.txt", ner);
		f.classify();
		NerWriter nerWriter = new NerWriter(f.getSentences(), root+"Ideas.ner");
		nerWriter.write();
		new DirectoryNerSpanish(root, outPath);
	}

}
