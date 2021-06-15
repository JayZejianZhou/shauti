# https://blog.csdn.net/qq_37821701/article/details/109636608
class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        data = {}
        res = []
        
        for name in names:
            count = data.get(name, 0)
            if count == 0:
                data[name] = 1
                res.append(name)
            else:
                name_back = name
                while name_back in data:
                    name_back = name + '(' + str(count) + ')'
                    count += 1
                data[name] = count
                data[name_back] = 1
                res.append(name_back)
                
        return res