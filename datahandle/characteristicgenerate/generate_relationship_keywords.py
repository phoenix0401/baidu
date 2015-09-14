#--*--coding: utf8--*--
import pymongo
from pymongo import MongoClient
import jieba
import jieba.posseg as pesg
import jieba.analyse
import cutnews
relationship = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫']
def get_key_words():
    client = MongoClient('localhost', 27017)
    db= client['baidu']
    relationship_keywords = db.relationship_keywords
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensetraindata.txt')
    for line in file.readlines():
        items = line.split()
        names = [items[1], items[2]]
        news = items[3]
        rel = items[0]
        for name in names:
            jieba.add_word(name, freq = None, tag = 'nr')
        words = pesg.cut(news)
        for word, flag in words:
            if flag == 'n':
                relationship_keywords.update({ 'name': rel }, {'$addToSet': { 'keywords': word}})
def condense_key_words(rel):
    client = MongoClient('localhost', 27017)
    db= client['baidu']
    relationship_keywords = db.relationship_keywords
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensetraindata.txt')
    file1 = ''
    name_list = []
    for line in file.readlines():
        items = line.split()
        names = [items[1], items[2]]
        news = items[3]
        rela = items[0]
        if rela == rel:
            for name in names:
                name_list.append(name)
                jieba.add_word(name, freq = None, tag = 'nr')
            file1 = file1 + news + '\n'
    tags = jieba.analyse.extract_tags(file1, topK=20, withWeight=False, allowPOS=())
    for tag in tags:
        if tag.encode('utf-8') not in name_list:
            relationship_keywords.update({ 'name': rel }, {'$addToSet': { 'keywords': tag}})
def condense_key_words_revise(rel):
    client = MongoClient('localhost', 27017)
    db= client['baidu']
    relationship_keywords = db.relationship_keywords1
    file = open('/Users/wutong/workspace/da/baidu/data/condensedata/condensetraindata.txt')
    for line in file.readlines():
        items = line.split()
        names = [items[1], items[2]]
        news = items[3]
        rela = items[0]
        if rela == rel:
            results = cutnews.cut_news(news, names)
            for word, flag in results:
                if flag not in ['relationwords', 'namewords']:
                    relationship_keywords.update({ 'name': rel }, {'$addToSet': { 'keywords': word}})



def generate_relashionship_keywords_mongodb():
    client = MongoClient('localhost', 27017)
    db= client['baidu']
    relationship_keywords = db.relationship_keywords1
    for rel in relationship:
        relationship_keywords.insert_one({'name': rel, 'keywords': []})
generate_relashionship_keywords_mongodb()
for rel in relationship:
    condense_key_words_revise(rel)