from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i=0
      n=len(nums)
      while i<len(nums)-1:
           j=i+1
    
           while j<len(nums)-1:
            if nums[i]==nums[j]:

             del nums[j]
            else :
               j+=1
           i+=1
      while len(nums)<n:
         nums.append(0)
      return nums
     
s=Solution()

num=s.removeDuplicates([5,6,6,7,8])


print(num)
