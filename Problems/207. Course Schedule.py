# 好厉害 进阶版dfs
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacent = [[] for i in range (numCourses)]
        visited =  [0 for i in range(numCourses)]

        for i in prerequisites:
            adjacent[i[0]].append(i[1])

        print(adjacent)

        for i in range(numCourses):
            if not self.dfs(i, adjacent, visited):
                return False
        return True

    def dfs(self, course, adjacent, visited):
        if visited[course] == -1:
            return False
        if visited[course] == 1:
            return True
        visited[course] = -1
        for i in adjacent[course]:
            if self.dfs(i, adjacent, visited) == False:
                return False
        visited[course] = 1
        return True

sol = Solution()
sol.canFinish(2, [[1,0], [0,1]])