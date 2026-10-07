class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        def rec(i,j):

            if j<0:
                return i+1
            if i<0:
                return j+1
            if (i,j) in dp:
                return dp[(i,j)]

            if(word1[i]==word2[j]):
                dp[(i,j)]=rec(i-1,j-1)
                return dp[(i,j)]
            
            dp[(i,j)]=1+min(rec(i-1,j),rec(i-1,j-1),rec(i,j-1))
            return dp[(i,j)]

        m,n=len(word1),len(word2)
        dp={}
        return rec(m-1,n-1)
        




        