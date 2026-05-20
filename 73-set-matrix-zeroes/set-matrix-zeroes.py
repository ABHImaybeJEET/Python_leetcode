class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        row_track=[0 for _ in range (m)]
        col_track=[0 for _ in range (n)]

        for i in range (0,m):
            for j in range (0,n):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    col_track[j]=-1
        for i in range (0,m):
            for j in range (0,n):
                if row_track[i]==-1 or col_track[j]==-1:
                    matrix[i][j]=0        