class Solution {
public:
    int longestValidParentheses(string s) {
	int n = s.size();
	if(n == 0 || n == 1)
		return 0;
	vector<int> dp(n); //it stores the lenght of the longest valid parentheses ending at index i	
	dp[0] = 0;		
	for(int i = 1; i < n; i++){
		if(s[i] == '('){
			dp[i] = 0;
		}
		else{// ) ending
			if(s[i-1] == '('){
				dp[i] = 2;
				if(i - 2 >= 0){
					dp[i] += dp[i-2];
				}
			}
			else{// ) at i-1
				dp[i] = 0;
				int cand_match_ind = i-1-dp[i-1];	
				if(cand_match_ind >= 0){
					if (s[cand_match_ind] == '('){
						dp[i] = 2 + dp[i-1];	
						if(cand_match_ind-1 >= 0){
							dp[i] += dp[cand_match_ind-1];
						}
					}
				}
			}
		}
	}

	int longest = INT_MIN;
	for(int i = 0; i < n; i++){
		if(dp[i] > longest)
			longest = dp[i];
	}

	return longest;
    }
};
