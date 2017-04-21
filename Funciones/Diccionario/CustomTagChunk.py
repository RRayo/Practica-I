from nltk.corpus import conll2002

from nltk.tag import UnigramTagger
from chunkers import ClassifierChunker

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.tree import Tree

from ProcesadorDeTexto import ProcesadorDeTexto

import sys
import pickle
import nltk
import os
import re


class TaggerEsp:
    def __init__(self,train_sents = conll2002.tagged_sents('esp.train')):
        #entrena al tagger
        sys.stderr.write('Training tagger...\n')
        self.tagger = UnigramTagger(train_sents)
        sys.stderr.write('Tagger ready.\n\n')
        
    def tag(self,text):
        return self.tagger.tag(text)

    def save(self,path_and_filename):
        f = open(path_and_filename,'wb')
        pickle.dump(self.tagger,f)
        f.close()

class ChunkerEsp:
    def __init__(self,train_chunks = conll2002.chunked_sents('esp.train')):
        #entrena al chunker        
        sys.stderr.write('Training chunker...\n')
        self.chunker = ClassifierChunker(train_chunks)
        sys.stderr.write('Chunker ready.\n\n')
        
    def parse(self,tagged_sents):
        return self.chunker.parse(tagged_sents)

    def save(self,path_and_filename):
        f = open(path_and_filename,'wb')
        pickle.dump(self.chunker,f)
        f.close()

class ParsedText(ProcesadorDeTexto):

    # n: name of file
    # p: path of file
    def __init__(self,n,p,parser_tools = []):
        super(ParsedText, self).__init__(n,p)
        super(ParsedText, self).loadText()
        if not parser_tools:
            self.tree = parsed_tree(self.text)
        elif len(parser_tools):
            self.tree = parsed_tree(self.text,parser_tools[0],parser_tools[1])

    def write_entities(self,file_path, file_name):
        file = open(file_path+file_name+".out", 'a')
        file.write('Named entities of file:\t'+file_name+'\n\n')
        file.write('PER tag:\n')
        write_nodes(self.tree,'PER',file)
        file.write('\n\nORG tag:\n')
        write_nodes(self.tree,'ORG',file)
        file.write('\n\nLOC tag:\n')
        write_nodes(self.tree,'LOC',file)
        file.close()

class DirectoryNer:

    def __init__(self,input_directory,output_directory):
        self.input = input_directory
        self.input_list = os.listdir(input_directory)
        self.output = output_directory

    def ner(self, parser_tools = []):
        for file in self.input_list:
            p = ParsedText(file,self.input,parser_tools)
            p.write_entities(self.output,file)


class CorpusAdapter(ProcesadorDeTexto):
    # n: name of file
    # p: path of file
    def __init__(self,n,p):
        super(CorpusAdapter, self).__init__(n,p)
        super(CorpusAdapter, self).loadText()
        self.text = re.sub(r"[\n]+","\n\n",self.text)
        self.text = re.sub(r" ","\n",self.text)
        self.text = re.sub(r"\|"," ",self.text)
        
        self.text = re.sub(r"^[\n]+","",self.text)
        

    def write(self,file_path, file_name):
        file = open(file_path+file_name+".out", 'w')
        file.write(self.text)
        file.close()




        

def saved_pickle(path):
    return pickle.load(open(path,'rb'))


def parsed_tree(text, tagger_path = 'trained_tools/my_tagger.pickle',
                chunker_path = 'trained_tools/my_chunker.pickle'):
    tagger = saved_pickle(tagger_path)
    chunker = saved_pickle(chunker_path)
    sents = sent_tokenize(text)
    
    for i in range(len(sents)):
        sents[i] = word_tokenize(sents[i])
        
    chunks =[]
    for i in range(len(sents)):
        t_s = tagger.tag(sents[i])
        chunks.append(chunker.parse(t_s))
    
    return Tree('T',chunks)


def getNodes(tree,label):
    for i in range(len(tree)):
        if type(tree[i]) is nltk.Tree:
            if tree[i].label() == label:
                print (extract_leaves(tree[i]),"\n")
            getNodes(tree[i],label)


def write_nodes(tree,label,file):
    for i in range(len(tree)):
        if type(tree[i]) is nltk.Tree:
            if tree[i].label() == label:
                file.write(extract_leaves(tree[i])+"\n")
            write_nodes(tree[i],label,file)

def extract_leaves(tree):
    s = ""
    for leave in tree.leaves():
        s = s + leave[0]+" "
        
    return s[:-1]


    

















