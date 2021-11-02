# Ex03_json_exam.py

'''
    sample.json 파일을 읽어서 총 과일의 금액을 출력하기
'''

import json

with open('./data/sample.json','r',encoding='utf-8') as f:
    data = f.read()


items = json.loads(data)

for k, v in items.items():

    print(k, '>>>>', v)
    print(v['price'])
    print(v['count'])
    print(v['price']*v['count'])


