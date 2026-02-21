class Solution:
    def countdigit(self,num):
        count=0
        while num>0:
            count+=1
            num=num//10

        return count
        
s=Solution()
result=s.countdigit(7685)
print(result)

