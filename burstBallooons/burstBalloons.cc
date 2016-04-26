class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        if(n == 0){
            return 0;
        }
        else if(n == 1){
            return nums[0];
        }
        else{
            vector<int> numsT(n+2);
            numsT[0] = 1;
            numsT[n+1] = 1;
            copy(nums.begin(), nums.end(), numsT.begin()+1);
            int** dp = new int*[n];
            for(int i = 0; i < n; i++){
                dp[i] = new int[n];
            }
            for(int i = 0; i < n; i++){
                dp[i][i] = numsT[i]*numsT[i+1]*numsT[i+2];
            }
            for(int L = 2; L <= n; L++){
                for(int i = 0; i <= n-L; ++i){
                    int j = i + L -1;
                    int maxCost = -1;
                    for(int last = i; last <= j; last++){
                        int currCost = numsT[last+1]*numsT[i]*numsT[j+2];
                        if(last == i){
                            currCost += dp[last+1][j];
                        }
                        else if(last == j){
                            currCost += dp[i][last-1];
                        }
                        else{
                            currCost += dp[i][last-1] + dp[last+1][j];
                        }
                        if(currCost > maxCost){
                            maxCost = currCost;
                        }
                    }
                    dp[i][j] = maxCost;
                }
            }
            return dp[0][n-1];
        }
    }
};
