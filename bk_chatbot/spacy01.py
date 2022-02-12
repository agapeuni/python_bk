import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Life is short and art is long')
for token in doc:
    print(token.text, token.pos_)

displacy.serve(doc, style="dep")