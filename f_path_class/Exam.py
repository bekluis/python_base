pin = '880122-1234567'

birthday = pin[:6]

# if gender[7] in ['1','3'] :
#     print("남자")
# else :
#     print("여자")

gender = '남자' if pin.split('-')[1][0] == '1'else'여자'

# if in[7] == '1':
#     gender = '남자'
# else :
#     gender = '여자'

print('홍길동님 생년월일 :{}'.format(birthday))
print('성별 :{}'.format(gender))

#
# [출력결과]
# 홍길동님 생년월일 : 880122
# 성별 : 남자




#2. 리스트 [1,3,5,4,2] 값을 [5,4,3,2,1]로 만들어서 출력한다.              sort()- 정렬, reverse- 역순정렬
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# [출력결과]
# [5,4,3,2,1]



# 3. 리스트를 문자열로 만들어서 출력한다                ''.join()=띄어쓰기 없이  ' '.join()=띄어쓰기 추가
a = ['독도는','대한민국의','아름다운','섬입니다']
result = ' '.join(a)
print( result )

# [출력결과]
# 독도는 대한민국의 아름다운 섬입니다



# 4. 튜플 (1,2,3)에 4 값을 추가하여 (1,2,3,4)를 만들어 출력한다          튜플은 값이 수정이 안되니 리스트로 변환하고 append로 추가 후  튜플로 변환
a = (1,2,3)
# a_list = list(a)
# a_list = [1,2,3]
# a_list.append(4)
# a = tuple(a_list)
# print(a)
a = a + (4,)        #튜플 추가 간단한 방법 요소가 하나밖에 없는



# [출력결과]
# (1,2,3,4)


# 5. 아래 파이썬의 실행 결과를 확인하고 이런 결과가 나오는 이유에 대해 설명한다.
a = b = [1,2,3]
a[1] = 4
print(b)

# 리스트는 값 수정이 가능하기 때문에 [1, 4, 3]

# 6. while 문을 아래와 같이 출력되도록 작성한다. (배운 모든 언어로 풀어보기 자바, 자바스크립트, 파이썬)
# *
# **
# ***
# ****
# *****
#>>>>>>>>>>>>>>>>>>>>>>>>>>>
count = 1
while True:
    if( count == 6): break
    print('*' * count)
    count += 1






# 7. 우리반 학생들의 중간고사 점수는 아래와 같은데, 각각의 개인별 학생의 총점과 평균을 구해서 출력한다 (20점)
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]



def avg(a):
    sum = 0
    for i in midterm_score:                 # midterm_score 자료를 i에 하나씩 넣어준다
        sum += i[a]
    return sum // 3
for i in range(0, 5):
    print("{}번쨰 학생 평균 :".format(i + 1), avg(i))
def grade(a):
    sum = 0
    for i in midterm_score:
        sum += i[a]
    return sum
for i in range(0, 5):
    print("{}번쨰 학생 총점 :".format(i + 1), grade(i))




# 8. 이차원 딕셔너리 life를 만든다.
# 최상위 키는 'animal','plants','other'이다.
# 그리고 'animal'는 각각 'cats','octopi','emus'를 키로 하고,
# 'cats'의 값에는 'Kim','Lee','Choi'이다.
# 나머지 요소는 빈 딕셔너리를 참조한다 (20점)

life = {'animal': {'cats':('Kim','Lee','Choi')},'octopi':(),'emus':{},'plants':{},'other':{}}

life = {
            'animal' :  {
                        'cats' :  ('Kim','Lee','Choi')    ,
                        'octopi':     {}  ,
                        'emus' :      {}
            }    ,
            'plants' :   {}   ,
            'other'  :    {}
}



# all_thing = {
#     'animal': {
#         'cats': 'Kim','Lee','Choi',
#         'octopi':,
#         'emus':
# },
#     'plants': {
#
#     },
#
#     'othet': {}
#
# }
#
# print(all_thing['animal']['cats'])

# count = 1
# while True:
#     if(count == 6): break
#     print('*' * count)
#     count += 1

# life = {'animal': {'cats':('Kim','Lee','Choi')},'octopi':(),'emus':{},'plants':{},'other':{}}