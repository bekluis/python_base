# Ex03_json.py
# json 쓰고싶다

import json

with open('./data/temp.json','r',encoding='utf-8') as f:        #파일을 열고 읽는 것을 f로 별칭해주겠다
    data = f.read()                         #별칭으로 만들어준 f를 데이터라는 변수에 넣어주겠다
    print(data)

print('-'*50)
items = json.loads(data)
print(items)

print(type(data))
print(type(items))

for k, v in items.items():
    print(k, '>>>>', v)
    print(v['Job'])             #필요한 애들만 뽑아올 수 있게끔
