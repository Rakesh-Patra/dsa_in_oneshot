class Solution:
    def next(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2*n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if stack:
                    res[i] = stack[-1]

            stack.append(nums[i % n])

        return res


s = Solution()
print(s.next([1,3,4,2]))