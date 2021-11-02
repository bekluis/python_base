# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사





"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False


if('아'):
    print('True')
else:
    print('False')

if([]):
    print('True2')
else:
    print('False2')
"""



hungry = True
sleep = False

print( type(hungry) )
print( hungry )
print( not hungry )
print( hungry and sleep )
print( hungry & sleep )
print( hungry or sleep)

# 실행결과
'''
<class 'bool'>
True
False
False
False
True
'''

