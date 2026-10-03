class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def rec(i,j):
            if i>=m or j>=n:
                return 0
            if(i==m-1 and j==n-1):
                return 1
            if(dp[i][j]!=0):
                return dp[i][j]
            
            dp[i][j]=rec(i+1,j)+rec(i,j+1)
            return dp[i][j]
        
        dp=[[0]*(n+1) for _ in range(m+1)]
        return rec(0,0)


        