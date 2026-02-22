from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i=0
      n=len(nums)
      while i<len(nums)-1:
          
    
            if nums[i]==0:
             del nums[i]
            else:
               
               i+=1
           
      while len(nums)<n:
         nums.append(0)
      return nums
     
s=Solution()

num=s.removeDuplicates([5,6,0,0,7,8])


print(num)
