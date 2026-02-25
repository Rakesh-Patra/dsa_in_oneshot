class Solution:

    def longest_subarray_simple(self,nums, k):

      n = len(nums)
      max_len = 0
 
      for i in range(n):
          current_sum = 0
        
    
          for j in range(i, n):
             current_sum += nums[j]
          
             if current_sum == k:
               
                length = j - i + 1
                if length > max_len:
                    max_len = length
                    
      return max_len


s=Solution()
f=s.longest_subarray_simple( [-3, 2, 1],15)
print(f)