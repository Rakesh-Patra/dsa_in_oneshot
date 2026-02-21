class Solution:
    def printNumbers(self, n):
        # Your code goes here

   
        if n==0:
            return 0
        else:
            return n+self.printNumbers(n-1)
       

s=Solution()


print(s.printNumbers(4))
