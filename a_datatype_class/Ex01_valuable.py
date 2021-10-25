"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + ctrl + F10

    [도움말] ctrl + q

@ 파이썬 자료형
1. 기본자료형
    ' 숫자형( 정수형 int/ 실수형 float )
    ' 문자형
    ' 논리형
    ' 날짜형

2. 집합자료형
    - list
    - tuple(*) : list와 유사, 값 변경 안됨
    - set
    - dictionary


    [ 참고 ] 자바의 Collection
        - List
        - Set
        - Map

"""

""" 여러줄 
주석 """

'''
여러줄 
주
석
'''



# 한줄 주석

# 문자열표시
print("헬로우")
print('hello')

print("""안녕""")
print('''올라''')
# 실행 : shift + ctrl + F10

'''
변수란
    파이션의 모든 자료형은 객체로 취급한다
    a = 7
            7 객체을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
'''

'''변수명으로 쓸 수 없는 키워드들'''

import keyword

print(len(keyword.kwlist))

print(keyword.kwlist)

a = 777
b = 777
print(id(a))
print(id(b))
# print(id(7))
print( a is b)



# 여러 변수 선언
a, b = 10, 20
print('a + b = ', a+b)

# 두 변수의 값을 바꿀 때
a, b = 10, 20
print('A=',a , ',B=', b)
a, b = b, a
print('A=',a , ',B=', b)

del b
# print('A=',a , ',B=', b)

print(c)





