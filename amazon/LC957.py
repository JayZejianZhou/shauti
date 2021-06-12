class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        # find the peroid
        new = cells[:]
        p = 0
        periods = [new[:]]
        while p <= n:
            for i in range(len(cells)):
                if i>0 and i<len(cells)-1 and periods[-1][i-1] == periods[-1][i+1]: new[i] = 1
                else: new[i] = 0     
                    
            if len(periods)>1 and new == periods[1]: break
                    
            periods.append(new[:])
            p += 1
        
        # find the mod
        rem = n % p
        
        if rem==0: return periods[-1]
        
        return periods[rem]
        
        
                