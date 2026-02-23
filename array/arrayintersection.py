
import numpy as np

class Solution:
    def unionArray(self, nums1, nums2):
        nums1 = list(nums1)
        nums2 = list(nums2)
        res=[]
       
        for i in range(len(nums1)):
            for j in range(len(nums2)-1):
                if nums1[i] == nums2[j]:
                    if nums1[i] not in res:
                        res.append(nums1[i])
        
      
        return res
        
s = Solution()
result = s.unionArray([1, 2], [2, 3])
print(result) 