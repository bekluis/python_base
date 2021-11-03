# Ex03.py
data = []

def fileopen(data):

    with open('./dream.txt','r',encoding='utf-8') as f:

        contents = f.read()
        splitdata = contents.split()
        data.append(splitdata)

    return  splitdata, len(splitdata)

def count_character(data):

    count = 0
    for i in data :
        count += len(i)
    return count

def count_sentence(data):

    count = 0
    while True:
        if data.readline()=='':break
        count += 1
    return count

data,count = fileopen('dream.txt')


print("총 글자수 : ", count_character(data))
print("총 단어의 수: ", count)
print("총 줄의 수: ", count_sentence(data))