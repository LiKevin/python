# -*- coding: utf-8 -*-
__author__ = 'k22li'


t = '''/“/请/！/”/“/请/！/”/两名/剑士/各自/倒转/剑尖/，/右手/握/剑柄/，
/左手/搭于/右手/手背/，/躬身行礼/。/两/人/身子/尚未/站/直/，
/突然/间/白光闪/动/，/跟着/铮的/一/声响/，
/双剑相/交/，/两/人/各/退一步/。
/旁/观众/人/都/是/“/咦/”/的/一声/轻呼/。/青衣/剑士/连/劈/三/剑/'''

t_list = t.split('/')

#print t_list

new_dict = {}
for item in t_list:

    if item not in new_dict:
        new_dict.update({item : 1})
    else:
        new_dict[item] += 1

new_list = [ (k, new_dict[k]) for k in new_dict if new_dict[k] != 1 ]

for item in new_list:

    print item[0].decode('utf-8'), ' --> ', item[1]