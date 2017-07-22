def extract_train(strs):
    word_list = strs.split(' ')
    vol_list=[]       #in case you wanna use it,not sure it's useful or not  
    cons_list=[]      #in case you wanna use it,not sure it's useful or not 
    vol_count = 1
    pri_stress_position = 0
    sec_stress_position = 0      #in case you wanna use it,not sure it's useful or not 
    for x in word_list:
        if x[-1] =='0':
            vol_list.append(x[:-1])
            vol_count+=1
        elif x[-1] == '1':
            vol_list.append(x[:-1])
            pri_stress_position = vol_count
            vol_count+=1
        elif x[-1] ==  '2':
            vol_list.append(x[:-1])
            sec_stress_position = vol_count
            vol_count+=1
        else:
            cons_list.append(x)
    feature = {'vol_number':vol_count-1}                    # 元音数量
    target = {'pri_stress_position':pri_stress_position}    # 重音位置
    
    head_tails = []
    x = word_list[0].find(':')              # 找到:的位置
    head_tails = head_and_tails(word_list[0][:x])   #提取出单词并检查前后缀
    feature['head'] = head_tails[0]
    feature['tail1'] = head_tails[1]
    feature['tail2'] = head_tails[2]
    feature['tail3'] = head_tails[3]
    feature['tail4'] = head_tails[4]
    feature['tail5'] = head_tails[5]

    return target, feature

#function below returns a array that contain infomation about prefix and postfix of word
def head_and_tails(word):
    head = ['A','AB','AC','AD','AL','BE','CON','DE','DIS','IM','IN','EM','EN','FOR','PRE',
    'PRO','TO','TRANS','MIS','RE','TANS','UN']
    tail1 = ['AIM','AIN','CUR','DUCE','ERE','FIRM','GN','OIN','OKE','OSE','PT','RCE','SELF','UME']
    tail2 = ['AL','ACY','AGE','ER','OR','FUL','ISM','IST','IVE','IZE','LESS','ISE','LY','NESS','SHIP','ING','ABLE','RY','TY']
    tail3 = ['ADA','ETTE','EE','ESE','QUE','AAR','EER','ZEE','ROO']
    tail4 = ['IC','ION','ANA','ESCENT','i','ICS','SIS']
    tail5 = ['ABLE','IBLE','ARY','ERY','ORY']
    result = [0,0,0,0,0,0]  #result array
    for x in head:
        if len(x) <= len(word):
            if word[:len(x)] == x:
                result[0] = 1
    for x in tail1:
        if len(x) <= len(word):
            if word[-len(x):] == x:
                result[1] = 1
    for x in tail2:
        if len(x) <= len(word):
            if word[-len(x):] == x:
                result[2] = 1
    for x in tail3:
        if len(x) <= len(word):
            if word[-len(x):] == x:
                result[3] = 1
    for x in tail4:
        if len(x) <= len(word):
            if word[-len(x):] == x:
                result[4] = 1
    for x in tail5:
        if len(x) <= len(word):
            if word[-len(x):] == x:
                result[5] = 1
    return result