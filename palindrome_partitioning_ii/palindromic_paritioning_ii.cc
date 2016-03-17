class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        if(n == 0 || n == 1){
            return 0;
        }
        
        int** isPalindrome = new int* [n];
        for(int i = 0; i < n; ++i){
            isPalindrome[i] = new int[n];
        }
        
        for(int L = 1; L <= n; ++L){
            for(int i = 0; i < n - L + 1; ++i){
                int j = i + L -1;
                if(L == 1){
                    isPalindrome[i][j] = 1;
                }
                else if(L == 2){
                    isPalindrome[i][j] = s[i] == s[j] ? 1 : 0;
                }
                else{
                    isPalindrome[i][j] = s[i] == s[j] ? isPalindrome[i+1][j-1] : 0;
                }
            }
        }
        
        int* dp = new int[n];
        dp[0] = 0;
        for(int i = 1; i < n; i++){
            dp[i] = INT_MAX;
        }
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(isPalindrome[0][i]){
                    dp[i] = 0;
                }
                else if(isPalindrome[j+1][i]){
                    dp[i] = min(dp[i], 1+dp[j]);
                }
            }
        }
        return dp[n-1];
    }
};
