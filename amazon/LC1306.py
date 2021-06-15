class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q = [start]
        
        while q:
            node = q.pop(0)
            if arr[node]<0:
                continue
            
            if arr[node] == 0:
                return True
            
            if node+arr[node]< len(arr): q.append(node+arr[node])
            if node-arr[node]>=0: q.append(node-arr[node])
            
            arr[node] = -arr[node]
        return False
        