class Solution:
    def rearrangeArray(self, nums):
        result1 = [] # To store positive numbers
        result2 = [] # To store negative numbers
        
        # 1. Separate the numbers into two lists
        for num in nums:
            if num >= 0:
                result1.append(num) # Use .append() to add to the list
            else:
                result2.append(num)
        
        # 2. Prepare the final result list
        ans = []
        minlength = min(len(result1), len(result2))
        
        # 3. Interleave them (The "Zip" logic)
        for i in range(minlength):
            ans.append(result1[i])
            ans.append(result2[i])
        if len(result2)>len(result1):
            ans.extend(result2[minlength:])
        else:
            ans.extend(result1[minlength:])
            
        return ans
s=Solution()
print(s.rearrangeArray([2, 4, 5, -1, -3, -4,5]))