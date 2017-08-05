'''
总共有5种情况：
末音节、倒数第二音节、倒数第三音节、第一音节、第二音节
所以有五个函数，这五个函数，从上到下，优先级下降，所以，前面一个函数判断Ture，后面就不用判断了
但是，具体这些规则判断效果怎么样，还要去试验一下
毕竟这些规则，还是大多数情况下正确，具体正确率到多少，还是不清楚的
'''

#判断末音节重音
def ultima(word):
    TAILS = [ADE, EER, ESE, ESQUE, ADE, AIN, EE, EER, ESQUE, ETTE, IQUE, INE, OON]

    Result = bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断倒数第二音节
def penult(word):
    #特殊情况，在倒数第三音节
    if word == 'rhetoric':
        return False

    TAILS = [IC, ION, ANA, ESCENCE, ESCENT, I, ICS, ITIS, ID,
    EOUS, IAL, IAN, IENT, IOUS, ISH, IT, LIAR, SIVE, TAL, UOUS, AL, TARIAN, SIS, ENCE, ENT]

    Result = bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断倒数第三音节
def antepenultimate(word):
    TAILS = [OUS, ITY, IAN, ANCE, ANCY, ENCE, ENCY, ANT, ENT, LOGY, NOMY, ICAL, IAN, ITY, ABLE, ARY, ERY, ORY]

    Result = bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断第一音节
def firstSyll(word):
    TAILS = [ARY, ERY, ORY, ISM, IST, MONY, MENT]
    WORDS = [ORIGINAL, PRISONAL, RESIDUAL, ADJECTIVAL, ANECDOTAL, CUSTOMARY, SCIENTIST, SLAVERY, ADVERTISE, MESSAGE]

    Result = bool(word == w for w in WORDS)
    Result = Result or bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result

#判断第二音节
def secondSyll(word):
    HEADS = [A, AB, AC, AD, AL, BE, CON, DE, DIS, EM, EN, IN, MIS, RE, TANS, UN]
    TAILS = [AIM, AIN, CUR, EEM, DUCE, ERE, FIRM, GN, OIN, OKE, OSE, PT, RCE, SELF, UME]

    Result = bool(word[:len(head)] == head for head in HEADS if (len(head) <= len(word)))
    Result = Result or bool(word[-len(tail):] == tail for tail in TAILS if (len(tail) <= len(word)))

    return Result