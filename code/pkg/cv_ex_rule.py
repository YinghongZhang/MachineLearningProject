'''
这份代码加了测试代码，输出的结果的规则测试和正确结果的f1score
重点：这些函数只返回 True 或 False

总共有5种情况：
末音节、倒数第二音节、倒数第三音节、第一音节、第二音节
所以有五个函数，这五个函数，从上到下，优先级下降
所以，前面一个函数判断Ture，后面就不用判断了
但是，具体这些规则判断效果怎么样，还要去试验一下
毕竟这些规则，还是大多数情况下正确，具体正确率到多少，还是不清楚的
'''

import helper
import extract_changed
import vectorizer
from sklearn.metrics import f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
import pickle
import submission
import preprocess
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier

#判断末音节重音
def ultima(word):
    TAILS = ['EER', 'FIRM', 'UME']
    for tail in TAILS:
        if (len(tail) <= len(word)):
            if (word[-len(tail):] == tail):
                return True

    return False

#判断倒数第二音节
def penult(word):
    TAILS = ['ION', 'I', 'IC', 'ICS', 'ITIS', 'ESCENT', 'ESCENCE', 'SIVE', 'ANA', 'LIAR']

    for tail in TAILS:
        if (len(tail) <= len(word)):
            if (word[-len(tail):] == tail):
                return True

    return False

#判断倒数第三音节
def antepenultimate(word):
    TAILS = ['OKE', 'IA', 'OIN', 'ICAL', 'ENCY', 'LOGY', 'ZEE', 'IAN',
    'ERY', 'IST', 'OON', 'IENT', 'AIM', 'UOUS', 'ITY', 'TUDE', 'IUM', 'CRAT']

    for tail in TAILS:
        if (len(tail) <= len(word)):
            if (word[-len(tail):] == tail):
                return True

    return False

#判断第一音节
def firstSyll(word):
    TAILS = ['ANCY', 'AAR', 'ARY', 'ILE', 'ISM', 'ORY', 'MONY', 'ISH']

    WORDS = ['ORIGINAL', 'PRISONAL', 'RESIDUAL', 'ADJECTIVAL',
    'ANECDOTAL', 'CUSTOMARY', 'SCIENTIST', 'SLAVERY', 'ADVERTISE', 'MESSAGE']

    for w in WORDS:
        if (w == word):
            return True

    for tail in TAILS:
        if (len(tail) <= len(word)):
            if (word[-len(tail):] == tail):
                return True

    return False

#判断第二音节
def secondSyll(word):
    HEADS = ['A', 'AB', 'AC', 'AD', 'AL', 'BE', 'CON', 'DE',
    'DIS', 'EM', 'EN', 'IN', 'MIS', 'RE', 'TANS', 'UN']
    TAILS = ['OKE', 'IA', 'OIN', 'ICAL', 'ENCY', 'LOGY', 'ZEE',
    'IAN', 'ERY', 'IST', 'OON', 'IENT', 'AIM', 'UOUS', 'ITY', 'TUDE', 'IUM', 'CRAT']

    for head in HEADS:
        if (len(head) <= len(word)):
            if (word[:len(head)] == head):
                return True

    for tail in TAILS:
        if (len(tail) <= len(word)):
            if (word[-len(tail):] == tail):
                return True

    return False


# 分离出每个data里的单词，用以规则判断
def depart(data):
    l = []
    for d in data:
        word_list = d.split(' ')
        pos = word_list[0].find(':')
        w = word_list[0][:pos]
        l.append(w)
    return l

# 用规则判断预测位置
def predict(x, data, true_y):
    predict_y = []                   # 规则判断的结果
    predict_way = []                 # 记录是属于哪一种规则判断
    words = []                       # 能够用规则判断的词汇
    extract_y = []                   # 能够用规则判断的词汇的正确位置
    word_index = []                  # 适用于规则判断的词汇的下标列表++++++++++++++++++++
    i = 0
    index = 0                        # 词汇的下标++++++++++++++++++++
    for w in data:
        # 单音节词
        if (x[i]['vol_number'] == 1):
            predict_y.append(1)
            predict_way.append(0)
            words.append(w)
            extract_y.append(true_y[i])
            if (true_y[i] != 1):
                print("error")
            word_index.append(index)
            i += 1
            continue
            
        #末音节位置，没有符合后缀的单词
        if (ultima(w) == True):
            if (x[i]['vol_number'] >= 3):
                predict_y.append(x[i]['vol_number'])
                predict_way.append(-1)
                words.append(w)
                extract_y.append(true_y[i])
                word_index.append(index)
            i += 1
            continue

        #倒数第二音节
        #成功率：0.81
        if (penult(w) == True):
            if (x[i]['vol_number'] >= 3):
                predict_y.append(x[i]['vol_number'] - 1)
                predict_way.append(-2)
                words.append(w)
                extract_y.append(true_y[i])
                word_index.append(index)
            i += 1
            continue

        #倒数第三音节
        #成功率：0.67
        if (antepenultimate(w) == True):
            if (x[i]['vol_number'] >= 3):
                predict_y.append(x[i]['vol_number'] - 2)
                predict_way.append(-3)
                words.append(w)
                extract_y.append(true_y[i])
                word_index.append(index)
            i += 1
            continue

        #第一音节
        #成功率0.65
        if (firstSyll(w) == True):
            predict_y.append(1)
            predict_way.append(1)
            words.append(w)
            extract_y.append(true_y[i])
            word_index.append(index)
            i += 1
            continue

        i += 1
        index += 1

    return predict_y, extract_y, words, predict_way, word_index

def cv_loop(model, name):
    data = preprocess.readplz()
    x, y=preprocess.get(data)
    SPLITS = 100
    kf = KFold(n_splits=SPLITS)
    all_score = 0

    avg_train_f1score=0
    
    for train,test in kf.split(x):
        x_train,x_test,y_train,y_test = x[train],x[test],y[train],y[test]

        model.fit(x_train,y_train)
        predict_y = model.predict(x_test)       # 模型预测的结果 类型是numpy.ndarray
        
        data_test = data[test[0]:test[-1]+1]    # 用于规则预测的测试集数据
        word_list = depart(data_test)           # 测试集单词

        mid = list(map(extract_changed.extract_train, data[test[0]:test[-1]+1]))
        feature, true_y = vectorizer.departit(mid)
        t_predict_y, extract_y, words, predict_way, word_index = predict(feature, word_list, true_y)
        # 用规则判断结果去替换部分模型测试的结果
        i = 0
        for index in word_index:
            predict_y[index] = t_predict_y[i]
            i += 1


        # 计算分数
        t_score = f1_score(y_test,predict_y, average='weighted')
        avg_test_f1score += t_score

    
    print(name)
    print(avg_test_f1score/SPLITS)

if __name__ == '__main__':
    
    models = [RandomForestClassifier(), ExtraTreesClassifier(), KNeighborsClassifier(),
        DecisionTreeClassifier(), LogisticRegression(), SVC()]
    model_names = ['RandomForestClassifier()', 'ExtraTreesClassifier()', 'KNeighborsClassifier()',
        'DecisionTreeClassifier()', 'LogisticRegression()', 'SVC()']

    for i in range(len(models)):
        cv_loop(models[i], model_names[i])


