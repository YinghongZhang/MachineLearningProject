# -*- coding: UTF-8 -*-
def read_data(file_path):
	with open(file_path) as f:
		lines = f.read().splitlines()
	return lines

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

    return target, feature

#function below returns a array that contain infomation about prefix and postfix of word
def head_and_tails(word):
    head = ['A','AB','AC','AD','AL','BE','CON','DE','DIS','IM','IN','EM','EN','FOR','PRE',
    'PRO','TO','TRANS','MIS','RE','TANS','UN']
    tail1 = ['AIM','AIN','CUR','DUCE','ERE','FIRM','GN','OIN','OKE','OSE','PT','RCE','SELF','UME']
    tail2 = ['AL','ACY','AGE','ER','OR','FUL','ISM','IST','IVE','IZE','LESS','ISE','LY','NESS','SHIP','ING','ABLE','RY','TY']
    tail3 = ['ADA','ETTE','EE','ESE','QUE','AAR','EER','ZEE','ROO']
    tail4 = ['IC','ION','ANA','ESCENT','i','ICS','SIS']
    result = [0,0,0,0,0]  #result array
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

    return result

if __name__ == "__main__":
    print("start!")
    data_lines = read_data("training_data.txt")

    feature_list = []
    target_list = []
    
    for data in data_lines:
        target, feature = extract_train(data)
        target_list.append(target)
        feature_list.append(feature)
    # with open("target_result.txt", 'w') as fout1:
    #     with open("fearure_result.txt", 'w') as fout2:
    #         i = 0
    #         for data in data_lines:
    #             target, feature = extract_train(data)
    #             target_list.append(target)
    #             feature_list.append(feature)
    #             fout1.write(str(target)+'\n')
    #             fout2.write(str(feature)+'\n')

                # i += 1
                # if i == 10:
                #     break
    
    from sklearn.feature_extraction import DictVectorizer
    vec = DictVectorizer()
    vec1 = DictVectorizer()
    feature_array = vec.fit_transform(feature_list).toarray()
    target_array = vec1.fit_transform(target_list).toarray()

    test = True
    if test == False:
        # 使数据在0-1之间,但是跑出来数据都为0
        from sklearn import preprocessing
        normalized_feature = preprocessing.normalize(feature_array)
        normalized_target = preprocessing.normalize(target_array)
    else:
        normalized_feature = feature_array
        normalized_target = target_array
    
    from sklearn import metrics
    from sklearn.ensemble import ExtraTreesClassifier
    model = ExtraTreesClassifier()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    # display the relative importance of each attribute
    print(vec.get_feature_names())
    print(model.feature_importances_)
    print('---------')

    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    # print(vec.get_feature_names())
    # # print(model.feature_importances_)
    print("-----------")

    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')

    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')

    from sklearn.svm import SVC
    # fit a SVM model to the data
    model = SVC()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')


    print('Done!')