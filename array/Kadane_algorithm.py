class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = 0
        current_sum=0
        
      
        for x in nums:
            current_sum=max(x,current_sum+x)


            max_sum=max(current_sum,max_sum)
            
           
        return max_sum

s = Solution()
print(s.maxSubArray([2, 3, 4, 5])) 