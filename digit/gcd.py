class Solution:
    
    def gcd(self, num1, num2):
        n = min(num1, num2)   # no need to check greater
        
        gcd_value = 1
        for i in range(1, n+1):
            if (num1 % i == 0) and (num2 % i == 0):
                gcd_value = i
                
        return gcd_value

s = Solution()
print(s.gcd(4, 8))
