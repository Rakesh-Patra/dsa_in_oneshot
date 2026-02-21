
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        
        digits[n-1]=digits[n-1]+1
        return digits
s=Solution()
print(s.plusOne([3,5,6]))
        