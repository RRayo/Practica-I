# -*- coding: utf-8 -*-

#n: file name
#p: path of the file
class ProcesadorDeTexto:
    def __init__(self,n,p):
        assert type(n)==str
        assert type(p)==str
        self.__name=n
        self.__path=p
        self.text=""

    #save the text in the file in a string
    def loadText(self):
        with open(self.__path+self.__name,"r") as archivo:
            self.text = archivo.read()

    def getText(self):
        return self.text

