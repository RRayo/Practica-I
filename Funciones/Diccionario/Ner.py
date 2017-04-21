# -*- coding: utf-8 -*-

import re
from ProcesadorDeTexto import ProcesadorDeTexto
import nltk_trainer
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.chunk.util import tree2conlltags, conlltags2tree

### Archivo de prueba donde se ejemplifica el proceso para obtener el NER ###
# trabaja con corpus procesado cess_esp y conll2002

# procesar: transforma de texto -> tokens -> tags -> chunks -> parsed tree
#           y lo imprime

# escribir: escribe las entidades en un archivo si son relevantes (!= 'O')

#n: file name
#p: path of the file
class Ner(ProcesadorDeTexto):
    def __init__(self,n,p):
        super(Ner, self).__init__(n,p)
        self.__tree = []

    def procesar(self):
        tokens = tokenize(self.text)
        tags = tag(tokens)
        chunks = chunk(tags)
        self.__tree = tree2conlltags(chunks)
        print(self.__tree)

    def escribir(self, path):
        with open(path, "w") as archivo:
            for tupla in self.__tree:
                if not tupla[2] == 'O':
                    archivo.write(tupla[0]+'\t'+tupla[2]+'\n')
    

def tokenize(texto):
    return word_tokenize(texto)

def tag(lista):
    tagger = nltk.data.load("taggers/cess_esp_aubt.pickle")
    return tagger.tag(lista)

def chunk(tags):
    #chunker = nltk.data.load("chunkers/conll2002_ub.pickle")
    chunker = nltk.data.load("chunkers/conll2002_NaiveBayes.pickle")
    return chunker.parse(tags)

'''
textPath =  r'C:\\Users\\Rayo1115\\Desktop\\Document classification\\Test archivos NER\\raw data\\'
textFile = '14014.data.txt'

textPath2 =  r'C:\\Users\\Rayo1115\\Desktop\\Document classification\\raw data\\OPIA\\'
textFile2 = '3.txt'

textPath3 =  r'C:\\Users\\Rayo1115\\Desktop\\'
textFile3 = 'ejemplo.txt'

outputPath =  r'C:\\Users\\Rayo1115\\Desktop\\'
outputFile = 'test.txt'

ner = Ner(textFile3, textPath3)
ner.loadText()
print(ner.getText())

ner.procesar()

ner.escribir(outputPath+outputFile)
'''
















