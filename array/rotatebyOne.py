class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        if n <= 1: return nums
        
      
        first_element = nums[0]
        
        i = 0
     
        while i < n - 1:
            nums[i] = nums[i + 1]
            i += 1
        
        
        nums[n - 1] = first_element
        
        return nums

s = Solution()
num = s.rotateArrayByOne([3, 4, 5, 6])
print(num) 