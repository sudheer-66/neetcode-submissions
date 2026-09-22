class Solution {
    public int maxSubArray(int[] nums) {

        int sm=0,mx=-99999;

        for(int i=0;i<nums.length;i++){
            
            sm+=nums[i];
            mx=Math.max(mx,sm);
            if(sm<0) sm=0;

        }
        return mx;
        
    }
}
