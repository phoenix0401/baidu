#--*--coding: utf8--*--
import pymongo
from pymongo import MongoClient
import cutnews
relationship = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫']
url = '/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/'
def condense_category():
    client = MongoClient('localhost', 27017)
    db = client['baidu']
    for rel in relationship:
        u_r = url + rel + '/' + '0'
        u_w = url + rel + '/' + '0_revise_revise'
        file_r = open(u_r)
        file_w = open(u_w, 'a')
        for line in file_r.readlines():
            k = 0
            if len([cur for cur in db.namelist.find({'name': line.split()[1]})]):
                if len([cur for cur in db.namelist.find({'name': line.split()[2]})]):
                    for word, flag in cutnews.cut_news(line.split()[0], [line.split()[1], line.split()[2]]):
                        if flag in ['nr', 'nrfg']:
                            k = k + 1
                    if k < 2:
                        file_w.write(line)
def condense_category_again():
    for rel in relationship:
        u_r = url + rel+ '/' + '0_revise_revise'
        u_w = url + rel+ '/' + '0_revise_final'
        file_r = open(u_r)
        file_w = open(u_w, 'a')
        for line in file_r.readlines():
            s = ''
            for item in line.split()[0:4]:
                s = s + item + '\t'
            s = s + '\n'
            file_w.write(s)
def condense_database():
    client = MongoClient('localhost', 27017)
    db = client['baidu_revise']
    for i in range(0, 50):
        print i
        db_client = db.names_require[i * 2]
        j = 0
        k = 0
        m = 0
        for cur in db_client.find({}):
            m = m + 1
            names = [cur['names'][0].encode('utf-8'), cur['names'][1].encode('utf-8')]
            news = cur['news'].encode('utf-8')
            if cutnews.cut_news(news, names):
                j = j+1
                pass
            else:
                k = k + 1
                db_client.delete_one(cur)
            if m % 500000 == 0:
                print 'm', m
                print 'j', j
                print 'k', k

if __name__ == '__main__':
    condense_database()