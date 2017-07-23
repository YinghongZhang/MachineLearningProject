from pkg import preprocess
from pkg import vectorizer
from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import time
from sklearn.metrics import f1_score

start = time.clock()
data = preprocess.readplz()
x,y=preprocess.get(data)
#kf = KFold(n_splits=10)
m = RandomForestClassifier()
m = m.fit(x,y)
predict_y = m.predict(x)
# print(m.score(x,y))
print('f1-score:')
print(f1_score(y,predict_y, average='weighted'))

elapsed = (time.clock() - start)
print("Time used:", elapsed)

'''
·····memory exploded·····
avg_train_score=0
avg_test_score=0
for train,test in kf.split(x):
    x_train,x_test,y_train,y_test = x[train],x[test],y[train],y[test]
    model = MultinomialNB()
    test = model.fit(x_train,y_train)
    avg_train_score+=test.score(x_train,y_train)
    avg_test_score+=test.score(x_test,y_test)
    print(test.score(x_train,y_train))
    print(test.score(x_test,y_test))
    print('----------')
print(avg_train_score/10)
print(avg_test_score/10)
'''


