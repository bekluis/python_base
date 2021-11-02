"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""


# (0) 인자도 없고 리턴값도 없는 함수
def func():
    print('inside function')

func()
result = func()
print(result)




# (1) 리턴값이 여러개인 함수 ==> 튜플 하나로 리턴됨
def func(args):         # 10
    return args+1, args-1       # 11,9

result = func(10)
print(result)

first, second = func(10)
print(first + second)


def func(args):
    return args+1, args-1


third, firth = func(10)
print(third + firth)


# (2) 위치인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!!!', name, '님')

# func('하이','백길동')
# func('김길동','안녕')



# (3) 키워드 인자 (keyword argument)
func(name='김길동2',greeting='안녕2')


# (4) 매개변수의 기본값
# func('올라','세뇨라','바이')

def func(greeting, name ="아무개"):
    print(greeting, '!!!!!', name, '님')

func('올라')
func('올라','김길동')

def method(a, b, c=100):
    return a+b+c
print(method(1,2,3))            # c=3으로 덮어줌
print(method(c=1,b=2,a=3))      #c 100이 없어지고
print(method(10,20))        # a=10, b=20, c=100





'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''

def func(a, b, c=0, *args):  # for구문을 args에 묶음
    sum = a + b + c
    for i in args:
        sum += i
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))



#-----------------------------------------------
# (6) 키워드 인자 모으기 (**)


def func(a, b, c=0, *args, **kwargs):
    sum = a + b + c
    for i in args:
        sum += i
    for k in kwargs:
        sum += kwargs[k]
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(1,2,3, kor=100, math=50))
print(func(1,2, kor=50, math=60, eng=40))
print(func(1,2, kor=50, java=40))














