class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        data = collections.defaultdict(list)
            
        for it in items:
            data[it[0]] += [it[1]]
        
        res = []
        for key, val in data.items():
            val.sort()
            val = val[::-1]
            sumT = 0
            for i in range(5):
                sumT += val[i]
            sumT = sumT//5
            res.append([key, sumT])
        
        return res
        
        