#--*--coding: utf8--*--
import pymongo
from pymongo import MongoClient
url = '/Users/wutong/workspace/da/baidu/data/condensedata/condensenews.txt'
client = MongoClient('localhost', 27017)
db = client['baidu']
def generate_relationship_collections():
    users = db.users
    relationship = db.relationship
    for person in users.find():
        relationship.insert_one({'name': person['name'], 'id': person['id']})
def generate_name_collections():
    file = open(url)
    namelist = db.namelist
    for line in file.readlines():
        results = line.split()
        length = len(results)/2
        if (length == 3) & (len(results) == 7):
            try:
                int(results[-3])
                for i in range(0, length):
                    a_results = [a for a in namelist.find({'name': results[i + 1]})]
                    if not a_results:
                        namelist.insert_one({'name': results[i + 1]})
            except:
                pass
def generate_news_collections():
    pass
generate_name_collections()
    rel = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫']
    for i in range(rel):
        db_client