class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        flag_found = False
        for it in nums1:
            ind = nums2.index(it)
            for jt in range(ind, len(nums2)):
                if nums2[jt] > it:
                    res.append(nums2[jt])
                    flag_found = True
                    break
            if not flag_found:
                res.append(-1)
            flag_found = False
                
        return res
                
                
        