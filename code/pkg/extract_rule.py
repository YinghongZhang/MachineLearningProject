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

#判断末音节重音
def ultima(word):
    TAILS = ['ADE', 'EER', 'ESE', 'ESQUE', 'AIN', 'EE', 'ETTE', 'IQUE', 'INE', 'OON']

    Result = bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断倒数第二音节
def penult(word):
    #特殊情况，在倒数第三音节
    if word == 'rhetoric':
        return False

    TAILS = ['IC', 'ION', 'ANA', 'ESCENCE', 'ESCENT', 'I', 'ICS', 'ITIS', 'ID',
    'EOUS', 'IAL', 'IAN', 'IENT', 'IOUS', 'ISH', 'IT',
    'LIAR', 'SIVE', 'TAL', 'UOUS', 'AL', 'TARIAN', 'SIS', 'ENCE', 'ENT']

    Result = bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断倒数第三音节
def antepenultimate(word):
    TAILS = ['OUS', 'ITY', 'IAN', 'ANCE', 'ANCY', 'ENCE',
    'ENCY', 'ANT', 'ENT', 'LOGY', 'NOMY', 'ICAL', 'ITY', 'ABLE', 'ARY,' 'ERY', 'ORY']

    Result = bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断第一音节
def firstSyll(word):
    TAILS = ['ARY', 'ERY', 'ORY', 'ISM', 'IST', 'MONY', 'MENT']

    # 这些单词的重音都在第一个位置
    WORDS = ['ORIGINAL', 'PRISONAL', 'RESIDUAL', 'ADJECTIVAL',
    'ANECDOTAL', 'CUSTOMARY', 'SCIENTIST', 'SLAVERY', 'ADVERTISE', 'MESSAGE']

    Result = bool(word == w for w in WORDS)
    Result = Result or bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断第二音节
def secondSyll(word):
    HEADS = ['A', 'AB', 'AC', 'AD', 'AL', 'BE', 'CON', 'DE',
    'DIS', 'EM', 'EN', 'IN', 'MIS', 'RE', 'TANS', 'UN']
    TAILS = ['AIM', 'AIN', 'CUR', 'EEM', 'DUCE', 'ERE', 'FIRM',
    'GN', 'OIN', 'OKE', 'OSE', 'PT', 'RCE', 'SELF', 'UME']

    Result = bool(word[:len(head)] == head for head in HEADS if (len(head) <= len(word)))
    Result = Result or bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

# 分离出每个data里的单词，用以规则判断
def depart(data):
    l = []
    for d in data:
        word_list = d.split(' ')
        pos = word_list[0].find(':')
        w = word_list[0][:pos]
        if (ultima(w) == True or penult(w) == True or antepenultimate(w) == True
            or firstSyll(w) == True or secondSyll(w) == True):
            l.append(w)
    print('符合规则判断的词汇有：', len(l), '个 ')
    return l

# 用规则判断预测位置
def predict(x, data):
    predict_y = []
    i = 0
    for w in data:
        #末音节位置
        if (ultima(w) == True):
            predict_y.append(x[i]['vol_number'])
            continue
        #倒数第二音节
        if (penult(w) == True):
            if (x[i]['vol_number'] >= 2):
                predict_y.append(x[i]['vol_number'] - 1)
                continue
        #倒数第三音节
        if (antepenultimate(w) == True):
            if (x[i]['vol_number'] >= 3):
                predict_y.append(x[i]['vol_number'] - 2)
                continue
        #第一音节
        if (firstSyll(w) == True):
            if (x[i]['vol_number'] >= 1):
                predict_y.append(1)
                continue
        #第二音节
        if (secondSyll(w) == True):
            if (x[i]['vol_number'] >= 2):
                predict_y.append(2)
                continue
        predict_y.append(1)
        i += 1
    return predict_y


if __name__ == '__main__':
    data = helper.read_data('../asset/training_data.txt')
    word_list = depart(data)
    mid = list(map(extract_changed.extract_train, data))
    feature, true_y = vectorizer.departit(mid)
    predict_y = predict(feature, word_list)
    print(f1_score(true_y,predict_y, average='weighted'))