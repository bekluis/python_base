msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리


# (1) unpacking : 각 요소를 분해(풀기)
a, b, c =  li
print(a)
print(b)
print(c)

# (2) enumerate() 함수 : 각 요소와 인덱스를 같이 추출
user_list = ['개발자','코더','전문가','분석가']
for value in user_list :
    print(value)

for value in enumerate(user_list) :
    print(value[0], ':', value[1])

for idx,value in enumerate(user_list) :
    print(idx, ':', value)



# (3) zip()
days = ['월','화','수']
doit = ['잠자기','공부','놀기','밥먹기']

print(list(zip(days, doit)))
print(dict(zip(days, doit)))

def test(x, y):
	tmp = x
	x = y
	y = tmp
	return y.append(x)

x = ["y"]
y = ["x"]

test(x,y)
print(y)