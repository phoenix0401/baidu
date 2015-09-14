#--*--coding: utf8--*--
import pymongo
from pymongo import MongoClient
import cutnews
relationship = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫']
url = ''
def condense_category()
    client = MongoClient('localhost', 27017)
    db = client['baidu']
    for rel in relationship:
        u_r = url + rel + '/' + '0'
        u_w = url + rel + '/' + '0_revise'
        file_r = open(u_r)
        file_w = open(u_w, 'a')
        for line in file_r.readlines():
            k = 0
            if (db.namelist.find(line.split())[1]) & (db.namelist.find(line.split()[2]))
                for word, flag in cutnews.cutnews(line.split()[0], [line.split()[1], line.split()[2]]):
                    if flag in ['nr', 'nrfg']:
                        k = k + 1
                if k < 2:
                    file_w.write(line)
