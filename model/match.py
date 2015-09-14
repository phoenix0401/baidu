#--*--coding: utf8--*--
import jieba, cutnews, model, pymongo
import jieba.posseg as pesg
from pymongo import MongoClient
fdir = ['cengshaozong', 'changguitian', 'chenjianbin', 'chenmeiqi', 'daibizhi', 'gaolin', 'geyou', 'guanyou', 'hanshaoyun', 'helin', 'huangbaiming', 'huanghong', 'jintielin', 'jinyouzhen', 'lian', 'liguangji', 'liguohao', 'lijian', 'liruiying', 'lishaochun', 'liuxiurong', 'liyaoxiang', 'liying', 'liyundi', 'luomeiwei', 'maidi', 'maihongmei', 'maji', 'maoweitao', 'mayun', 'mazhiming', 'sanmao', 'sunlirong', 'sunzhihao', 'wanglixin', 'wangshuo', 'wangxiaobao', 'wangxiaohu', 'wangxiaomin', 'wangxuebing', 'wangxueqi', 'xianghuasheng', 'yuzhanyuan', 'zhangbo', 'zhanghanyu', 'zhanghaolong', 'zhaopeiru', 'zhouhaiying', 'zhoushaolin', 'zhuzhenmo']
names_require = ['曾少宗', '521886', '常贵田', '2321257', '陈建斌', '11640', '陈美琪', '63872', '戴碧芝', '8538324', '郜林', '4310539', '葛优', '335918', '冠佑', '390053', '韩少云', '5560239', '何琳', '32221', '黄百鸣', '5599577', '黄宏', '5862', '金铁林', '816268', '金宥真', '8414614', '李安', '16812', '李光洁', '4413008', '李国豪', '4616848', '李健', '3', '李瑞英', '802226', '李少春', '80856', '刘秀荣', '31512', '黎耀祥', '1970419', '黎婴', '2753192', '李云迪', '855485', '罗美薇', '1274617', '麦蒂', '142344', '买红妹', '9182605', '马季', '84373', '茅威涛', '2929190', '马云', '6252', '马志明', '1260216', '三毛', '1364178', '孙立荣', '4161', '孙志浩', '42178', '王栎鑫', '4171833', '王朔', '436', '王小宝', '30272', '王小虎', '7268667', '汪小敏', '9920009', '王学兵', '2058748', '王学圻', '3585146', '向华胜', '9384507', '于占元', '4392373', '张博', '9426', '张涵予', '747579', '张豪龙', '977879', '赵佩茹', '5033042', '周海婴', '2492347', '周少麟', '10122402', '朱镇模', '5147823']
rel_list = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫', '绯闻男友', '学生', '丈夫', '前男友', '前夫', '配偶']
rel_one_way = ['暧昧', '传闻不和', '分手', '闺蜜', '老乡', '朋友', '同居', '同为校花', '昔日情敌', '同学', '撞衫', '配偶']
rel_two_way_single = ['翻版', '经纪人', '偶像']
rel_two_way_double = ['绯闻女友', '老师', '妻子', '前女友', '前妻', '绯闻男友', '学生', '丈夫', '前男友', '前夫']
transform_dict = {'绯闻女友': '绯闻男友', '绯闻男友': '绯闻女友', '老师': '学生', '学生': '老师', '妻子': '丈夫', '丈夫': '妻子', '前女友': '前男友', '前男友': '前女友', '前妻': '前夫', '前夫': '前妻'}
client = MongoClient('localhost', 27017)
db = client['baidu_revise']
url = '/Users/wutong/workspace/da/baidu/data/final_right/'
def match(news, names):
    rels_count = 0
    names_count = 0
    jieba_results = cutnews.cut_news(news, names)
    if jieba_results:
        rels_loc = jieba_results[1] + []
        names_loc = jieba_results[2] + []
        results = jieba_results[0]
        rels_count = len(rels_loc)
        names_loc = len(names_loc)
        if rels_count == 2 & names_count == 2:
            if (((rels_loc[0] > names_loc[0]) & (rels_loc[0] > names_loc[1])) & (rels_loc[1] > names_loc[1])) | ((rels_loc[0] < names_loc[0]) & ((rels_loc[1] < names_loc[1]) | (rels_loc[1] > names_loc[0]))) | ((rels_loc[0] < names_loc[0]) & (rels_loc[1] > names_loc[1])):
                return False
            elif rels_loc[0] > names_loc[1]:
                for word, flag in words[rels_loc[0]:rels_loc[1] + 1]:
                    if flag == v_transform:
                        if rels_loc[0] == ['妻子', '女友']:
                            pass
            
            elif (rels_loc[0] + 1) != (rels_loc[1] + 0):
                pass
        elif rels_count == 2 & names_count == 3:
            pass
        elif rels_count == 1:
            return model.single_relationship(results ,news)
    return False
def generate_results():
#    transform_list = [1, 3, 4, 6, 7, 8, 10, 11, 14, 17, 20, 21, 22, 23, 25, 28, 29, 30, 32, 37, 38, 41, 43, 48]
#    transform_list = [3, 4, 6, 7, 8, 10, 11, 14, 17, 20, 21, 22, 23, 25, 28, 29, 30, 32, 37, 38, 41, 43, 48]
    for i in range(0, 50):
        print i
        db_client = db.names_require[i * 2]
        u = url + fdir[i]
        first_name = ['', names_require[i * 2]]
        level = 1
        generate_results_item(db_client, u, first_name, level)
def generate_results_item(db_client, u,first_name, level):
    first_name_item1 = first_name + []
    f_name = first_name_item1[1]
    b_name = first_name_item1[0]
    print level
    value = []
    condense_name_list = []
    condense_ids_list = []
    file = open(u, 'a')
    for cur in db_client.find({'names': f_name}):
        news = cur['news'].encode('utf-8')
        names = []
        ids = []
        for i in range(0, len(cur['names'])):
            names.append(cur['names'][i].encode('utf-8'))
            ids.append(cur['ids'][i].encode('utf-8'))
        results_item = match(news, names)
        if results_item:
            rel = results_item[2]
            names_return = [results_item[0], results_item[1]]
            ids_return = [ids[names.index(results_item[0])], ids[names.index(results_item[1])]]
            one_way_tag = 1
            flag = results_item[3]
            if (f_name in names_return) & (b_name not in names_return):
                if rel in rel_one_way:
                    if names_return[0] != f_name:
                        names_return.reverse()
                        ids_return.reverse()
                if rel in rel_two_way_single:
                    if names_return[0] != f_name:
                        one_way_tag = 0
                if rel in rel_two_way_double:
                    if names_return[0] != f_name:
                        rel = transform_dict[rel]
                        names_return.reverse()
                        ids_return.reverse()
                if one_way_tag:
                    name = names_return[1]
                    if name in condense_name_list:
                        if flag == '1':
                            value[condense_name_list.index(name)][rel_list.index(rel)] += 1
                        else:
                            value[condense_name_list.index(name)][rel_list.index(rel)] -= 100
                    else:
                        condense_name_list.append(names_return[1])
                        condense_ids_list.append(ids_return[1])
                        value.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    condense_rel =[rel_list[v.index(max(v))] for v in value]
    condense_key = [max(v) for v in value]
    final_name_list = []
    for r in rel_list:
        k = 0
        name_mid = ''
        id_mid = ''
        for i in range(0, len(condense_rel)):
            if condense_rel[i] == r:
                if condense_key[i] > k:
                    k = condense_key[i]
                    name_mid = condense_name_list[i]
                    id_mid = condense_ids_list[i]
        if k > 0:
            file.write(r + '\t' + f_name + '\t' + name_mid + '\t' + ids_return[0] + '\t' + id_mid + '\t' + 'layer' + str(level) + '\n')
            final_name_list.append(name_mid)
    print len(final_name_list)
    level = level + 1
    if level < 4:
        for name in final_name_list:
            first_name_item2 = [f_name ,name]
            generate_results_item(db_client, u, first_name_item2, level)
if __name__ == '__main__':
        generate_results()