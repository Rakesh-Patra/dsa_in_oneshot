class Solution:
    def set_matrix(self, nums):
        if not nums:
            return []
            
        rows_count = len(nums)
        cols_count = len(nums[0])
       
        zero_rows = set()
        zero_cols = set()

        for i in range(rows_count):
            for j in range(cols_count):
                if nums[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in range(rows_count):
            for j in range(cols_count):
                if i in zero_rows or j in zero_cols:
                    nums[i][j] = 0

        return nums
s=Solution()
print(s.set_matrix( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))