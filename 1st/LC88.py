class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res = []
        cur_max = float('-inf')
        ind1, ind2 = 0, 0
        
        if not n:
            return -1
                
        if m == 0:
            res = nums2
            
        if n == 0:
            res = num[:m]
        
        for i in range(m+n):
            if nums1[ind1]<=nums2[ind2]:
                res.append(nums1[ind1]) 
                ind1 += 1
            else:
                res.append(nums2[ind2]) 
                ind2 += 1

            if ind1>=m:
                res = res+nums2[max(ind2,0):n]
                break
            if ind2>=n:
                res = res+nums1[max(ind1,0):m]
                break
        for i in range(m+n):
            nums1[i] = res[i]
        pass