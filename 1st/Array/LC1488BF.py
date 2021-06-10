class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        # 用0来消多的
        data = collections.defaultdict(int) # i湖下了几场雨
        full = []   # 满的湖
        res = []
        for i in range(len(rains)):
            if rains[i]==0:  # 清理湖
                # 找到下一个下雨的满湖
                j = i
                while j<len(rains) and (rains[j]==0 or data[rains[j]]==0): j+=1
                if not j==len(rains): 
                    data[rains[j]] -= 1
                    res.append(rains[j])
                else:
                    if data[rains[i]]>0:res.append(-1)
                    else: res.append(1)

            elif data[rains[i]]>0: return []    # 满了
            else: 
                data[rains[i]] += 1
                res.append(-1)
        return res
            
            