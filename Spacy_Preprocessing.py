###                             SPACY                            ###
import spacy
import os
folder = os.listdir(r'C:\Users\mridu\OneDrive\Documents\VMware\cloud_documentation')

##input must be a folder
def grab_doc_info(folder):
    j = 0 ##count documents in folder, 0...N
    nlp = spacy.load('en_core_web_lg') ## lg lets us use large documents
    tokens = [] ##store all tokens from all the documents
    pos = [] ##store all parts of speech for each token MUST CHECK if POS can't be labeled does it still output something... to make sure we map POS to each token that exists wihthin the documents
    dep = [] ##store dependnancy of each token MUST CHECK how dependnancy is found... is it token wise?
    sim = [] ##store similarity of each token MUST CHECK how similarity is found... is it toke wise?
    hasvector = [] ##store if token can be vectorized or not... using some sort of norm equation, i think it was the forbenuis equation that was mentioned in the documentation
    vectornorm = [] ##stores scalar values of vector norm... useful info
    isoov = [] ##if toke is out of vocabulary False if in vocabulary True, both being boolean values
    cloud_dict = {} ##dictionary to map each document, numbered numerically from 0...N, to their the respective characteristics of the document, listed above... within each of theses characteristic lists there are sublists whose position corresponds directly to the document number
    for efile in folder: ##go through each file in the folder
        with open(efile,'r') as f: ##setting file attribute which is to be utilized
            data = f.read() 
            doc = nlp(data) ##spacy function, tokenizes our document and makes it ready for us to process
            ###         DOCUMENT CHARACTERISTICS            ###
            new_token = [] ##           0
            new_pos = [] ##             1
            new_dep = []##              2
            new_sim = []##              3
            new_hasvector=[]##          4
            new_vectornorm=[]##         5
            new_isoov=[]##              6
            for tokens in doc:
                new_token = new_token.append(tokens.text)
                new_pos = new_pos.append(tokens.pos_)
                new_dep = new_dep.append(tokens.dep_)
                new_sim = new_sim.append(tokens.sim_)
                new_hasvector = new_hasvector.append(tokens.has_vector)
                new_vectornorm = new_vectornorm.append(tokens.vector_norm)
                new_isoov = new_isoov.append(tokens.is_oov)
            tokens = tokens.append(new_token)
            pos = pos[j].append(new_pos)
            dep = dep[j].append(new_dep)
            sim = sim[j].append(new_sim)
            hasvector = hasvector[j].append(new_hasvector)
            vectornorm = vectornorm[j].append(new_vectornorm)
            isoov = isoov[j].append(new_isoov)
            j = j + 1 ##counts once we have opened a new documents
    return cloud_dict