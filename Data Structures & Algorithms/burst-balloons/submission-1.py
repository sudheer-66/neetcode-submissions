class Solution:
    def maxCoins(self, nums: List[int]) -> int:


        def rec(l,r):

            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            dp[(l,r)]=0
            
            for i in range(l,r+1):
                count = nums[l-1]*nums[i]*nums[r+1]

                count+=rec(l,i-1)+rec(i+1,r)
                dp[(l,r)]=max(dp[(l,r)],count)
            
            return dp[(l,r)]

        nums=[1]+nums+[1]
        dp={}
        return rec(1,len(nums)-2)


        