import extract
import helper
import vectorizer
from sklearn.naive_bayes import MultinomialNB

def readplz():
    return helper.read_data('./asset/training_data.txt')

def get(training_data):
    mid = list(map(extract.extract_train,training_data))
    feature,label = depart(mid)
    feature = vectorizer.vectorize(feature)
    label = vectorizer.label(label)
    return feature,label


def cut_train_file(training_data,start,end):   #cut off part of training_data
    x,y = get(training_data)
    return x[start:end],y[start:end]


def feedtest(x,y):
    nb = MultinomialNB(alpha=1)
    nb.fit(x,y)
    nb.score(x,y)