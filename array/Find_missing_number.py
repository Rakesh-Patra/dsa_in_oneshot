class Solution:
    def missingNumber(self, nums ) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
                   
          
s=Solution()
f=s.missingNumber([3,0,1])
print(f)