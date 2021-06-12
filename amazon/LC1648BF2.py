class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        kmol = 10e9+7
        inventory.sort()
        price = 0
        i = len(inventory)-1
        order = 0

        while i>0:
            diff = inventory[i] - inventory[i-1]
            next_price = price + (inventory[i] + inventory[i-1] + 1)*diff/2 * (len(inventory)-i)
            next_order = order + diff*(len(inventory)-i)
            
            # 检测是不是到超了order
            if order>=orders: break
            price = next_price
            order = next_order
            
            
            inventory[i] = inventory[i-1]
            i -= 1

        # 尾部处理一下
        h = []
        heapify(h) 
        for it in inventory:
            heappush(h, -it)
        
        for i in range(orders-order):
            temp = -heappop(h)
            price += temp
            heappush(h, -(temp-1))
                
                
        return price