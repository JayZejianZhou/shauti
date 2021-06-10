"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # make a dictionary for all employees
        emp = collections.defaultdict(Employee)
        for it in employees:
            emp[it.id] = it
        
        
        
        res = self.helper(emp, id)
        return res
            
            
    def helper(self, emp, id):
        summ = emp[id].importance
        if not emp[id].subordinates:
            return emp[id].importance
        for i in emp[id].subordinates:
            summ += self.helper(emp, i)
            
        return summ