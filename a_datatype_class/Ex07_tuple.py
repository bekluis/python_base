"""
#----------------------------------------------------------
[튜플 자료형]    파이썬에만 있음
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1,2,3,1)
print(t)
print(t[1])

print('------------------- 2 -----------------')
# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0
# del t[1]
# del t         가능


'''
    - list
        a = list()
        a = []
    - set
        b = set()
        b = {}
    - tuple
        c = tuple()
        c = ()
'''

# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')

# t = 1,2,3,1    # 괄호 없는거 권장하지 않음 -> 반드시 튜플 () 표시하기
# print(type(t))
# print(t[1])


t = (9)
print(t)
print(type(t))


t = (9,) # *********************
print(t)
print(type(t))




# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
print(t2[0])
print(t + t2)
print(t * 3)


