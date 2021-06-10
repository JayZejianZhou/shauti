class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_str = ''
        if not strs[0]: #empty string
            return ''
        flag_diff = False
        for i in range(len(min(strs, key=len))):
            c = strs[0][i]
            if all(a[i]==c for a in strs):
                common_str += c
            else: 
                break
                
        return common_str
        