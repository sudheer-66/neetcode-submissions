class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        map={0:1}
        sm=0
        cnt=0
        for i in nums:
            sm+=i
            
            if sm-k in map:
                cnt+=map[sm-k]
            if sm not in map:
                map[sm]=1
            else:
                map[sm]+=1
        return cnt

        