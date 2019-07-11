# -*- coding:utf-8 -*-
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if 'e' in s:
            #如果有e
            s.split('e')
            

    def isNumber(self, s):
        pass


s = '1e-14'
print('E' in s)
# 有e 还可以有+ - 号 不能有小数点 不能使最后一个
# 有+ - 不能同时有 + -后面要有数字 只能在第一个
# 有小数点 小数点不能是最后一个

str = s.split('e')
print(str)