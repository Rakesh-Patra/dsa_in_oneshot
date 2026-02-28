class Solution:
    def nextPermutation(self, a: list[int]) -> None:
        n = len(a)
        ind = -1
        
   
        for i in range(n - 2, -1, -1):
            if a[i] < a[i + 1]:
                ind = i
                break
     
        if ind == -1:
            a.reverse()
            return

   
        for i in range(n - 1, ind, -1):
            if a[i] > a[ind]:
                a[i], a[ind] = a[ind], a[i] 
                break
        
       
        a[ind + 1:] = reversed(a[ind + 1:])
        return a
    
s=Solution()
print(s.nextPermutation([1,2,3]))