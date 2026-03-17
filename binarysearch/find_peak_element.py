class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]

obj = Solution()
print(obj.findPeakElement(nums))