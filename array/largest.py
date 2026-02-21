class Solution:
    def largest(self, num):
        n = len(num)
        largest = num[0]

        for i in range(n):
            if num[i] > largest:
                largest = num[i]

        print(largest)

s = Solution()
s.largest([3, 4])
