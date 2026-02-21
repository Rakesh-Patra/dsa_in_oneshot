class Solution:
    def print_digit(self, num):
        number = 0
        original=num
        total=0
        power = len(str(num))
     
        while num > 0:
            digit = num % 10
            total+=digit**power
            num = num // 10
        
       

        #if number<0:
           # print("not palindrome")
        if total==original:
            print('armstrong number')
        else:
            print("not armstrong")
   


s = Solution()
s.print_digit(153)
