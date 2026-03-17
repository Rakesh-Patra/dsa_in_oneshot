class Solution:
    def shipWithinDays(self, weights, days):
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
           
            curr = 0
            d = 1
            
            for w in weights:
                if curr + w > mid:
                    d += 1
                    curr = 0
                curr += w
            
            if d > days:
                left = mid + 1
            else:
                right = mid
        
        return left
        
        