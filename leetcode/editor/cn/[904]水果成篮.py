# 在一排树中，第 i 棵树产生 tree[i] 型的水果。 
# 你可以从你选择的任何树开始，然后重复执行以下步骤： 
# 
#  
#  把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。 
#  移动到当前树右侧的下一棵树。如果右边没有树，就停下来。 
#  
# 
#  请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。 
# 
#  你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。 
# 
#  用这个程序你能收集的水果树的最大总量是多少？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,1]
# 输出：3
# 解释：我们可以收集 [1,2,1]。
#  
# 
#  示例 2： 
# 
#  输入：[0,1,2,2]
# 输出：3
# 解释：我们可以收集 [1,2,2]
# 如果我们从第一棵树开始，我们将只能收集到 [0, 1]。
#  
# 
#  示例 3： 
# 
#  输入：[1,2,3,2,2]
# 输出：4
# 解释：我们可以收集 [2,3,2,2]
# 如果我们从第一棵树开始，我们将只能收集到 [1, 2]。
#  
# 
#  示例 4： 
# 
#  输入：[3,3,3,1,2,1,1,2,3,3,4]
# 输出：5
# 解释：我们可以收集 [1,2,1,1,2]
# 如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tree.length <= 40000 
#  0 <= tree[i] < tree.length 
#  
#  Related Topics 数组 哈希表 滑动窗口 
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def totalFruit(self, fruits):
        max_length = 0
        unique = Counter()
        index = 0
        for i in range(len(fruits)):
            unique[fruits[i]] += 1
            while len(unique) > 2:
                # 这里之前多加了一个index 所以current length的计算不用加1
                current_length = i - index
                max_length = max(max_length, current_length)
                unique[fruits[index]] -= 1
                if unique[fruits[index]] == 0:
                    del unique[fruits[index]]
                index += 1
        return max(max_length, i - index + 1)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = [0, 1, 2, 2]
    b = [1, 2, 3, 2, 2]
    c = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    sol = Solution()
    print(sol.totalFruit(a))
    print(sol.totalFruit(b))
    print(sol.totalFruit(c))
