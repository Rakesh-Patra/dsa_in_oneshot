class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        n=len(nums)
        value=1
        longest=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                value+=1
            else:
                longest=max(longest,value)
        return max(longest,value)
s=Solution()
print(s.longestConsecutive([2,4,5,6,8,7]))