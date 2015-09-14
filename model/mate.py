#--*--coding: utf8--*--
import cutnews
main_features = ['v', 'n', 'v_false', 'v_conj', 'v_prep', 'v_stop', 'v_special']
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['baidu']
def feiwennvyou(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'n', 'v_stop']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_two_double':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)

#    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_double'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_double', ], ['namewords', 'v_conj', 'namewords', 'v', 'v_prep', 'relationwords_two_double']]:
#        return [names[0], names[1], r_real, '1']
#    if orgnize_flag in [['namewords', 'v', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_double']]
#        return [names[0], names[1], r_real, '1']
#    if orgnize_flag in [['namewords', 'v', 'namewords', 'v_prep', 'relationwords_two_double']]:
#        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'relationwords_two_double', 'v_prep', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'v_stop', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
#    if orgnize_flag in [['namewords', 'namewords', 'v', 'v_prep', 'relationwords_two_double']]:
#        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_conj', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'v_conj', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_two_double', 'namewords', 'v', 'namewords']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['v_conj', 'namewords', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_two_double', 'namewords', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_double', 'v', 'namewords'], ['namewords', 'namewords', 'v_conj', 'relationwords_two_double']]:
        return [names[0], names[1], r_real, '0']


    return False

def jingjiren(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'v_false', 'v_stop']:
            del words[loc]
#    words = remove_repeat(words)


    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_two_single':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)


    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_single', ], ['namewords', 'v_conj', 'namewords', 'v', 'v_prep', 'relationwords_two_single']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'relationwords_two_single', 'v_prep', 'namewords'], ['namewords', 'v', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'relationwords_two_single']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_single', 'v', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'relationwords_two_single']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_single', 'n', 'v_conj', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'n', 'relationwords_two_single']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'n', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'n', 'v', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_conj', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_two_single', 'namewords', 'v','namewords']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'n', 'namewords', 'relationwords_two_single']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_single', 'n', 'namewords']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['relationwords_two_single', 'namewords', 'v','namewords']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'n', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in  [['namewords', 'relationwords_two_single', 'v', 'n', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_two_single', 'namewords', 'v', 'n', 'namewords']]:
        return [names[1], names[0], r_real, '1']

    return False

def fanban(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['n', 'v_false', 'v_stop', 'v_special']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_one':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)

    flag = 0
        
    if orgnize_flag in [['namewords', 'relationwords_two_single', 'namewords']]:
        flag = 1
    if orgnize_flag in [['namewords', 'namewords', 'relationwords_two_single']]:
        flag = 1
    if orgnize_flag in [['relationwords_two_single', 'namewords', 'namewords']]:
        flag = 2
    if orgnize_flag in [['namewords', 'v_prep', 'relationwords_two_single', 'namewords']]:
        flag = 1
    if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'relationwords_two_single']]:
        flag = 1
    if orgnize_flag in [['namewords', 'v', 'namewords', 'relationwords_two_single']]:
        flag = 1
    if orgnize_flag in [['namewords', 'v', 'relationwords_two_single', 'namewords']]:
        flag = 1
    if orgnize_flag in [['namewords', 'v','v_passive', 'relationwords_two_single', 'namewords']]:
        flag = 1
    if orgnize_flag in [['namewords', 'v','v_passive', 'namewords', 'relationwords_two_single']]:
        flag = 1
    if orgnize_flag in [['namewords', 'v_passive', 'relationwords_two_single', 'namewords']]:
                flag = 1
    if orgnize_flag in [['namewords', 'v_passive', 'namewords','relationwords_two_single', 'namewords']]:
        flag = 1
    if flag == 1:
        return [names[0], names[1], r_real, '1']
    if flag == 2:
        return [names[1], names[0], r_real, '1']

    return False


def buhe(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_false', 'v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'v_stop', 'v_prep', 'n']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_one':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)
    if r_word == '不和':
        if orgnize_mix in [['不和', 'namewords', 'namewords'], ['namewords', '不和', 'namewords']]:
            return False

    if orgnize_flag in [['namewords', 'v', 'namewords', 'v', 'relationwords_one'], ['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'v_passive', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'namewords''v_passive''relationwords_one', 'v', 'namewords', 'namewords', 'relationwords_one'], ['namewords', 'v', 'n', 'v_conj', 'namewords' ,'relationwords_one'], ['namewords', 'namewords', 'v', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_conj', 'namewords', 'v', 'relationwords_one'],  ['namewords', 'relationwords_one', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'relationwords_one'], ['namewords', 'v', 'namewords', 'relationwords_one', 'relationwords_one'], ['namewords', 'v', 'v_conj', 'namewords', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['v_false', 'namewords', 'namewords', 'relationwords_one'], ['v_conj', 'namewords', 'namewords', 'relationwords_one'], ['namewords', 'v', 'namewords', 'v', 'n', 'relationwords_one']]:
        return [names[0], names[1], r_real, '0']

    return False
def fenshou(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_false', 'v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'v_stop', 'n']:
            del words[loc]
#    words = remove_repeat(words)

    orgnize_flag = [flag for word, flag in words]

    if orgnize_flag in [['namewords', 'v', 'namewords', 'v', 'relationwords_one'], ['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'v_passive', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'namewords''v_passive''relationwords_one', 'v', 'namewords', 'namewords', 'relationwords_one'], ['namewords', 'v', 'n', 'v_conj', 'namewords' ,'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['v_false', 'namewords', 'namewords', 'relationwords_one'], ['v_conj', 'namewords', 'namewords', 'relationwords_one']]:
        return [names[0], names[1], r_real, '0']
    if orgnize_flag in [['namewords', 'namewords', 'v', 'relationwords_one'], ['namewords', 'v', 'namewords', 'relationwords_one'], ['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'v', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    return False

def zhuangshan(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords', 'v_conj']:
            del words[loc]
    orgnize_flag = [flag for word, flag in words]
    if len(names) == 2:
        if orgnize_flag in [['namewords', 'namewords', 'relationwords_one'],['namewords', 'namewords', 'relationwords_one'],['namewords',  'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'relationwords_one', 'namewords']]:
            return [names[0], names[1], r_real, '1']
    if len(names) == 3:
        if orgnize_flag in [['namewords', 'namewords', 'namewords','relationwords_one'], ['namewords', 'namewords', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'namewords', 'relationwords_one']]:
            return [names[0], names[1], r_real, '1'], [names[0], names[2], r_real, '1'], [names[1], names[2], r_real, '1']
    return False
def qingdi(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v', 'n', 'v_false']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_flag = [flag for word, flag in words]
    flag = 0
    if r_word == '情敌':
        if orgnize_flag in [['namewords', 'v_conj', 'v_special', 'namewords'], ['namewords', 'v_special', 'namewords', 'relationwords_one'], ['namewords', 'v_special', 'namewords', 'v_stop', 'relationwords_one'], ['namewords', 'namewords', 'v_special', 'relationwords_one']]:
            flag = 1
    if r_word == '前情敌':
        if orgnize_flag in [['namewords', 'relationwords_one', 'relationwords_one'], ['namewords', 'relationwords_one', 'v_prep', 'relationwords_one'], ['namewords', 'v_stop','relationwords_one', 'namewords'], ['namewords', 'v_stop','relationwords_one', 'v_prep', 'relationwords_one']]:
            flag = 1
        if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'relationwords_one'], ['namewords', 'v_prep', 'namewords', 'v_stop', 'relationwords_one']]:
            flag = 1
    if r_word == '昔日情敌':
        if orgnize_flag in [['relationwords_one', 'namewords', 'namewords'], ['relationwords_one', 'namewords', 'v_conj', 'namewords'], ['namewords', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_one']]:
            flag = 1
    if flag:
        return [names[0], names[1], r_real, '0']
    return False
def pengyou(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'n', 'v_false', 'v_stop']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_one':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)

    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_one', ], ['namewords', 'v_conj', 'namewords', 'v', 'v_prep', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v_stop', 'relationwords_one', 'namewords'], ['namewords', 'namewords', 'v', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v', 'relationwords_one'], ['namewords', 'namewords','relationwords_one'], ['namewords', 'relationwords_one', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v', 'v_conj', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v_prep', 'namewords'], ['namewords', 'v', 'relationwords_one', 'namewords'], ['namewords', 'v', 'namewords', 'relationwords_one'], ['namewords', 'v', 'namewords', 'v', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v', 'namewords'], ['namewords', 'v_conj', 'namewords', 'v', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'v', 'v_prep', 'relationwords_one'], ['namewords', 'v_prep', 'namewords', 'relationwords_one'], ['namewords', 'v_prep', 'namewords', 'v_stop', 'relationwords_one'], ['relationwords_one', 'namewords', 'namewords'], ['namewords', 'v', 'namewords', 'v_prep', 'v', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_one', 'namewords', 'v_conj', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_one', 'v', 'namewords'], ['namewords', 'namewords', 'v_conj', 'relationwords_one']]:
        return [names[0], names[1], r_real, '0']
    return False
def ouxiang(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'n', 'v_false', 'v_stop']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_flag = [flag for word, flag in words]



    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'v_conj', 'relationwords_two_single', 'namewords'], ['namewords', 'v', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'v', 'relationwords_two_single', 'v_prep', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_single', ], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_single']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'relationwords_two_single', 'v_prep', 'namewords'], ['namewords', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_single'], ['namewords', 'v_prep', 'namewords', 'relationwords_two_single'], ['namewords', 'v_prep', 'namewords', 'v_stop', 'relationwords_two_single']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_single', 'namewords'], ['namewords', 'namewords', 'v_conj', 'relationwords_two_single'], ['namewords', 'v', 'relationwords_two_single', 'namewords']]:
        return [names[0], names[1], r_real, '0']
    if orgnize_flag in [['namewords',  'v_conj', 'namewords', 'relationwords_two_single']]:
        return [names[0], names[1], r_real, '0']
    return False
def guimi(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_false', 'v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'v_stop', 'n']:
            del words[loc]
#    words = remove_repeat(words)

    orgnize_flag = [flag for word, flag in words]

    if orgnize_flag in [['namewords', 'v', 'namewords', 'v', 'relationwords_one'], ['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'v_passive', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'namewords''v_passive''relationwords_one', 'v', 'namewords', 'namewords', 'relationwords_one'], ['namewords', 'v', 'n', 'v_conj', 'namewords' ,'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['nameword', 'v', 'relationwords_one', 'namewords'], ['namewords', 'relationwords_one', 'v_prep', 'namewords'], ['relationwords_one', 'namewords', 'v', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_one', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v_conj', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_one', 'namewords', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_conj', 'relationwords_one', 'namewords']]:
        return [names[0], names[1], r_real, '1']

    if orgnize_flag in [['namewords', 'relationwords_one', 'v', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['v_false', 'namewords', 'namewords', 'relationwords_one'], ['v_conj', 'namewords', 'namewords', 'relationwords_one']]:
        return [names[0], names[1], r_real, '0']
    if orgnize_flag in [['namewords', 'namewords', 'v', 'relationwords_one'], ['namewords', 'v', 'namewords', 'relationwords_one'], ['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v', 'v_conj', 'namewords', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'v', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    return False
def laoxiang(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'n', 'v_false', 'v_stop']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_one':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)

    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_one', ], ['namewords', 'v_conj', 'namewords', 'v', 'v_prep', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_conj', 'relationwords_one', 'namewords'], ['v_conj', 'namewords', 'relationwords_one', 'namewords'], ['namewords', 'v', 'v_prep', 'namewords', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_one', 'namewords', 'v_prep', 'namewords'], ['namewords', 'v_prep', 'relationwords_one', 'namewords'], ['relationwords_one', 'namewords', 'v', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'relationwords_one'], ['namewords', 'v_stop', 'relationwords_one', 'namewords'], ['namewords', 'namewords', 'v', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v', 'relationwords_one'], ['namewords', 'namewords','relationwords_one'], ['namewords', 'relationwords_one', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v', 'v_conj', 'namewords', 'v_prep', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v_prep', 'namewords'], ['namewords', 'v', 'relationwords_one', 'namewords'], ['namewords', 'v', 'namewords', 'relationwords_one'], ['namewords', 'v', 'namewords', 'v', 'relationwords_one'], ['namewords', 'v', 'relationwords_one', 'v', 'namewords'], ['namewords', 'v_conj', 'namewords', 'v', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'v', 'v_prep', 'relationwords_one'], ['namewords', 'v_prep', 'namewords', 'relationwords_one'], ['namewords', 'v_prep', 'namewords', 'v_stop', 'relationwords_one'], ['relationwords_one', 'namewords', 'namewords'], ['namewords', 'v', 'namewords', 'v_prep', 'v', 'relationwords_one'], ['namewords', 'v_conj', 'namewords', 'relationwords_one']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_one', 'namewords', 'v_conj', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_one', 'v', 'namewords'], ['namewords', 'namewords', 'v_conj', 'relationwords_one']]:
            return [names[0], names[1], r_real, '0']

    return False
def feiwennvyou(words, r_word, r_real):
    words = words + []
    names = []
    if words[0][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + ['v_conj']:
        del words[0]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] == 'namewords':
            names.append(words[loc][0])
        if words[loc][1] in ['v_special', 'n', 'v_stop']:
            del words[loc]
#    words = remove_repeat(words)
    orgnize_mix = []
    orgnize_flag = []
    for word, flag in words:
        orgnize_flag.append(flag)
        if flag == 'relationwords_two_double':
            orgnize_mix.append(flag)
        else:
            orgnize_mix.append(word)

    #    if orgnize_flag in [['namewords', 'namewords', 'v_prep', 'relationwords_two_double'], ['namewords', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_double', ], ['namewords', 'v_conj', 'namewords', 'v', 'v_prep', 'relationwords_two_double']]:
    #        return [names[0], names[1], r_real, '1']
    #    if orgnize_flag in [['namewords', 'v', 'v_conj', 'namewords', 'v_prep', 'relationwords_two_double']]
    #        return [names[0], names[1], r_real, '1']
    #    if orgnize_flag in [['namewords', 'v', 'namewords', 'v_prep', 'relationwords_two_double']]:
    #        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'relationwords_two_double', 'v_prep', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v_prep', 'namewords', 'v_stop', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    #    if orgnize_flag in [['namewords', 'namewords', 'v', 'v_prep', 'relationwords_two_double']]:
    #        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v_conj', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'v_conj', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_two_double', 'namewords', 'v', 'namewords']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'namewords', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['namewords', 'v', 'namewords', 'relationwords_two_double']]:
        return [names[1], names[0], r_real, '1']
    if orgnize_flag in [['v_conj', 'namewords', 'relationwords_two_double', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['relationwords_two_double', 'namewords', 'namewords']]:
        return [names[0], names[1], r_real, '1']
    if orgnize_flag in [['namewords', 'relationwords_two_double', 'v', 'namewords'], ['namewords', 'namewords', 'v_conj', 'relationwords_two_double']]:
        return [names[0], names[1], r_real, '0']
    
    
    return False

find_func = {'传闻不和': buhe, '暧昧': buhe, '分手': fenshou, '同居': fenshou, '昔日情敌': qingdi, '朋友': pengyou, '同学': pengyou, '老乡': laoxiang, '闺蜜': guimi, '撞衫': zhuangshan, '同为校花': fenshou, '翻版': fanban, '经纪人': jingjiren, '偶像': ouxiang, '绯闻女友': feiwennvyou,'老师': feiwennvyou, '前女友': feiwennvyou, '妻子': feiwennvyou, '前妻': feiwennvyou, '绯闻男友': feiwennvyou,'学生': feiwennvyou, '前男友': feiwennvyou, '丈夫': feiwennvyou, '前夫': feiwennvyou, '配偶': pengyou}
def mate(words, news):
    words = words + []
    useful_locs = []
    r_word = ''
    r_real = ''
    r_loc = 0
    words_only = []
    names = []
    for i in range(0, len(words)):
        words_only.append(words[i][0])
        if words[i][1] in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double']:
            useful_locs.append(i)
            r_word = words[i][0]
            r_loc = i
            r_real = [cur for cur in db.relationship_keywords.find({'keywords': r_word})][0]['name'].encode('utf-8')
        if words[i][1] in ['namewords']:
            useful_locs.append(i)
            names.append(words[i][0])
    if r_real in ['妻子', '丈夫', '配偶']:
        if '《' in words_only:
            return [names[0], names[1], r_real, '0']
        if '》' in words_only:
            return [names[0], names[1], r_real, '0']
        if '<' in words_only:
            return [names[0], names[1], r_real, '0']
        if '>' in words_only:
            return [names[0], names[1], r_real, '0']
        if r_loc < len(words) - 1:
            if words_only[r_loc+1] in ['"', '"', '“', '”']:
                return [names[0], names[1], r_real, '0']
        if r_loc > 0:
            if words_only[r_loc-1] in ['"', '"', '“', '”']:
                return [names[0], names[1], r_real, '0']
    start = useful_locs[0]
    stop = useful_locs[-1]
    if start > 0:
        start = start - 1
    words = words[start:stop+1]
    length = len(words)
    for i in range(0, length):
        loc = length - i - 1
        if words[loc][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords'] + main_features:
            del words[loc]
    remove_repeat(words)
    return find_func.get(r_real)(words, r_word, r_real)






def remove_repeat(words):
    words = words + []
    length = len(words)
    if length > 4:
        for i in range(0, length):
            loc = length - i -1
            if loc > 0:
                if words[loc][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords']:
                    if words[loc][1] == words[loc-1][1]:
                        del words[loc]
    length = len(words)
    if length > 5:
        for i in range(0, length - 2):
            loc = length - i - 3
            if loc > 0:
                if words[loc+2][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords']:
                    if words[loc+1][1] not in ['relationwords_one', 'relationwords_two_single', 'relationwords_two_double', 'namewords']:
                        tag = 1
                        if len(words) > loc:
                            if [words[loc+2][1],words[loc+1][1]] == [words[loc][1],words[loc-1][1]]:
                                del words[loc+2]
                                del words[loc+1]
                                tag = 0
                            if tag:
                                if [words[loc][1], words[loc+1][1],words[loc+2][1]] in [['n', 'v', 'n'], ['v', 'n', 'v']]:
                                    words[loc][1] = 'v'
                                    words[loc+1][1] = 'n'
                                    del words[loc+2]
    return words







#def mate(words, news):
#    words_initial = words + []
#    words_mate = cut_false_news(words_initial)
#    if words_mate:
#        return find_func.get(words_mate[2])(words_mate[0], words_mate[1], words_mate[2])
#    return False
def mate_test(words, news):
    words_initial = words + []
    words_mate = cut_false_news(words_initial)
    if words_mate:
        results = find_func.get(words_mate[2])(words_mate[0], words_mate[1], words_mate[2])
        return results
        if results == False:
            s = ''
            for word, flag in words_mate[0]:
                s = s + flag + ' '
            print s
            print news
        else:
            return results
    return False
def test_mate():
#比较高传闻不和
#％50偶像，分手，同居
#%30同学
#前女友，前妻，同为校花
    rel_list = ['暧昧', '传闻不和', '翻版', '绯闻女友', '分手', '闺蜜', '经纪人', '老师', '老乡', '偶像', '朋友', '妻子', '前女友', '前妻', '同居', '同为校花', '昔日情敌', '同学', '撞衫']
    for r in rel_list:
#        if r == '绯闻女友':
        k = 0
        line_list = open('/Users/wutong/workspace/da/baidu/data/condensedata/traindatacategory/' + r + '/1').readlines()
        for line in line_list:
            results = line.split()
            news = results[3]
            names = [results[1], results[2]]
            words_cut = cutnews.cut_news(news, names)
            if words_cut:
                words_mate = mate_test(words_cut[0], news)
                if words_mate:
                    k = k + 1
        print r, '=', k, ':', len(line_list)
if __name__ == '__main__':
    test_mate()


                     
        
        
        

