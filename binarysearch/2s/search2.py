class Solution:
    def searchMatrix(self, matrix, target):
       m=len(matrix)
       n=len(matrix[0])
       rows=0
       cols=n-1
       while rows<m and cols>=0:
        if matrix[rows][cols]==target:
            return True
        elif matrix[rows][cols]>target:
            cols-=1
        else:
            rows+=1
       return False