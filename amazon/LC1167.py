class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        #priority queue
        heapify(sticks)
        
        cost = 0
        while len(sticks) >= 2:
            a = heappop(sticks)
            b = heappop(sticks)
            
            costT = a+b
            cost += costT
            heappush(sticks, costT)
        
        return cost