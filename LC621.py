
#https://maxming0.github.io/2020/07/28/Task-Scheduler/
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # make dictionary for the occurance
        data = collections.defaultdict(int)
        for i in tasks:
            data[i] += 1
        data = sorted(data.items(), key = lambda d:(d[1], d[0]), reverse = True)   # sort the dictionary
        

        
        frequent = data[0][1]
        
        p = 0
        for it in data:
            if it[1] == frequent: p+=1
        
        return max(len(tasks), (frequent-1)*(n+1) + p)
        
        
        