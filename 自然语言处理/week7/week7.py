

#algorithom define
#split=nltk.word_tokenize(str(info))

def execise1(positiveList,negtiveList):
    vocabulary = []
    wordsNum=0
    priorNeg = 0.0
    priorPos = 0.0
    likelihoodsPos={}
    likelihoodsNeg = {}

    #prior
    import nltk;
    priorPos=len(positiveList)*1.0/(len(positiveList)+len(negtiveList))
    priorNeg = 1- priorPos;

    #likelihoods
    tempdic={}
    negdic={}
    posdic={}
    posNum = 0
    negNum = 0
    for string in negtiveList:
        words = nltk.word_tokenize(string)
        for word in words:
            negNum +=1
            if(tempdic.get(word)==None):
                tempdic[word]=1
            if(negdic.get(word)==None):
                negdic[word]=1
            else:
                negdic[word]+=1

    for string in positiveList:
        words = nltk.word_tokenize(string)
        for word in words:
            posNum += 1
            if(tempdic.get(word)==None):
                tempdic[word]=1
            if(posdic.get(word)==None):
                posdic[word]=1
            else:
                posdic[word]+=1

    vocabulary = list(tempdic.keys())
    for word in vocabulary:
        numInPos = posdic.get(word,0)
        numInNeg = negdic.get(word,0)
        likelihoodsPos[word]=(numInPos+1)*1.0/(len(vocabulary)+posNum)
        likelihoodsNeg[word]=(numInNeg+1)*1.0/(len(vocabulary)+negNum)
    #print(likelihoodsNeg)
    #print(likelihoodsPos)
    #print(priorPos)
    return priorPos,priorNeg,likelihoodsPos,likelihoodsNeg

def execise2(priorPos,priorNeg,likelihoodsPos,likelihoodsNeg,testCase):
    import nltk
    testwords = nltk.word_tokenize(testCase)
    proPos=priorPos
    proNeg = priorNeg
    for word in testwords:
        proPos *= likelihoodsPos.get(word,1.0)
        proNeg *= likelihoodsNeg.get(word,1.0)
    #print(priorPos)
    #print("positive probability:",proPos)
    #print("negtive probability:",proNeg)
    return proPos,proNeg
def main():
    # data define
    negtiveList = ["just plain boring","entirely predictable and lacks energy",
                        "no surprises and very few laughs"]
    positiveList = ["very powerful","the most fun film of the summer"]

    testCase = "predictable with no originality"
    priorPos,priorNeg,likelihoodsPos,likelihoodsNeg = execise1(positiveList,negtiveList)
    proPos,proNeg = execise2(priorPos,priorNeg,likelihoodsPos,likelihoodsNeg,testCase)
    print("prior probability:")
    print("\tpositive:\t",priorPos)
    print("\tnegtive:\t",priorNeg)
    print("\n\n\nlikelihoods of positive:\n")
    print(likelihoodsPos)
    print("\nlikelihoods of negtive:\n")
    print(likelihoodsNeg)
    print("\n\n\n")
    print("probability of positive:\t",proPos)
    print("probability of negtive :\t",proNeg)

main()