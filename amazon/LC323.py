class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = []
        graph = collections.defaultdict(list)
        for it in edges: 
            graph[it[0]].append(it[1])
            graph[it[1]].append(it[0])
        
        res = 0
        for i in range(n):
            if not i in visited: res+=1
            self.dfs(graph, i, visited)
        
        return res
        
        
    def dfs(self, graph, base, visited):
        if base in visited: return 0
        else:
            visited.append(base)
            for it in graph[base]:
                self.dfs(graph, it, visited)
        
        