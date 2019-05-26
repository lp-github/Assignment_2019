import nltk
import string
import re
import sysconfig

f = open("C:/Users/Administrator/Desktop/text_en.txt",'r',1,"utf-8")
info = f.read()
#$print(info)
f.close()


####################split & stem##################
fw=open("C:/Users/Administrator/Desktop/split.txt","w",1,"utf-8")
split=nltk.word_tokenize(str(info))
#print(split)
for i in split:
    fw.write(str(i)+' ')
fw.close()

fw=open("C:/Users/Administrator/Desktop/stem.txt","w",1,"utf-8")
from nltk.stem import LancasterStemmer
stemmereporter=LancasterStemmer()
stem=[]
for i in split:
    stem.append(stemmereporter.stem(i))
    fw.write(stem[-1]+' ')
#print(stem)
fw.close()

##################stop words########################
fstop=open("C:/Users/Administrator/Desktop/stopwords.txt","w",1,"utf-8")
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
words=stem
words = [word for word in words if word.lower() not in stops]
#print(words)
for i in words:
    fstop.write(i+' ')
fstop.close()

################punctuation########################
fpunct=open("C:/Users/Administrator/Desktop/punctuation.txt","w",1,"utf-8")
new_words=[]
illegal_char=string.punctuation+'【·！…（）—：“”？《》、；】'
pattern = re.compile('[%s]'%re.escape(illegal_char))
for word in words:
    new_word = pattern.sub(u'', word)
    if not new_word ==u'':
        new_words.append(new_word)
        fpunct.write(new_word+' ')
#print(new_words)
fpunct.close()

################threshold filtering##################
fthreshold=open("C:/Users/Administrator/Desktop/threshold.txt","w",1,"utf-8")
n = 20
punct=new_words
from nltk.probability import FreqDist
fdist=FreqDist(punct)

thresholdwords=[]
for word in punct:
        if fdist[word]>=n:
                thresholdwords.append(word)
                fthreshold.write(word+' ')
#print(thresholdwords)
fthreshold.close()

##################discrete plot##########

from nltk.text import Text
moby = Text(split)
tocheck=['Elizabeth', 'Darcy','Wickham', 'Bingley', 'Jane']
#moby.dispersion_plot(tocheck)

##############frequency distribution graph#######
fdist.plot(20)
