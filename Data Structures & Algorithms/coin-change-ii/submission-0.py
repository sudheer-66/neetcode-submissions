class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(ind,sm):
            if sm>amount or ind == len(coins):
                return 0
            if sm == amount:
                return 1
            if(dp[ind][sm]!=0):
                return dp[ind][sm]
            
            dp[ind][sm]=dfs(ind,sm+coins[ind])+dfs(ind+1,sm)
            return dp[ind][sm]
        
        dp=[[0]*(amount+1) for _ in range(len(coins)+1)]
        return dfs(0,0)