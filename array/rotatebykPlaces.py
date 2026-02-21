class Solution:
    def rotateArrayByOne(self, nums, k):
        n = len(nums)

        k = k % n 
        if n <= 1 or k == 0: return nums
        
     
        temp = nums[:k]
        
     
        i = 0
        while i < n - k:
            nums[i] = nums[i + k]
            i += 1
       
        for j in range(len(temp)):
            nums[n - k + j] = temp[j]
            
        return nums

s = Solution()

num = s.rotateArrayByOne([3, 4, 5, 6], 2)
print(num)