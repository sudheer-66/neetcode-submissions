class Solution {
    public int orangesRotting(int[][] grid) {


        Queue<int[]> que = new ArrayDeque<>();
        Set<int[]> visited = new HashSet<>();

        int len=0;
        int rows=grid.length,cols=grid[0].length;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]==2){
                    visited.add(new int[]{i,j});
                    que.offer(new int[]{i,j});
                    len++;
                }
            }
        }
        int res=0;
        while(!que.isEmpty()){
            int l =len;
            len=0;
            
            for(int i=0;i<l;i++){
                int[] cell = que.poll();
                int row = cell[0];
                int col = cell[1];
               
                
                int[][] dim = {{-1,0},{0,1},{1,0},{0,-1}};
                
                for(int[] di: dim){
                    int r = row+di[0];
                    int c = col + di[1];
                    if(r>=0 && r <rows && c>=0 && c<cols && grid[r][c]==1){
                        grid[r][c]=2;
                        if(!visited.contains(cell)){
                            visited.add(new int[]{r,c});
                            que.offer(new int[]{r,c});
                            len++;

                        }
                    }
                }
                

            }
            res+=1;
        }
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]==1){
                    return -1;
                }
            }
        }
        return res==0?0:res-1;
    }
}
