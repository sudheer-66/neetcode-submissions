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
        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]+=dp[i][j+1]+dp[i+1][j]
        return dp[0][0]

        


        