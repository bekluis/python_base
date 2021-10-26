"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

# name = input('이름을 입력하세요')
# print('당신은', name, '입니다')
# %를 활용하여 출력
# format() 활용하여 출력


#
# print("당신의 이름은 {0}입니다.".format(name))
# print("당신의 이름은 %s입니다." %(name))


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input('나이 입력'))
# print('당신의 나이는', age+1)
#
# height = float(input('키 입력'))
# print('당신의 키는', height)
#
# print('1+2')
# print(eval('1+2'))




#----------------------------------
# 단을 입력받아 구구단을 구하기

# dan = int(input('단 입력'))
# for i in range(1,10):
#     print(format(dan),'X',i,'=',(dan*i))
#





#-----------------------------------------
# print() 함수

# print('안녕' + '친구')
# print('안녕' , '친구')
# print('안녕'   '친구')
#
# for i in range(10):
#     print(i)
#
# for i in range(1,10):
#     print(i)
#
# for i in range(1,10,3):
#     print(i, end=',' if i<5 else "")  # 1,4,


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3


# alist = []
# sum = 0
# for i in range(5):
#     i = int(input("정수를 입력해주세요: "))
#     alist.append(i)
#     sum+=i
#
# avg = sum/len(alist)
# print(avg)


# b = input('문자열입력 : ')
# print('결과 :' , b[::-1])


# b = input('문자열을 입력하세요')
# print('결과 : ' , b[::-1])


# import numpy
# abc = [10, 20, 30, 40, 50]
# abc = input('정수리스트 입력 : ').split()
# avg2 = numpy.mean(abc)
# print('평균 : ', avg2)
# var2 = numpy.var(abc)
# print('분산 :', var2)
# std2 = numpy.std(abc)
# print('표준편차 : ', std2)

# import numpy
# inArr = []
# for i in range(5):
#     # inArr.append(int(input('number')))
#     print(numpy.std(inArr))

totalScore = 0

for i in range(5):
    score = int(input("점수를 입력하세요 : "))
    totalScore += score

sum = totalScore/5
print("평균 = %.1f" % (sum))


# phone = [[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],
#          ['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
# string = input('문자열을 입력하시오')
# result = ''
# for char in string:
#     for i in range(len(phone)):
#         if char.upper() in phone[i]:
#             result += str(i + 1)


totalScore = 0

for i in range(5):
    score = int(input("점수를 입력하세요 :"))
    totalScore += score

sum = totalScore/5
print("평균 = %.1f" % (sum))



