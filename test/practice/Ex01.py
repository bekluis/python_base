

try:

    with open('./sample.txt','r',encoding='utf-8') as f:         #close를 안해도 된다

        contents = f.read()
        print(contents)                         #모든 내용


        sum =
        num = len(words)

except FileNotFoundError as e:
    print('파일을 찾을 수 없음 - ',e)
else:
    print('총합 :',f.name,',평균값:', num)
    # f.close()
finally:
    print('종료')