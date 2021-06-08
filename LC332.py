class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 统计图
        graph = collections.defaultdict(list)
        for it in tickets:
            graph[it[0]].append(it[1])
            
        # 排序
        for key in graph.keys(): graph[key].sort()
            
        self.lens = len(tickets)
        
        # dfs
        res = ["JFK"]
        self.dfs(graph, [], "JFK", res)
        return res
        
    def dfs(self, graph, used, cur, res):  
        if not graph[cur] and len(used) < self.lens:    # 这跳路径去不了任何地方，但是票还没用完，所以说明此方法不通
            return False  
        elif len(used) >= self.lens: # 找完了
            return True
        elif not graph[cur]:
            return False        
        else:
            cc = graph[cur][:]
            for i in range(len(cc)):
                it = cc[i]
                now_cur = it
                res.append(now_cur)            
                graph[cur].pop(i)
                used.append([cur, it])
                if self.dfs(graph, used, now_cur, res):
                    return True
                else:
                    res.pop()
                    used.pop()
                    graph[cur] = graph[cur][:i] + [it] + graph[cur][i:]
            return False
        
        
        