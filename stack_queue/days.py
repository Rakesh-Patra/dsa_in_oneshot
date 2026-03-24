class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  

        for i in range(n - 1, -1, -1):
          
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                
                res[i] = stack[-1] - i
            
            
            stack.append(i)
            
        return res

s = Solution()
print(s.dailyTemperatures([1, 3, 4, 2])) 
# Output: [1, 1, 0, 0]