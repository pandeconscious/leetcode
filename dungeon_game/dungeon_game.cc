class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        vector<vector<int> > dp_power(m);
        for(int i = 0; i < m; i++){
            dp_power[i].resize(n);
        }
        
        if(dungeon[m-1][n-1] <= 0){
            dp_power[m-1][n-1] = 1;
        }
        else{
            dp_power[m-1][n-1] = dungeon[m-1][n-1] + 1;
        }
        
        for(int i = m-2; i >= 0; --i){
            if(dungeon[i][n-1] >= dp_power[i+1][n-1] - dungeon[i+1][n-1]){
                dp_power[i][n-1] = dungeon[i][n-1] + 1; 
            }
            else{
                dp_power[i][n-1] = dp_power[i+1][n-1] - dungeon[i+1][n-1];
            }
        }
        
        for(int i = n-2; i >= 0; --i){
            if(dungeon[m-1][i] >= dp_power[m-1][i+1] - dungeon[m-1][i+1]){
                dp_power[m-1][i] = dungeon[m-1][i] + 1; 
            }
            else{
                dp_power[m-1][i] = dp_power[m-1][i+1] - dungeon[m-1][i+1];
            }
        }
        
        for(int i = m-2; i >= 0; --i){
            for(int j = n-2; j >= 0; --j){
                if(dp_power[i+1][j] - dungeon[i+1][j] < dp_power[i][j+1] - dungeon[i][j+1]){
                    //along row best soln
                    if(dungeon[i][j] >= dp_power[i+1][j] - dungeon[i+1][j]){
                        dp_power[i][j] = dungeon[i][j] + 1; 
                    }
                    else{
                        dp_power[i][j] = dp_power[i+1][j] - dungeon[i+1][j];
                    }
                }
                else{
                    //along col best soln
                    if(dungeon[i][j] >= dp_power[i][j+1] - dungeon[i][j+1]){
                        dp_power[i][j] = dungeon[i][j] + 1; 
                    }
                    else{
                        dp_power[i][j] = dp_power[i][j+1] - dungeon[i][j+1];
                    }
                }
            }
        }
        return dp_power[0][0] - dungeon[0][0];
    }
};
