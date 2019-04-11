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
