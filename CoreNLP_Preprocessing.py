###                             CORENLP                          ###
#from nltk.parse import CoreNLPParser
#import os
#need 7zip java python Stanford Core NLP

##      COMMAND LINE    ##
##cd ~
#python -m wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
#7z e stanford-corenlp-full-2018-02-27.zip
#cd stanford-corenlp-full-2018-02-27
#Then run 
#java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \-preload tokenize,ssplit,pos,lemma,ner,parse,depparse \-status_port 9000 -port 9000 -timeout 15000 
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
parse_text()

#Cannot conect to stanford server for some reason... lets utilize spacy then...  I think its because I am using UNIX based station... utilizing linux terminal should let us use the code above!
