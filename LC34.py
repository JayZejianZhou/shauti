class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 二分法，找到这个位置
        left, right = 0, len(nums)-1
        if left==right:
            return [0,0] if nums[left]==target else [-1,-1]
        if not nums:
            return [-1, -1]
         
        flag_found = False
        while left < right:
            mid = left+(right-left)//2
            if right-left == 1: break
            elif nums[mid] > target:  right = mid
            elif nums[mid]< target:  left = mid
            else: 
                flag_found = True
                break
            
        if not flag_found:
            if nums[left] == target: mid=left
            elif nums[right] == target: mid=right
            else: return [-1,-1]
        
        res = []
        # 往左往右找最先出现的, 左
        left, right = 0, mid
        if left==right: res.append(left)
        else:
            while left < right:
                mid = left+(right-left)//2
                if right-left == 1: break
                if nums[mid] < target:  left = mid
                elif nums[mid] == target: right = mid
            if nums[left] == target: res.append(left)
            else: res.append(right)
        
        # 右
        left, right = mid, len(nums)-1
        if left==right: res.append(left)
        else:
            while left+1 < right:
                mid = left+(right-left)//2
                if right-left == 1: break
                if nums[mid] > target: right = mid
                elif nums[mid] == target: left = mid
            if nums[right] == target: res.append(right)
            else: res.append(left)
            
        return res
                