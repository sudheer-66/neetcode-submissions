class Solution:
    def jump(self, nums: List[int]) -> int:

        mx=0

        n=len(nums)
        
        count=0
        i=0
        
        while i<n-1:

            if mx>=n-1:
                return count
            
            maxi=mx
            while i<=maxi:
                if(i+nums[i]>mx):
                    mx=i+nums[i]
                i+=1

            count+=1
        
        return count


        


            
        
        
        