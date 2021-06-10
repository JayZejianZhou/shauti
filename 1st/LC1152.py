#https://blog.csdn.net/qq_32424059/article/details/99549039
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        seq_count = collections.defaultdict(int)
        # set profile for everyone
        record = collections.defaultdict(list)
        for i, it in enumerate(username):
            record[it].append([timestamp[i], website[i]])
        
        
        for key in record.keys():
            record[key].sort()  # sort based on time stamps
            used = []   # used combinations for the same person
            # seek the combinations
            for i in range(len(record[key])):
                for j in range(i+1, len(record[key])):
                    for k in range(j+1, len(record[key])):
                        cur_seq = record[key][i][1] + '.' + record[key][j][1] + '.' + record[key][k][1]   
                        if not cur_seq in used:
                            seq_count[cur_seq] += 1
                            used.append(cur_seq)
        
        
        # search for possible solutions
        sols = []
        max_num = max(seq_count.values())
        for key, val in seq_count.items():
            if val == max_num:
                sols.append(key.split('.'))     
        sols = sols[::-1]
        
        # more than one solution
        if len(sols) >= 1:
            sols.sort()

        return sols[0]
        
                
        
        