class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        data = sorted(boxTypes, key = lambda a: a[1], reverse = True)
        
        box = 0 
        res = 0
        for i in range(len(data)):
            for j in range(data[i][0]):
                if box >= truckSize: break
                else: 
                    res += data[i][1]
                    box += 1
            if box >= truckSize: break
        
        return res