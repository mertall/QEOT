import spacy
nlp = spacy.load('en_core_web_lg') ## lg lets us use large documents

def understandability(cloud_dict): 
    iter = len(cloud_dict)
    counter = 0
    score =[]
    for i in range(iter):
        doc = cloud_dict[iter]
        num_tokens = len(cloud_dict)
        for j in range(num_tokens):
            isoov = doc[6]
            if isoov[j] == 1:
                counter += 1
            else:
                pass
        score[i] = counter/num_tokens
    return score