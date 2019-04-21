# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        children = [i for i in range(0,n)]
        pop_pos = 0
        while len(children) >1:
            pop_pos = (pop_pos + m-1) % len(children)
            children.pop(pop_pos)
        return children[0]

sol = Solution()
print(sol.LastRemaining_Solution(6,7))

# 0 1 2 3 4 --- pop = 1 pos = 2
# 0 2 3 4 ---- pop = 2 pos = 3
# 0 2 4 --- pop = 0 pos =1
# 2 4 --- pop =