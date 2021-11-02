
# [추가] 함수도 객체이다
def case1():
    print('case-1')

def case2():
    print('case-2')

def case3():
    print('case-3')

# case1()
f = { 'a1' : case1, 'a2' : case2, 'a3' : case3 }
print(f['a1'])
f['a1']()


#---------------------------------------
# 글로벌 변수와 지역변수

# (1)
# temp = '글로벌'
#
# def func():
#     print('1>', temp )
#
# func()
# print('2>', temp)

# (2)
# temp = '글로벌'
#
# def func():
#     # print('0>', temp)            #
#     temp = '지역'                 # 이 블록안에서만 사용 가능
#     print('1>', temp )   # 지역
#
# func()
# print('2>', temp)  # 글로벌


# (3)
temp = '글로벌'

def func():
    #global temp
    temp = '지역'                 # 변수가 다른데 아래 변수를 쓰고 싶을때
    print('1>', temp )     # 지역

func()
print('2>', temp)  # 글로벌



'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''
def f(x, y):        # 일반 함수
    return x+y
print( f(3,2))


f = lambda x, y : x+y       # 위랑 같은 코드
print( f(3,2))


#-----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""

# (1) map()
def cal(x):
    return x*2
data = [1,2,3,4,5]              # 집합 list, set, tuple 가능

result = list(map(cal, data))
print(result)

# (2) reduce()
from functools import reduce            #이전 값과 맞물려 가는 통합 개념, 인자 2개    1x2, 2x3, 6x4...
def cal(x, y):
    return x*y
data = [1,2,3,4,5]

print(reduce(cal, data))


number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])




