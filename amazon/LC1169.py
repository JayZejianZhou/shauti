class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        invalid = dict()
        data = collections.defaultdict(list)
        for i in range(len(transactions)):
            it = transactions[i]+","+str(i) # 给一个编号识别
            temp = it.split(",")    
            
            
            if int(temp[2]) > 1000: invalid[it]=0
            if data[temp[0]]:
                for j in range(len(data[temp[0]])-1, -1, -1):
                    if abs(int(data[temp[0]][j][0]) - int(temp[1])) <= 60:
                        if not data[temp[0]][j][2] == temp[3]: 
                            last_one = temp[0]+","+",".join(data[temp[0]][j])
                            invalid[it] = 0
                            invalid[last_one] = 0

            data[temp[0]].append(temp[1:])
        
        res = []
        for it in invalid:
            temp = it.split(",")
            res.append(",".join(temp[:-1]))
        
        return res