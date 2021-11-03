""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""
def count_words(filename):
    try :
        f = open('./data/'+filename, 'r', encoding='utf-8')
    except FileNotFoundError as e:
        print('%s 파일이 존재하지 않습니다 에러코드는 %s' % (filename, e))
    else :
        v = f.read().split()
        num = len(v)
        print('%s 파일의 글자수 %d 입니다' % (filename, num))
        f.close()



# 존재하지 않는 파일명도 있음
filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames:
    count_words(filename)

# sentence = list("Hello Gachon")
# print(len(sentence) +1 )


# try:
#
#     for i in range(1, 7):
#
#         result = 7 // i
#
#         print(result)
#
# except ZeroDivisionError:
#
#     print("Not divided by 0")
#
# finally:
#
#     print("종료되었습니다.")


# sentence = list("Hello Gachon")
#
# while (len(sentence) + 1):
#
#     try:
#
#         print(sentence.pop(0))
#
#     except Exception as e:
#
#         print(e)
#
#         break


# for i in range(3):
#
#     try:
#
#         print(i, 3// i)
#
#     except ZeroDivisionError:
#
#         print("Not divided by 0")

# with open('i_have_a_dream.txt','r',encoding='utf-8') as f:
#
#     contents = f.read()
#     print(contents)
    # f.close()             #close 쓰지 않을 경우
