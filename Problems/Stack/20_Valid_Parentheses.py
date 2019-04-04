# 这道题上课讲过， 很简单， 但是关键是 如何更方便的实现
# open close list如果设置成两个list 要写一个match函数 比较麻烦
# 更快的是使用dictionary
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_list = ['(','{','[']
        close_list = [')','}',']']
        stack = []
        for i in s:
            if i in open_list:
                stack.append(i)
            if i in close_list:
                if i != stack.pop():
                    return False
        return True

    def match(self, x, y):
        for i in range(3):
            if x ==
def main():
    s = '[]'
    s = str(s)
    sol = Solution
    sol.isValid(s)

if __name__ == '__main__':
    main()