class Solution:
    def leaders(self, a):
         
        n = len(a)
        ind = -1
        res=[]
        
        max_from_right = a[n - 1]
        res.append(max_from_right)
        for i in range(n - 2, -1, -1):
            if a[i]>max_from_right:
                res.append(a[i])
                max_from_right = a[i]
        return res[::-1]
s=Solution()
print(s.leaders([1, 2, 5, 3, 1, 2]))