# -*- coding:utf-8 -*-
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)<=0:
            return []
        res = []
        path = ''
        res = self.Helper(ss, res, path)
        #接下来要去除重复部分
        res = list(set(res))
        res = sorted(res)
        return res

    def Helper(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.Helper(ss[:i]+ss[i+1:], res, path+ss[i])
        return res
sol = Solution()
print(sol.Permutation('aa'))
