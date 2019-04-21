import spacy
nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)
sen1='My sister has a dog. She loves him.'
sen2 = 'Some like to play football, others are fond of basketball.'
sen3 = 'The more a man knows, the more he feels his ignorance.'
sens=[sen1,sen2,sen3]
for sen in sens:
    doc = nlp(sen)
    print(doc._.has_coref)
    print(doc._.coref_clusters)
    print(doc._.coref_resolved)
