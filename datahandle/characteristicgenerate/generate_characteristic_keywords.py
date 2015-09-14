#--*--coding: utf8--*--
import jieba
import jieba.posseg as pesg
import pymongo
import cutnews
from pymongo import MongoClient
url = '/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/'
def generate_keywords():
    client = MongoClient('localhost', 27017)
    db= client['baidu']
    characteristic_keywords = db.characteristic_keywords
    file = open(url + '1')
    features = []
    lines = file.readlines()
    keywords_count = {}
    for line in lines:
        news = line.split()[3]
        words = pesg.cut(news)
        for word, flag in words:
            if flag not in features:
                features.append(flag)
    for feature in features:
        generate_characteristic_keywords_monogodb(feature)
    for line in lines:
        news = line.split()[3]
        words = pesg.cut(news)
        for w, flag in words:
            keywords_count[w] = 0
    for line in lines:
        news = line.split()[3]
        words = pesg.cut(news)
        for w, flag in words:
            keywords_count[w] = keywords_count[w] + 1
            if keywords_count[w] > 0:
                keywords_count[w] = -10000000
                characteristic_keywords.update({ 'feature': flag }, {'$push': { 'keywords': w}})
def generate_characteristic_keywords_monogodb(feature):
    client = MongoClient('localhost', 27017)
    db = client['baidu']
    characteristic_keywords = db.characteristic_keywords
    characteristic_keywords.insert_one({'feature': feature, 'keywords': []})
def generate_falsewords(rel):
    file = open(url + '1')
    file1 = open(url + '/0')
    file2 = open(url + '0+1+2', 'a')
    truekeywords = []
    falsekeywords = []
    for line in file.readlines():
        results = line.split()
        names = [results[1], results[2]]
        news = results[3]
        words = cutnews.cut_news(news, names)
            #去掉不关键属性
        if words:
            for i in range(0, len(words)):
                word = words[i][0]
                flag = words[i][1]
                if flag in ['c', 'v']:
                    if word not in truekeywords:
                        truekeywords.append(word)

    for line in file1.readlines():
        s = ''
        results = line.split()
        names = [results[1], results[2]]
        news = results[3]
        k = 1
        for name in names:
            flags = []
        for word, flag in pesg.cut(name):
            flags.append(flag)
            if flags[0] not in ['nr', 'nrfg']:
                k = 0
            if k == 1:
                words = cutnews.cut_news(news, names)
                    #去掉不关键属性
                if words:
                    length = len(words)
                    for i in range(0, length):
                        word = words[i][0]
                        flag = words[i][1]
                        next_flag = ''
                        if i < length - 1:
                            next_flag = words[i+1][1]
                        if (i == length - 1) & (length - 2 >= 0):
                            next_flag = words[i-1][1]
                        if flag in ['c', 'v']:
                            if word not in truekeywords + falsekeywords:
                                falsekeywords.append(word)
    falsekeywords = set(sorted(falsekeywords))
    s = ''
    for word in falsekeywords:
        s = s + word + ' '
    file2.write(s)
def generate_falsewords_implementation():
    relationwords = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫']
    for rel in relationwords:
        generate_falsewords(rel)

def generate_vague_words():
    file = open(url + '2')
    file1 = open(url + '22', 'a')
    org = []
    for line in file.readlines():
        words = line.split()
        names = [words[1], words[2]]
        news = words[3]
        results = cutnews.cut_news(news, names)
        if results:
            org_item = []
            for word, flag in results:
                if flag not in ['relationwords', 'namewords']:
                    org_item.append(word)
                else:
                    org_item.append(flag)
            if org_item not in org:
                org.append(org_item)
    for org_item in org:
        s = ''
        for o in org_item:
            s = s + o + ' '
        file1.write(s + '\n')

generate_keywords()