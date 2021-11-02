"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""
try:
 #   f = open('./data/data.txt','r',encoding='utf-8')                    # 상대경로
 #   f = open('/python/aBasic_1/e_file_class/data/.data.txt', 'r', encoding='utf-8')                  # 절대경로


    with open('./data/data.txt','r',encoding='utf-8') as f:         #close를 안해도 된다
        # while True:
        #     line = f.readline()
        #     if not line: break
        #     print(line, end='')                 #반복문을 벗어남

        contents = f.read()
        print(contents)                         #모든 내용
        words = contents.split()
        print(words)                            #쪼개기
        num = len(words)

except FileNotFoundError as e:
    print('파일을 찾을 수 없음 - ',e)
else:
    print('파일명:',f.name,',총 단어수:', num)
    # f.close()
finally:
    print('종료')





