class Solution:
    def rotate(self, nums, k: int) -> None:

        n = len(nums)
        k = k % n 
        if n <= 1 or k == 0: return nums
     
    
        temp = nums[n-k:] 
        
     
        i = n - k - 1
        while i >= 0:
            nums[i + k] = nums[i]
            i -= 1
     
        for j in range(len(temp)):
            nums[j] = temp[j]
            
        return nums
    
s = Solution()

num = s.rotate([3, 4, 5, 6], 3)
print(num)