# 给定一个长字符串A和一个短字符串B，判断B的所有字符是不是都在A中
# 方法1：每个都检查过去
# 复杂度 O(m * n)
def stringCotain1(str1, str2):
    count = 0
    str1 = set(str1)
    str2 = set(str2)

    for char in str2:
        for char2 in str1:
            if char == char2:
                count+=1
    if count == len(str2):
        return True
    else:
        return False

# 来一个牛逼方法
# hash table法
def stringContain2(str1, str2):
    pass




str1 = 'acaadbefg'
str2 = 'aab'
print(stringCotain1(str1, str2))
# set = set(str1)
# list = list(set)
# list.sort()
# print(list)