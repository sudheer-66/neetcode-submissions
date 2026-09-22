class Solution {

    Map<Integer,List<Integer>> map = new HashMap<>();
    Set<Integer> visited = new HashSet<>();
    public boolean validTree(int n, int[][] edges){

        if(edges.length<n-1) return false;

        for(int[] edge : edges){
            map.putIfAbsent(edge[0],new ArrayList<>());
            map.putIfAbsent(edge[1],new ArrayList<>());

            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);

        }

        for(int i=0;i<n;i++){
        
        if(!visited.contains(i)){
        if(!(dfs(i,-1))) return false;
        }
        }
        return true;
    }
    

        public boolean dfs(int source , int parent){
            if(visited.contains(source)){
                return false;
            }
            visited.add(source);
            for(int node : map.getOrDefault(source,new ArrayList<>())){
                if(node == parent) continue;
                if(!dfs(node,source)){
                    return false;
                }
            }
            return true;

        }
}
