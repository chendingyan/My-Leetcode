# 这道题上课讲过， 很简单， 但是关键是 如何更方便的实现
# open close list如果设置成两个list 要写一个match函数 比较麻烦
# 更快的是使用dictionary
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"]": "[", "}": "{", ")": "("}
        stack = []
        for i in s:
            if i in dict.values():
                stack.append(i)
            if i in dict.keys():
                if stack == [] or dict[i] != stack.pop():
                    return False
        return stack == []

