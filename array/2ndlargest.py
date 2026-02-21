class Solution:
    def largest(self, num):
        n = len(num)
        largest = num[0]
        second_largest= num[0]
        if n==1:
            print("There is no second largest element")
            return

        for i in range(n):
            if num[i] > largest:
                largest = num[i]

       
        for j in range(n):
            if num[j] > largest and num[j] != largest:
                second_largest = num[j]
            else:
                second_largest=-1

        print(second_largest)

s = Solution()
s.largest([1,1, 1,1])
