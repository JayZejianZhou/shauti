class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for it in arr:
            dic[it] = 1
            
        cnt = 0
        while k > 0:
            cnt += 1
            if dic[cnt] == 0:
                k -= 1
            
        
        return cnt