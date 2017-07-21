# -*- coding: UTF-8 -*-
from extract_modified import extract_train
from extract_modified import head_and_tails
from helper import read_data
from prepocess import get
from prepocess import result

def get_predicted_lists():

    data_lines = read_data("training_data.txt")
    feature_list = []
    target_list = []
    
    for data in data_lines:
        target, feature = extract_train(data)
        target_list.append(target)
        feature_list.append(feature)
    
    from sklearn.feature_extraction import DictVectorizer
    vec = DictVectorizer()
    vec1 = DictVectorizer()
    feature_array = vec.fit_transform(feature_list).toarray()
    target_array = vec1.fit_transform(target_list).toarray()

    

    # feature_array, target_array = get(data)
    # print(type(feature_array))
    # print(type(target_array))
    test = True # 决定是否要把数据归一化
    if test == False:
        # 归一化使数据在0-1之间,但是跑出来数据都为0
        from sklearn import preprocessing
        normalized_feature = preprocessing.normalize(feature_array)
        normalized_target = preprocessing.normalize(target_array)
    else:
        normalized_feature = feature_array
        normalized_target = target_array
    
    all_lists = []
    print('-------------------------')
    print(type(normalized_feature))
    print(type(normalized_target))
    print('-------------------------')

    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier()
    model.fit(normalized_feature, normalized_target)
    DecisionTreeClassifierpredicted = list(model.predict(normalized_feature))
    all_lists.append(DecisionTreeClassifierpredicted)
    
    from sklearn.ensemble import ExtraTreesClassifier
    model = ExtraTreesClassifier()
    model.fit(normalized_feature, normalized_target)
    ExtraTreesClassifierpredicted = list(model.predict(normalized_feature))
    all_lists.append(ExtraTreesClassifierpredicted)

    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(normalized_feature, normalized_target)
    GaussianNBpredicted = list(model.predict(normalized_feature))
    all_lists.append(GaussianNBpredicted)

    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(normalized_feature, normalized_target)
    KNeighborsClassifierpredicted = list(model.predict(normalized_feature))
    all_lists.append(KNeighborsClassifierpredicted)

    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier()
    model.fit(normalized_feature, normalized_target)
    DecisionTreeClassifierpredicted = list(model.predict(normalized_feature))
    all_lists.append(DecisionTreeClassifierpredicted)

    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(normalized_feature, normalized_target)
    LogisticRegressionpredicted = list(model.predict(normalized_feature))
    all_lists.append(LogisticRegressionpredicted)

    from sklearn.svm import SVC
    model = SVC()
    model.fit(normalized_feature, normalized_target)
    SVCpredicted = list(model.predict(normalized_feature))
    all_lists.append(SVCpredicted)
    
    return all_lists

# for test:
if __name__ == '__main__':
    from sklearn.naive_bayes import BernoulliNB
    model = BernoulliNB()
    data = read_data("training_data.txt")
    feature_array, target_array = get(data)
    get_predicted_lists()
    print('?')
    predicted = result(get_predicted_lists())
    print(type(predicted))
    print(model.score(normalized_feature, target_array))