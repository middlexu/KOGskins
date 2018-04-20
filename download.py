# -*- encoding: utf-8 -*-

import requests
import json

with open('herolist.json', 'r', encoding='utf-8') as f:
    herolist = json.load(f)

for hero in herolist:
    print(hero['ename'], hero['cname'], hero['skin_name'])
    skin_list = hero['skin_name'].split('|')
    for i in range(len(skin_list)):
        url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(hero['ename'],hero['ename'],i+1)
        result = requests.get(url)
        with open('skins/'+hero['cname']+skin_list[i]+'.jpg', 'wb') as f:
            f.write(result.content)


