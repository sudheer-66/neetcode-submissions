class Solution {

    List<List<Integer>> result = new ArrayList<>();
    public List<List<Integer>> subsets(int[] nums) {

        int n = nums.length;
        generate(0,new ArrayList<Integer>(),nums);
        return result;


        
    }

    public void generate(int ind,List<Integer> temp,int[] nums){
        if(ind==nums.length){
            result.add(new ArrayList<>(temp));
            return;
        }

        temp.add(nums[ind]);
        generate(ind+1,temp,nums);
        
        temp.remove(temp.size()-1);

        generate(ind+1,temp,nums);
    }
}
