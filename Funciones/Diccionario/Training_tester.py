from nltk.corpus import conll2002

from nltk.tag import UnigramTagger
from chunkers import TagChunker
from chunkers import ClassifierChunker

#entrenar tagger
train_sents = conll2002.tagged_sents('esp.train')
tagger = UnigramTagger(train_sents)

#ntrenar chunkers (el segundo es mucho mejor)
chunker_1 = TagChunker(train_chunks)
score_1_a = chunker_1.evaluate(test_chunks_a)
score_1_b = chunker_1.evaluate(test_chunks_b)

chunker_2 = ClassifierChunker(train_chunks)
score_2_a = chunker_2.evaluate(test_chunks_a)
score_2_b = chunker_2.evaluate(test_chunks_b)































