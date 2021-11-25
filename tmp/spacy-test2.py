# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_trf")

# Process whole documents
# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")

texts = [
    "time", "get time", "what time is it", "what is the time", "what time is it at the moment", "what time is it now", "what time is it today?",
]


for text in texts:
    # process text
    print("Text: '" + text + "'")
    doc = nlp(text)

    # Analyze syntax
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        print(entity.text, entity.label_)
    
    print()