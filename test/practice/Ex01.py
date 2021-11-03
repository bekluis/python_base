
try:
    with open('./sample.txt','r',encoding='utf-8') as f:

        contents = f.read()
        word = contents.split()


except FileNotFoundError as e:
    print('파일을 찾을 수 없음 - ',e)
else:
    f.close()

# print(word)

sum = 0
for i in word:
    sum = sum + int(i)
    # print(sum)

result = ["sum : " + str(sum), "avg : " + str(sum//len(word))]
with open('./result.txt','w',encoding='utf-8') as f:
    for i in result:
        f.write(i + "\n")

# try:
#
#     with open('./sample.txt','r',encoding='utf-8') as f:         #close를 안해도 된다
#
#         contents = f.read()
#         print(contents)                         #모든 내용
#
#
#
#
# except FileNotFoundError as e:
#     print('파일을 찾을 수 없음 - ',e)
# else:
#     print('총합 :',f.name,',평균값:', num)
#     # f.close()
# finally:
#     print('종료')


    # score=[]
    # sum = 0
    # for i in score:
    #     sum+=i
    # print('점수 총합은',sum,'입니다.')
    #
    # score=[]
    # sum = 0
    # for i in score:
    #     sum += i
    # print(sum//4)