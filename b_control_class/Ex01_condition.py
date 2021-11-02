"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생 (들여쓰기)

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass (아무것도 명령하지 않는다)
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}       # 딕셔너리
i10=None


a = -1
if a:
    print('True')       #True
else:
    print('False')    #


if not a:
    print('True2')      #


#-------------------------------------------
# 2) 논리연산자 이용
a = 10
b = -1
if a and b:
    print('True3')      #True
else :
    print('False3')

if a or b:
    print('True4')      #True
else :
    print('False4')


print( a and b )  # b   마지막 나오는 값에 의해서 결정
print( a or b )   # a   가장 먼저 나온 값에 의해서 이미 결정



#-----------------------------
# (3)

a = 10
if a:
    c = 2
elif b:
    c = 4
else:
    c = b

print(c)  # 2
