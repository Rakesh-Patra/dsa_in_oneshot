class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1 if nums[0] == 1 else 0
        res = count 

        for i in range(n - 1): 
            if nums[i+1] == 1:
               
                if nums[i] == 1:
                    count += 1
                else:
                    count = 1
                
                if count > res: res = count
            else:
                
                count = 0
                
        return res
        

s = Solution()

f = s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
print(f) 