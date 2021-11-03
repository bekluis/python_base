# Ex02.py
data = []

try:
    with open('./dream.txt','r',encoding='utf-8') as f:
        while True:
            con = f.readline()                      # 먼저 읽어주고
            if not con : break                      # 그 다음 if문 돌리기
            data.append(con)

        # print(contents)



except FileNotFoundError as e :
    print('파일을 찾을 수 없음 - ', e)
else :
    for idx,i in enumerate(data):
        print(str(idx) + '---' + i)

finally:
    print('')



# f = open('dream.txt')
# line = f.readline()
# line[:2]

        # f.close()
        # for i in range(0,5):
        #     print(str(i)+contents)
        # num = range(0,5)
        # print('%d---%s' % (num,contents))