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
db1 = client['baidu']
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
        elif rels_count == 1:
            return model.single_relationship(results ,news)
    return False
def generate_results():
    for i in range(0, 50):
        print i
        db_client = db.names_require[i * 2]
        u = url + fdir[i]
        first_name = ['', names_require[i * 2]]
        level = 1
        generate_results_item(db_client, u, first_name, level)
def generate_results_item(db_client, u,first_name, level):
    file = open(u, 'a')
    first_name_ge = first_name + []
    b_name = first_name_ge[0]
    f_name = first_name_ge[1]
    db_right_client = db1.right_rel
    db_mid_client = db_right_client
    if db_right_client.find_one({'names': f_name}):
        db_mid_client = db_right_client
    else:
        db_mid_client = db_client
    f_name_id = ''
    cur = db_client.find_one({'names': f_name})
    if cur:
        pass
    else:
        cur = db_right_client.find_one({'name': f_name})
    if cur['names'][0].encode('utf-8') == f_name:
        f_name_id = cur['ids'][0].encode('utf-8')
    else:
        f_name_id = cur['ids'][1].encode('utf-8')

    print level


    initial_name_list = []
    cur_all_list = {}
    for cur in db_mid_client.find({'names': f_name}):
        name = ''
        if cur['names'][0].encode('utf-8') != f_name:
            name = cur['names'][0].encode('utf-8')
        else:
            name = cur['names'][1].encode('utf-8')
        if name != b_name:
            if name not in initial_name_list:
                initial_name_list.append(name)
                cur_all_list[name] = [cur]
            else:
                cur_all_list[name].append(cur)
    if len(initial_name_list) == 0:
        db_mid_client = db_client
        for cur in db_mid_client.find({'names': f_name}):
            name = ''
            if cur['names'][0].encode('utf-8') != f_name:
                name = cur['names'][0].encode('utf-8')
            else:
                name = cur['names'][1].encode('utf-8')
            if name != b_name:
                if name not in initial_name_list:
                    initial_name_list.append(name)
                    cur_all_list[name] = [cur]
                else:
                    cur_all_list[name].append(cur)

    final_mid = []
    for name in initial_name_list:
        id = ''
        cur = db_client.find_one({'$and': [{'names': f_name}, {'names': name}]})
        if cur:
            pass
        else:
            cur = db_right_client.find_one({'names': name})
        if cur['names'][0].encode('utf-8') == f_name:
            id = cur['ids'][1].encode('utf-8')
        else:
            id = cur['ids'][0].encode('utf-8')
        
        cur_all = cur_all_list[name]
        value_all = []
        rel_all = []

        for cur in cur_all:
            news= cur['news'].encode('utf-8')
            results = match(news, [f_name, name])
            if results:
                r_real = results[2]
                r_tag = results[3]
                one_way_tag = 1
                if results[0] != name:
                    if r_real in rel_two_way_single:
                            one_way_tag = 0
                    if r_real in rel_two_way_double:
                            r_real = transform_dict[r_real]
                if one_way_tag:
                    if r_real not in rel_all:
                        rel_all.append(r_real)
                        value_all.append(1)
                    l = rel_all.index(r_real)
                    if r_tag == '0':
                        value_all[l] -= 100
                        if r_real in ['妻子', '丈夫']:
                            if transform_dict[r_real] not in rel_all:
                                rel_all.append(transform_dict[r_real])
                                value_all.append(1)
                            value_all[rel_all.index(transform_dict[r_real])] -= 100

                    if r_tag == '1':
                        value_all[l] += 1
        v_max = 0
        l = -1
        for l_ in range(0, len(value_all)):
            if value_all[l_] > v_max:
                v_max = value_all[l_]
                l = l_
        if l > -1:
            final_mid.append([rel_all[l], name, id, value_all[l]])
    final_final = list(set([r for r, n, i, v in final_mid]))
    final_name_list = []
    for r in final_final:
        max = 0
        l = 0
        for l_ in range(0, len(final_mid)):
            if final_mid[l_][0] == r:
                if final_mid[l_][3] > max:
                    max = final_mid[l_][3]
                    l = l_
        final_name_list.append(final_mid[l][1])
        file.write(r + '\t' + f_name + '\t' + final_mid[l][1] + '\t' + f_name_id + '\t' + final_mid[l][2] + '\t' + 'layer' + str(level) + '\n')
    level = level + 1
    if level < 4:
        for name in final_name_list:
            first_name_next = [f_name ,name]
            generate_results_item(db_client, u, first_name_next, level)
if __name__ == '__main__':
    generate_results()