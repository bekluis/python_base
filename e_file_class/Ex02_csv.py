# Ex02_csv.py
# CSV : common string value

#파이썬에서 csv 쓰려면

import csv

#1. 리스트의 데이터를 csv로 저장하기
# data = [[1,'김','책임'],[2,'박','선임'],[3,'맹','연구원']]
#
# with open('./data/imsi.csv','wt',encoding='utf-8') as f:
#     cout = csv.writer(f)
#     cout.writerows(data)




#2. csv로 저장된 파일을 읽어서 리스트 저장하기
result = []
with open('./data/imsi.csv','rt', encoding='utf-8') as f:
    cin = csv.reader(f)
    result = [row for row in cin if row]        #cin을 row로 하나씩 뽑아넣어주고 만약 row일때 row row아닐때 넣지 않는다

print(result)
