class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def rec(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            sm=0
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(s[i]==t[j]):
                sm+=rec(i+1,j+1)
            sm+=rec(i+1,j)

            dp[i][j]=sm
            return sm

        dp=[[-1]*(len(t)+1) for _ in range(len(s))]
        return rec(0,0)
        