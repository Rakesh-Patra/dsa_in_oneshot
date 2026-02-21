class Solution:
    def print_digit(self, num):
        number = 0

     
        while num > 0:
            digit = num % 10
            number = number * 10 + digit
            num = num // 10

        
        while number > 0:
            print(number % 10)
            number = number // 10


s = Solution()
s.print_digit(5873)
