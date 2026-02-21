class Solution:
    def print_digit(self,num):
        n=num
        if n==0:
            return 
        self.print_digit(n-1)
        print(n,end="")

s=Solution()
s.print_digit(4)
        