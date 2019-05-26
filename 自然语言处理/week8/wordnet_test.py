from nltk.corpus import wordnet as wn

def _printSynset(word):
    wset = wn.synsets(word)
    print(word,':\n')
    i = 0
    for w in wset:
        i+=1
        print('\t',i,'. ',w)
        print('\tsynset:',w.lemma_names())
        print('\tdefinition:\t',w.definition())
        print('\texamples:\t',w.examples())
        print()
def printSynset():
    print('-------------------synset------------------------------------------')
    wordset = ['dog','apple','fly']
    for word in wordset:
        _printSynset(word)
def calculateSimilarity(w1,w2):
    wset = wn.synsets(w1)
    wset2 = wn.synsets(w2)
    max = 0.0
    for w in wset:
        for w2 in wset2:
            sim = w.path_similarity(w2)
            if(sim == None):
                continue
            if(sim > max):
                max = sim
    return max
def printSimilarity():
    print('----------------------------Similarity-----------------------------')
    wdcmp1=['good','beautiful']
    wdcmp2=['good','bad']
    wdcmp3=['dog','cat']
    print('similarity between good and beautiful:\t',calculateSimilarity(wdcmp1[0],wdcmp1[1]))
    print('similarity between good and bad:\t',calculateSimilarity(wdcmp2[0],wdcmp2[1]))
    print('similarity between dog and cat:\t',calculateSimilarity(wdcmp3[0],wdcmp3[1]))
def calculateEntailments(w):
    res = []
    wset = wn.synsets(w)
    for wd in wset:
        res.extend(wd.entailments())
    return res
def calculateReverse(w):
    res = []
    wset = wn.lemmas(w)
    for wd in wset:
        res.extend(wd.antonyms())
    return res

def printEntailmentAndReverse():
    print('-----------------------------Entailments and Reverse-----------------------')
    testwordset=['walk','supply','hot']
    for word in testwordset:
        print(word)
        print('entailments:\t',calculateEntailments(word))
        print('reverse:\t',calculateReverse(word))
        print()
def exercise1():
    printSynset()
    printSimilarity()
    printEntailmentAndReverse()


exercise1()
#synset1.path_similarity(synset2)
#wn.synset('car.n.01').lemma_names()

#wn.synset('car.n.01').definition()

#wn.synset('car.n.01').examples()