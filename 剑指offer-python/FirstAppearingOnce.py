# -*- coding:utf-8 -*-
# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
class Solution:
    # 返回对应char
    def __init__(self):
        self.str = dict()
        self.queue = []
    def FirstAppearingOnce(self):
        # write code here
        while self.queue and self.str[self.queue[0]] != 1:
            self.queue.pop(0)
        if not self.queue:
            return '#'
        else:
            return self.queue[0]

    def Insert(self, char):
        # write code here
        if char in self.str:
            self.str[char]+=1
        else:
            self.str[char] = 1
            self.queue.append(char)

sol =Solution()
sol.Insert('h')
print(sol.FirstAppearingOnce())

sol.Insert('e')
print(sol.FirstAppearingOnce())

sol.Insert('l')
print(sol.FirstAppearingOnce())

sol.Insert('l')
print(sol.FirstAppearingOnce())

sol.Insert('o')
print(sol.FirstAppearingOnce())

sol.Insert('w')
print(sol.FirstAppearingOnce())

print(sol.FirstAppearingOnce())
