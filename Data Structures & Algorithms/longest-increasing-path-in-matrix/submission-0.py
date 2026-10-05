class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def rec(i,j):
            
            
            if dp[i][j]!=0:
                return dp[i][j]
            dp[i][j]=1
            for x,y in [[-1,0],[1,0],[0,-1],[0,1]]:
                r=x+i
                c=y+j

                if min(r,c)>=0 and r<=len(matrix)-1 and c<=len(matrix[0])-1 and matrix[r][c]>matrix[i][j]:
                    dp[i][j]=max(dp[i][j],1+rec(r,c))
            return dp[i][j]

        lis=0
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lis=max(lis,rec(i,j))
        return lis
        