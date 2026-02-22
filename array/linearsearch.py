class Solution:
    def linearSearch(self, nums, target):
        target=target
        n=len(nums)
        for i in range(n-1):
            if (nums[i]==target):
                return i
            else :
                return -1
s=Solution()
num=s.linearSearch([2,4,5,6],2)
print(num)