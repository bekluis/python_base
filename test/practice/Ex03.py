# Ex03.py
def fileopen(data):

    with open('./dream.txt','r',encoding='utf-8') as f:

        contents = f.read()
        splitdata = contents.split()

    return  splitdata, len(splitdata)

def count_character(data):

        count = 0
        for i in data :
            count += len(i)
        return count




data,count = fileopen('dream.txt')



print("글자수 : ", count_words(data))
print("공백을 제외한 문자수 : ", count_character(data))
print("단어 수: ", count)