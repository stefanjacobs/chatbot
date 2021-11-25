# import spacy
import spacy

# https://explosion.ai/demos/displacy

# load english language model
nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

text = "This is a sample sentence."

# create spacy 
doc = nlp(text)
for token in doc:
    print(token.text,'->',token.pos_)
from pathlib import Path

html = spacy.displacy.render(doc, style='dep', page=True)
output_path = Path(text + ".html")
output_path.open("w", encoding="utf-8").write(html)


texts = [
    "time", "get time", "what time is it", "what is the time", "what time is it at the moment", "what time is it now", "what time is it today?",
]
for text in texts:
    print("Text: '" + text + "'")
    # create spacy 
    doc = nlp(text)
    for token in doc:
        print(token.text,'->',token.pos_)
        if token.dep_ == 'nsubj':
            print("---> Subject: " + token.text)
        if token.dep_ == 'dobj':
            print("---> Object: " + token.text)
    
    html = spacy.displacy.render(doc, style='dep', page=True)
    output_path = Path(text + ".html")
    output_path.open("w", encoding="utf-8").write(html)
    print()