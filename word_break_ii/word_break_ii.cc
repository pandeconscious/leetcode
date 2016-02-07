class Solution {
private:
	vector<string> cross(vector<string>* a, vector<string>* b){
		vector<string> to_return;
		for(vector<string>::iterator itrA = a->begin(); itrA != a->end(); itrA++){
			for(vector<string>::iterator itrB = b->begin(); itrB != b->end(); itrB++){
				to_return.push_back(*itrA + " " + *itrB);	
			}
		}
		return to_return;
	}
public:
    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
		vector<vector<vector<string>* > > dp(s.size());  
		for(int i = 0; i < s.size(); ++i){
			dp[i].resize(s.size());
			for(int j = 0; j < s.size(); ++j){
				dp[i][j] = NULL;
			}
		}
		for(int i = 0; i < s.size(); ++i){
			if(wordDict.find(s.substr(i,1)) != wordDict.end()){
				dp[i][i] = new vector<string>();
				dp[i][i]->push_back(s.substr(i,1));
			}
		}
		for(int L = 2; L <= s.size(); L++){
			for(int i = 0; i < s.size()-L+1; ++i){
				int j = i + L -1;
				if(wordDict.find(s.substr(i,j-i+1)) != wordDict.end()){
					dp[i][j] = new vector<string>();
					dp[i][j]->push_back(s.substr(i,j-i+1));
				}
				for(int k = i; k < j; k++){
					if(wordDict.find(s.substr(i,k-i+1)) != wordDict.end() && dp[k+1][j]){
						if(dp[i][j] == NULL){
							dp[i][j] = new vector<string>();
						}
						vector<string> lhsOfCross;
						lhsOfCross.push_back(s.substr(i, k-i+1));
						vector<string> to_add = cross(&lhsOfCross, dp[k+1][j]);
						dp[i][j]->insert(dp[i][j]->end(), to_add.begin(), to_add.end()); 
					}
				}
			}
		}
		if(dp[0][s.size()-1]){
			return *dp[0][s.size()-1];
		}
		else{
			vector<string> v;
			return v;
		}
    }
};
