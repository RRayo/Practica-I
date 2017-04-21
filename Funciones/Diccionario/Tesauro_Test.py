# -*- coding: utf-8 -*-

from Diccionario import Diccionario
from Texto import Texto
from ComparadorStems import ComparadorStems
from ComparadorCustomStems import ComparadorCustomStems
from ComparadorDirecto import ComparadorDirecto

import os

class DirectoryDict:

    def __init__(self,diccFile,diccPath,input_directory,output_directory):
        self.input = input_directory
        self.dicc = Diccionario(diccFile, diccPath)
        self.dicc.loadText()
        self.dicc.clean()
        self.dicc.loadWords()
        self.dicc_words = self.dicc.getWords()
        self.input_list = os.listdir(input_directory)
        self.output = output_directory
        
    def procesar(self, out_stems="", out_custom="", out_directo=""):
        for file in self.input_list:
            t = Texto(file, self.input)
            t.loadText()
            t.clean()
            t.loadWords()
            
            compStems = ComparadorStems(self.dicc.getWords(), t.getWords())
            compStems.coincidencias()
            f1 = open(self.output+out_stems+file+".stems", 'a')
            for i in compStems.getMatches():
                f1.write(self.dicc_words[i]+'\n')
            f1.close()

            compStemsCustom = ComparadorCustomStems(self.dicc.getWords(), t.getWords())
            compStemsCustom.coincidencias()
            f2 = open(self.output+out_custom+file+".customstems", 'a')
            for i in compStemsCustom.getMatches():
                f2.write(self.dicc_words[i]+'\n')
            f2.close()
            

            compDirecto = ComparadorDirecto(self.dicc.getWords(), t.getWords())
            compDirecto.coincidencias()
            f3 = open(self.output+out_directo+file+".directo", 'a')
            for i in compDirecto.getMatches():
                f3.write(self.dicc_words[i]+'\n')
            f3.close()



diccPath =  r'C:\\Users\\Rayo1115\\Desktop\\Document classification\\AGROVOC - tesauro\\'
diccFile = 'MERGE.txt'

textPath =  r'C:\\Users\\Rayo1115\\Desktop\\Document classification\\raw data\\OPIA\\'
textFile = '3.txt'


opia_path = "C:/Users/Rayo1115/Desktop/Document classification/OPIA raw data/Selected/"
out_path = "C:/Users/Rayo1115/Desktop/Document classification/Test diccionarios OPIA/"


d = DirectoryDict(diccFile,diccPath,opia_path,out_path)
d.procesar("stems/","custom/","directo/")












