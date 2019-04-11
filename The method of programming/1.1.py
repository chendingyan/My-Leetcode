# abcdef -> defabc
def solution(str):
    str1 = str[:3]
    str2 = str[3:]
    print(str1, str2)
    str1 = str1[::-1]
    str2 = str2[::-1]
    str = str1 + str2
    return str[::-1]


str = 'abcdef'
string = solution(str)
print(string)

# I am a student -> student. a am I
# list.reverse()与 join两个函数
def solution2(str):
    ans =[]

    strings = str.split(' ')
    print(strings)
    strings.reverse()
    print(strings)
    ans = ' '.join(strings)

    return ans


str = 'I am a student.'
string =solution2(str)
print(string)