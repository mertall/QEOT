from nltk.parse import CoreNLPParser
import os
def parse_text():
    folder = os.listdir(r'C:\Users\mridu\OneDrive\Documents\VMware\cloud_documentation')
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
##need to update corenlp also access corenlp via java after running this
##cd ~
#wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
#unzip stanford-corenlp-full-2018-02-27.zip
#cd stanford-corenlp-full-2018-02-27
#then run 
#java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
#-preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
#-status_port 9000 -port 9000 -timeout 15000 & 
#then run parse text...
parse_text()
