class Solution:
    def stockBuySell(self, arr):
        if not arr:
            return 0
            
        min_price = float('inf')
        max_profit = 0
        
        for price in arr:
          
            if price < min_price:
                min_price = price
            
            current_profit = price - min_price
            
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit
s=Solution()
num = s.stockBuySell([3, 2,1,0])
print(num)