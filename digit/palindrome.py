class Solution:
    def print_digit(self, num):
        number = 0
        original=num
     
        while num > 0:
            digit = num % 10
            number = number * 10 + digit
            num = num // 10
       

        #if number<0:
           # print("not palindrome")
        if number==original:
            print('palindrome number')
        else:
            print("not palindrome")
   


s = Solution()
s.print_digit(-6534)
