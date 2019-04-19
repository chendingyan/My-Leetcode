# -*- coding:utf-8 -*-
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）
# 我们可以定义哈希表的键值(Key)是字符的ASCII值，而值(Value)是该字符出现的次数。
# 同时我们需要扫描两次字符串，第一次扫描字符串时，每扫描到一个字符就在哈希表的对应项中把次数加1。
# 接下来第二次扫描的时候，没扫描到一个字符就能在哈希表中得到该字符出现的次数。
# 找出第一个Value为1的那个key就是我们需要找到那个字符。

# 为了实现hash table 可以用一个dict

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        queue = []
        hash = dict()
        for idx, char in enumerate(s):
            if char not in hash:
                queue.append(idx)
                hash[char] = 1
            else:
                hash[char]+=1

        while queue and hash[s[queue[0]]] != 1:
            queue.pop(0)
        if queue:
            return queue[0]
        else:
            return -1


sol = Solution()
s = 'google'
hash = sol.FirstNotRepeatingChar(s)
print(hash)