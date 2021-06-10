class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 统计
        self.data = collections.defaultdict(int) # {index: value}
        self.inds = []
        self.len = len(nums)
        
        for i in range(len(nums)):
            if not nums[i]==0:
                self.data[i] = nums[i]
                self.inds.append(i)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for key, val in vec.data.items():
            if key in self.inds and key in vec.inds: res+=self.data[key]*vec.data[key]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)