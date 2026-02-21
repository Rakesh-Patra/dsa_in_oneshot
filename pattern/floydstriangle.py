class Solution:
    def pattern2(self, n):
        nums=0
        for i in range(n):
            for j in range(i+1):
                nums+=1
                print(nums,end="")
            print()
s=Solution()
s.pattern2(5)