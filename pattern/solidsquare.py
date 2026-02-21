class Solution:
    def pattern1(self, n):
         for i in range(n):
            for k in range(n-i-1):
                print(" ",end="")
            for j in range(i*2+1):
                print("*", end="")
            print()
         for i in range(n):
            for k in range(i):
                print(" ",end="")
            for j in range(2 * (n - i) - 1):
                print("*", end="")
            print()
s=Solution()
s.pattern1(4)