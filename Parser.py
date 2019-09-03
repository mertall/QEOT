#from nltk.parse import CoreNLPParser
#import os
#need 7zip java python Stanford Core NLP
##cd ~
#python -m wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
#7z e stanford-corenlp-full-2018-02-27.zip
#cd stanford-corenlp-full-2018-02-27
#then run 
#java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
#-preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
#-status_port 9000 -port 9000 -timeout 15000 
def parse_text_stanford():
    folder = os.listdir(r'C:\Users\mridu\OneDrive\Documents\PythonScripts\VMware\QEOT\cloud_documentation')
    for efile in folder :
        with open(efile) as f :
            data = f.read()
            parser = CoreNLPParser(url='http://localhost:9000')
            pos_tagger = CoreNLPParser(url='http://localhost:9000', tagetype='pos')
            ner_tagger = CoreNLPParser(url='http://localhost:9000', tagtype = 'ner')
            tokens = parser.tokenize(data)
            pos = pos_tagger.tag(data)
            ner = ner_tagger.tag(data)
            print(tokens)
            print(pos)
            print(ner)
#parse_text()

#Cannot conect to stanford server for some reason... lets utilize spacy then

import spacy
import os
folder = os.listdir(r'C:\Users\mridu\OneDrive\Documents\VMware\cloud_documentation')
nlp = spacy.load('en_core_web_lg')

for efile in folder:
    with open(efile,'r') as f:
        data = f.read()
        print(len(data))
        doc = nlp(data)
        tokens = []
        pos = []
        dep = []
        sim = []
        hasvector = []
        vectornorm = []
        isoov = []
        for token in doc:
            tokens = token.append(token.text)
            pos = pos.append(toke.pos_)
            dep = dep.append(token.dep_)
            hasvector = hasvector.append(token.has_vector)
            vectornorm = vectornorm.append(token.vector_norm)
            isoov = isoov.append(token.is_oov)
        cloud_dict = {}
        i = 1
        cloud_dict[i] = [tokens,pos,dep,hasvector,vectornorm,isoov]
        i = i + 1

##NEXT step find similarity between docs
i = 1
j = 2
for doc1 in cloud_dict[i].:
    for doc2 in cloud_dict[j]
        sim = sim.append(token)




##LENGHT OF DOC IS TOO LONG< FIND HOW OT SHORTREN DOCS OR INCREASE INPUT SIZE
