class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 统计前置课
        crs = collections.defaultdict(list)
        crsR = collections.defaultdict(list)
        for it in prerequisites:
            crs[it[1]].append(it[0])    # 修了某课之后可以再修什么课
            crsR[it[0]].append(it[1])   # 修某课需要什么前置课
        
        # DFS
        visited = [0]*numCourses    # 0--not visited, 1--visited in this loop, 2--visited in previous loops
        
        for it in range(numCourses):            
            if not self.dfs(visited, crsR, it):
                return False        
        return True
            
            
            
    # crs: 修了某课之后可以再修什么课
    def dfs(self, visited, crs, i):
        if visited[i] == 1:
            return False
        elif visited[i] == 2:
            return True
        visited[i] = 1
        for it in crs[i]:
            if not self.dfs(visited, crs, it):
                return False
        visited[i] = 2
        return True
                
                