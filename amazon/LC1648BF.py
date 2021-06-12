class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        # make tuples out of inventory
        inv = [(-inventory[i], i) for i in range(len(inventory))]
        
        heapify(inv)
        price = 0
        for i in range(orders):
            inv_num, ball = heappop(inv)
            price += (-inv_num)
            heappush(inv, (inv_num+1, ball))
        return price % (pow(10,9)+7)
        
        pass
        
        