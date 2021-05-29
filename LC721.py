class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        flag_fnd = False    # 发现重复的了
        rec = collections.defaultdict(list)
        for it in accounts:
            if it[0] in rec:
                # for jt in rec[it[0]]:   # 挑出来同一名字，有多少email list
                    # for kt in it[1:]:   # 把此时的这个人的每个email选出来
                    #     if kt in jt:
                    #         jt += it[1:]    # 先全放进去，然后再消重0
                    #         flag_fnd = True
                    #         break
                    # if flag_fnd:
                    #     flag_fnd = False
                    #     break
                    # else:
                    #     rec[it[0]].append(it)    # 不一样，放回去
                rec[it[0]].append(it[1:])   # 同名的先全部存一起
            else:
                rec[it[0]] = [it[1:]] # 名字就不一样，直接加进去
        
        # 找出同名不同email
        for key, val in rec.items():
            while not self.is_intec_all(val):   # 确保一个人同一个名字，不同email列表，没有交集了
                for it in val:  # 每一个名字+email

                    diff = self.find_diff(val, it)  # 除了本列表以外的其他列表

                    for jt in diff: # 看看本列表与同名其他列表有没有email 重合
                        if self.is_intec(jt, it):
                            it += jt
                            val.remove(jt)
                pass
        
        res = []      
        # 最后处理
        for key, val in rec.items():
            for it in val:   # 每一个同名不同email的的列表
                em = {}.fromkeys(it).keys()   # 删重复的
                em.sort()   # 排序
                res.append([key]+em)    # 包装好放到结果列表中
        
        return res
                
    # 补集, a-b
    def find_diff(self, a, b):
        res = []
        for it in a:
            if not it == b:
                res.append(it)
        return res
        
    # 有没有交集
    def is_intec(self, a, b):
        for it in a:
            if it in b:
                return True
        return False
    
    # list 内部有没有交集
    def is_intec_all(self, a):
        for i in a:
            diff = self.find_diff(a, i)
            for j in diff:
                if self.is_intec(i, j):
                    return False
        return True
                    
                    
            