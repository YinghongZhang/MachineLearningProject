import prepocess
import vectorizer
import extract_changed
from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

data = prepocess.readplz()
x,y=prepocess.get(data)
#kf = KFold(n_splits=10)
m = LogisticRegression()
m = m.fit(x,y)
print(m.score(x,y))

#·····memory exploded·····
#avg_train_score=0
#avg_test_score=0
#for train,test in kf.split(x):
    #x_train,x_test,y_train,y_test = x[train],x[test],y[train],y[test]
    #model = MultinomialNB()
    #test = model.fit(x_train,y_train)
    #avg_train_score+=test.score(x_train,y_train)
    #avg_test_score+=test.score(x_test,y_test)
    #print(test.score(x_train,y_train))
    #print(test.score(x_test,y_test))
    #print('----------')
#print(avg_train_score/10)
#print(avg_test_score/10)


