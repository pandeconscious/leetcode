class Solution {
public:
    int nthUglyNumber(int n) {
        int* dp = new int[n];
        dp[0] = 1;
        int ind2 = 0, ind3 = 0, ind5 = 0;
        for(int i = 1; i < n; i++){
            while(2*dp[ind2] <= dp[i-1]){
                ind2++;
            }
            while(3*dp[ind3] <= dp[i-1]){
                ind3++;
            }
            while(5*dp[ind5] <= dp[i-1]){
                ind5++;
            }
            int minNum = min(2*dp[ind2], min(3*dp[ind3], 5*dp[ind5]));
            if(minNum == 2*dp[ind2]){
                dp[i] = 2*dp[ind2];
                ind2++;
            }
            else if(minNum == 3*dp[ind3]){
                dp[i] = 3*dp[ind3];
                ind3++;
            }
            else{
                dp[i] = 5*dp[ind5];
                ind5++;
            }
        }
        return dp[n-1];
    }
};
