class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def rec(ind1,ind2):
            if(ind1==len(s1)):
                if(s3[ind1+ind2:]==s2[ind2:]):
                    return True
                return False
            if(ind2==len(s2)):
                if(s3[ind1+ind2:]==s1[ind1:]):
                    return True
                return False
            if(dp[ind1][ind2]!=-1):
                return dp[ind1][ind2]
            if(s1[ind1]==s2[ind2]):
                if(s1[ind1]==s3[ind1+ind2]):
                    dp[ind1][ind2]=rec(ind1+1,ind2) or rec(ind1,ind2+1)
                    
                else:
                    dp[ind1][ind2]= False
    
            elif(s1[ind1]==s3[ind1+ind2]):
                dp[ind1][ind2]=rec(ind1+1,ind2)
            elif(s2[ind2]==s3[ind1+ind2]):
                dp[ind1][ind2]= rec(ind1,ind2+1)
            else:
                return False
            return dp[ind1][ind2]
        

        dp=[[-1]*len(s2) for _ in range(len(s1))]
        if(len(s1)+len(s2)>len(s3)):
            return False
        return rec(0,0)
            


            
        