class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        # 用0来消多的
        data = collections.defaultdict(list) # i湖下了几场雨
        full = []   # 满的湖
        res = [9]*len(rains)
        allow = []   # 允许清理的日子
        for i in range(len(rains)):
            if rains[i]==0: 
                allow.append(i)
            elif len(data[rains[i]])>0 :
                if not allow: return []    # 满了
                if data[rains[i]][0] > allow[-1]: return [] # 排空都出现在你这个重复之前
                else: # 关于是用前面的还是后面的allow来清，前面的能清就用前面的，前面的不行就用后面的
                    j = 0
                    while j<len(allow) and allow[j] < data[rains[i]][0]: j += 1  # 找出rains[i]第一次下雨后最近的一个allow时间
                    if j == len(allow): j-=1
                    res[allow[j]] = rains[i]
                    allow.pop(j)  # 清理
                    data[rains[i]].pop(0)
                    data[rains[i]].append(i)
                res[i]=-1
            else:
                data[rains[i]].append(i)
                # allow = []  # 记得allow 排空
                res[i]=-1

        return res
            
            