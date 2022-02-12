import spacy
from spacy import displacy

nlp = spacy.load("ja_core_news_sm")
doc = nlp("人生は短く、芸術は長い。")

for token in doc:
    print(token.text, token.pos_)

displacy.serve(doc, style="dep")