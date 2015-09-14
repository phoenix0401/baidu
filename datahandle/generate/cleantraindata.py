#--*--coding: utf8--*--
import jieba
import jieba.posseg as pesg
def condense_data():
    file = open('/Users/wutong/workspace/da/baidu/RawData/competition-test-set/test_entity_sentence/test_entity_sentence.cengshaozong')
    file1 = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensenews_cengshaozong.txt', 'a')
    mid = ''
    for line in file.readlines():
        results = line.split()
        news = line.split()[0]
        if len(results) < 8:
            if news[:6] != mid:
                file1.write(line)
                mid = news[:6]
def category_train_data():
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensetraindata.txt')
    for line in sorted(file.readlines()):
        words = line.split()
        file1 = open('/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/' + words[4], 'a')
        file1.write(line)
        file1.close()
def category_train_data_detail(s):
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensetraindata.txt')
    file1 = open('/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/' + s  + '/results', 'a')
    for line in file.readlines():
        words = line.split()
        if words[0] == s:
            file1.write(line)
def category_detail(s):
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/' + s  + '/results')
    for line in file.readlines():
        words = line.split()
        file1 = open('/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/' + s  + '/' + words[4], 'a')
        file1.write(line)
def get_relation_words():
    relationwords = []
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensetraindata.txt')
    for line in file.readlines():
        words = line.split()
        if words[0] not in relationwords:
            relationwords.append(words[0])
    return relationwords
condense_data()