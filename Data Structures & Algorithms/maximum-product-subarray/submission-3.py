class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        posprod,negprod=1,1

        mx=-11

        for i,v in enumerate(nums):
            if(v==0):
                posprod,negprod=1,1
                if(mx<0):
                    mx=0
            else:
                old,new = posprod,negprod
                posprod=max(old*v,v,new*v)
                negprod=min(new*v,old*v,v)
                mx=max(mx,posprod)
                
        return mx



        