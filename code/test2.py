# -*- coding: UTF-8 -*-
from pkg.extract_modified import extract_train
from pkg.extract_modified import head_and_tails
from pkg.helper import read_data


if __name__ == "__main__":
    print("start!")
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

    test = True
    if test == False:
        # 使数据在0-1之间,但是跑出来数据都为0
        from sklearn import preprocessing
        normalized_feature = preprocessing.normalize(feature_array)
        normalized_target = preprocessing.normalize(target_array)
    else:
        normalized_feature = feature_array
        normalized_target = target_array

    from sklearn.liner_model import LogisticRegression
    print('LogisticRegression')
    model = LogisticRegression()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predicted(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')

    from sklearn import metrics
    from sklearn.ensemble import ExtraTreesClassifier
    print("ExtraTreesClassifier")
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
    print('GaussianNB')
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
    print('KNN')
    model = KNeighborsClassifier()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')

    from sklearn.tree import DecisionTreeClassifier
    print('DecisionTree')
    model = DecisionTreeClassifier()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')

    from sklearn.svm import SVC
    print('SVC')
    # fit a SVM model to the data
    model = SVC()
    model.fit(normalized_feature, normalized_target)
    expected = normalized_target
    predicted = model.predict(normalized_feature)
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print('------------')

    print('Done!')