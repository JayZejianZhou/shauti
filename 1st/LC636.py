class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        times = [0 for i in range(n)]
        stack = []
        for it in logs:
            rec = it.split(":")
            if stack and rec[0]==stack[-1][0] and rec[1]=="end":
                duration = int(rec[2])-int(stack[-1][2]) + 1
                times[int(rec[0])] += duration
                # 调整下面所有的时间
                for it in stack:
                    it[2] = str(duration + int(it[2]))
                stack.pop()
            else: stack.append(rec)
        
        return times
        