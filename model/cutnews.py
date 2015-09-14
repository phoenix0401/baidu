#--*--coding: utf8--*--
import jieba
import jieba.posseg as pesg
import pymongo
from pymongo import MongoClient
features = ['v', 'd', 'c', 'p', 'a', 'n']
vague_features = ['m', 'y', 'v']
client = MongoClient('localhost', 27017)
db = client['baidu']
relationship_keywords = db.relationship_keywords
rel_one_way = ['暧昧', '传闻不和', '分手', '闺蜜', '老乡', '朋友', '同居', '同为校花', '昔日情敌', '同学', '撞衫', '配偶']
rel_two_way_single = ['翻版', '经纪人', '偶像']
rel_two_way_double = ['绯闻女友', '老师', '妻子', '前女友', '前妻', '绯闻男友', '学生', '丈夫', '前男友', '前夫']
def generate_dict():
    jieba.add_word('绯闻女友', freq = None, tag = 'nr')
    for word in ['被曝', '被传', '被称', '被誉为', '被称为', '被誉', '被指']:
        jieba.add_word(word, freq = 1000, tag = 'v_passive')
    for word in ['否认', '不同意', '不赞成', '辟谣', '澄清', '没有', '不是', '不做']:
        jieba.add_word(word, freq = 1000, tag = 'v_false')
    for word in ['与', '和', '同', '跟', '跟着']:
        jieba.add_word(word, freq = 1000, tag = 'v_conj')
    for word in ['的']:
        jieba.add_word(word, freq = 1000, tag = 'v_stop')
    for word in ['是', '为', '正是', '竟是', '像是', '就是']:
        jieba.add_word(word, freq = 1000, tag = 'v_prep')
    for word in ['曾是', '曾经是', '被']:
        jieba.add_word(word, freq = 1000, tag = 'v_special')
    for word in ['变', '变成', '成为', '长成', '变为']:
        jieba.add_word(word, freq = 1000, tag = 'v_transform')
    for cur in relationship_keywords.find():
        for word in cur['keywords']:
            jieba.add_word(word.encode('utf-8'), freq = 1000, tag = 'n_false')
            for word1 in ['没' ,'没有', '破', '无', '险', '不', '不是', '否认', '不同意', '不赞成', '辟谣', '澄清', '不算', '做不成', '不做', '扮演', '饰演', '饰演', '装', '装作', '装成']:
                jieba.add_word(word1 + word.encode('utf-8'), freq = 10000, tag = 'n_false')
    for word in ['全能偶像', '国民偶像', '全民偶像', '美女偶像', '偶像界', '偶像运动会', '偶像一哥', '偶像化', '偶像男孩', '偶像榜', '全名偶像', '全名新偶像', '亚洲偶像', '体坛偶像', '幸福偶像', '人气偶像', '新锐偶像', '新锐偶像', '新偶像', '偶像派', '偶像本色', '偶像归来', '新偶像天团', '偶像天团', '偶像形象', '北大偶像', '清华偶像', '民国偶像', '个人崇拜', '偶像男神', '偶像女神', '偶像剧', '偶像气质', '偶像栏目剧', '时尚偶像', '台偶像', '台湾偶像', '校花级']:
        jieba.add_word(word, freq = 10000, tag = 'n_false')
    for word in ['小朋友', '不算朋友', '不是朋友', '丑到没朋友', '帅到没朋友', '朋友队']:
        jieba.add_word(word, freq = 10000, tag = 'n_false')
generate_dict()
def cut_news(news, names):
    #添加自定义词典
    for name in names:
        jieba.add_word(name, freq = 1000, tag = 'nr')
    #初步分词
    words = [[word.encode('utf-8'), flag.encode('utf-8')] for word, flag in pesg.cut(news)]
    #纪录名字与关系关键词在words中的index
    k = 0
    names_loc = []
    rels_loc = []
    for word, flag in words:
        cur = relationship_keywords.find_one({'keywords': word})
        if cur:
            rel = cur['name'].encode('utf-8')
            if rel in rel_one_way:
                words[k][1] = 'relationwords_one'
            elif rel in rel_two_way_single:
                words[k][1] = 'relationwords_two_single'
            elif rel in rel_two_way_double:
                words[k][1] = 'relationwords_two_double'
            rels_loc.append(k)
        elif word in names:
            words[k][1] = 'namewords'
            names_loc.append(k)
        k += 1

    if (len(names_loc) != len(names)) | (len( rels_loc) < 1):
        return False

    return [words,  rels_loc, names_loc]