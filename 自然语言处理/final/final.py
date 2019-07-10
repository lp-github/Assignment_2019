

embedding_dim = 300
emb_file = 'glove.6B.300d.txt'
polarity_dict = {'neutral': '0', 'negative': '1', 'positive': '2'}
polarity_dict_back = {value:key for key,value in polarity_dict.items()}

def load_glove(filename):
    print('Loading glove vector...')
    vocab = []
    emb = []
    vocab.append('unk') #装载不认识的词
    emb.append([0] * embedding_dim)
    with open(filename, mode='r', encoding='utf-8') as infile:
        for line in infile:
            row = line.strip().split(' ')
            vocab.append(row[0])
            emb.append(row[1:])
    return vocab, emb

# vocab, emb = load_glove(emb_file)
# print(len(vocab))

#数据集乱七八糟我cnm

import re
def get_target(sentence, index1, index2):
    words = sentence.split(' ')
    target = ''
    if int(index1) == int(index2):
        if int(index1) >= len(words):
            print(words)
        else:
            target = words[int(index1)]
    else:
        target = ''
        for i in range(int(index1), int(index2) + 1):
            target = target + ' ' + words[i]
    return target

#reading training data
print("reading training data start")
train_sentence = []
train_polarity = []
train_target = []

with open('sa_data/train.tsv') as infile:
    for line in infile:
        splits = line.split("\t")
        train_polarity.append(polarity_dict[splits[4]])
        train_sentence.append(splits[5][:-1])
        train_target.append(get_target(splits[5][:-1], splits[2], splits[3]))
print(len(train_polarity), len(train_sentence), len(train_target))

#reading test data
print("reading test data start")
test_linenum = []
test_sentence = []
test_target = []
with open('sa_data/test.tsv') as infile:
    for line in infile:
        splits = line.split("\t")
        test_linenum.append(splits[1])
        test_sentence.append(splits[5][:-1])
        test_target.append(get_target(splits[5][:-1], splits[2], splits[3]))
print(len(test_linenum), len(test_sentence), len(test_target))

import nltk
from nltk.corpus import stopwords
def clean_data(sentence):
    #review_text = BeautifulSoup(sentence, features = "html5lib").get_text()
    letters_only = re.sub('[^a-zA-Z]', ' ', sentence)
    words = nltk.word_tokenize(letters_only.lower())
    stops = set(stopwords.words('english'))
    meaningful_words = [w for w in words if w not in stops]
    return(" ".join(meaningful_words))

print("cleaning data start")
data_size = len(train_sentence)
clean_training_data = []
for i in range(0, data_size):
    clean_training_data.append(train_target[i] + " " + clean_data(train_sentence[i]))


#clean test data
print("cleaning test data start")
test_data_size = len(test_sentence)
clean_test_data = []
for i in range(0, test_data_size):
    clean_test_data.append(test_target[i] + " " + clean_data(test_sentence[i])) 

#creating bag of words
print('creating bag of words start')
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer = 'word', tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000)
train_data_features = vectorizer.fit_transform(clean_training_data)
train_data_features = train_data_features.toarray()

test_data_features = vectorizer.transform(clean_test_data)
test_data_features = test_data_features.toarray()

#training random forest
print('training random forest start')
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit(train_data_features, train_polarity)

#test
import pandas as pd
print('test start')
result = forest.predict(test_data_features)
output = pd.DataFrame(data = {'id': test_linenum, 'polarity': result})
output['polarity'] = output['polarity'].apply(lambda x: polarity_dict_back[x])
output.to_csv('Bag_of_Words_model.csv', index = False, quoting = 3)
