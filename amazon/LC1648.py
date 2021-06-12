class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        kmol = pow(10,9) + 7
        inventory.sort()
        price = 0
        i = len(inventory)-1
        order = 0

        while i>0:
            diff = inventory[i] - inventory[i-1]
            next_price = price + (inventory[i] + inventory[i-1] + 1)*diff/2 * (len(inventory)-i) 
            next_order = order + diff*(len(inventory)-i)
            
            # 检测是不是到超了order
            if next_order>orders: break
            price = next_price
            order = next_order
            
            i -= 1

        # 尾部处理一下
        rem = orders - order
        if rem > 0:
            num = len(inventory) - i    # the number of same digits
            # part 1: full decrease
            p1 = rem // num
            price += (inventory[i]-p1+1 + inventory[i])*p1/2 * num
            # part 2: individule decrease
            p2 = rem % num
            price += p2 * (inventory[i]-p1) % kmol 

                
                
        return int(price % kmol)