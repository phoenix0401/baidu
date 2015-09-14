#--*--coding: utf8--*--
import mate
def single_relationship(words, news):
    return mate.mate(words, news)
#
#    names = words
#    names_relative_location = []
#    results = []
#    r = ''
#    for i in range(0, len(words)):
#        flag = words[i][1]
#        if flag == ['relationwords_one', 'relationship_two_single', 'relationwords_two_double']:
#            rel_loc = i
#            r = words[i][0]
#            r_real = convert_real_relword(r)
#            names_location.append(i)
#        if flag == 'namewords':
#            names_location.append(i)
#            names_relative_location.append(i)
#    if len(names_location) - 1 > 2:
#        for loc in range(0, len(names_location)):
#        for loc in names_location:
#            words_mid = words + []
#            words_mid[names_location][1] = 'nr'
#            w_orgnize = cutnews.cut_false_news
#        
#        for loc in range(0, len(names_location)):
#            tag_rel = names_location.index(rels_location[0])
#            tag_judge = 0
#            if tag_rel == 0:
#                 tag_judge = 1
#            if tag_rel == 1:
#                if loc ==0:
#                    tag_judge = 1
#            name_words = [] + words
#            if names_location[loc] not in rels_location:
#                if loc == 0:
#                    i = 0
#                else:
#                    i = names_location[loc - 1] + 1
#                j = names_location[loc]
#                w_initial = cut_location(i, j, name_words)
#                w_false = cutnews.cut_false_news(w_initial)
#                w_orgnize = getfalseorgnize.get_false_orgnize_item(w_false)
#                a_list = [0, 1, 2]
#                a_list.remove(names_relative_location.index(j))
#                mid = ([r_real] + a_list + ['0'], [r_real] + a_list + ['1'])
#                if tag_judge:
#                    results.append([r_real] + a_list + ['0'])
#                else:
#                    if (w_orgnize[0] in false_orgnize) | (w_orgnize[1] in false_orgnize) | (w_orgnize[2] in false_orgnize):
#                        if mid[0] not in results:
#                            results.append([r_real] + a_list + ['0'])
#                    else:
#                        if mid[1] not in results:
#                            results.append([r_real] + a_list + ['1'])
#    else:
#        w_false = cutnews.cut_false_news(words)
#        w_orgnize = getfalseorgnize.get_false_orgnize_item(w_false)
#        a_list = [0, 1]
#        mid = ([r_real] + a_list + ['0'], [r_real] + a_list + ['1'])
#        if (rels_location[0] < names_location[0]) & (rels_location[0] < names_location):
#            results.append([r_real] + a_list + ['0'])
#        else:
#            if (w_orgnize[0] in false_orgnize) | (w_orgnize[1] in false_orgnize) | (w_orgnize[2] in false_orgnize):
#                if mid[0] not in results:
#                    results.append([r_real] + a_list + ['0'])
#            else:
#                if mid[1] not in results:
#                    results.append([r_real] + a_list + ['1'])
##results/[r_real] + a_list + ['0']
#    return results
def compound_relationship(words):
    pass
#    rels_location = []
#    names_location = []
#    results = []
#    for i in range(0, len(words)):
#        flag = words[i][1]
#        if flag == 'relationwords':
#            rels_location.append(i)
#            names_location.append(i)
#        if flag == 'namewords':
#            names_location.append(i)
#    rels_location_relative = []
#    words_split_to_list = []
#    for loc in range(0, len(names_location)):
#        i_loc = names_location[loc]
#        if loc == 0:
#            if i_loc == 0:
#                words_split_to_list.append([words[0]])
#            else:
#                words_split_to_list.append(words[0:i_loc])
#        else:
#            words_split_to_list.append(words[names_location[loc-1]:i_loc])
#    for i in rels_location_relative:
#        relative = rels_location_relative + []
#        relative.remove(i)
#        rels_words = [] + words
#        relative.reverse()
#        for j in relative:
#            del rels_words[j]
#        results.append(single_relationship(rels_words))
