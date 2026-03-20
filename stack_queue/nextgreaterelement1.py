class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge_map = {}

        for s in nums2:
            while stack and stack[-1] < s:
                nge_map[stack.pop()] = s
            
            stack.append(s) 
        
        while stack:
            nge_map[stack.pop()] = -1

        return [nge_map[num] for num in nums1]


s = Solution()
print(s.nextGreaterElement([1,2,1], [1,2,1]))