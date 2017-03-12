#include<iostream>
#include<vector>


using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n1 = s1.size();
	int n2 = s2.size();
	int n3 = s3.size();
	if(n1 + n2 != n3)
		return false;
	if(n1 == 0)
		return s2 == s3;
	if(n2 == 0)
		return s1 == s3;
	
	//dp[i][j] would mean s1[0...i] can interleave with s2[0...j] to give s3[0...i+j+1]	
	vector<vector<bool> > dp(n1);
	for(int i = 0; i < n1; i++){
		dp[i].resize(n2);
	}

	//fill top row base case: dp[0][i] - > s1[0] interleave with s2[0...i] to give s3[0...i+1] 
	dp[0][0] = s1[0] + s2[0] == s3[0] + s3[1] ? true: false;
	for(int i = 1; i < n2; i++){
		if(s1[0] == s3[i+1] && s2[i] != s3[i+1]){
			dp[0][i] = (s2.substr(0,i+1) == s3.substr(0,i+1));
		}
		else if(s1[0] != s3[i+1] && s2[i] == s3[i+1]){
			dp[0][i] = dp[0][i-1];
		}
		else if(s1[0] != s3[i+1] && s2[i] != s3[i+1]){
			dp[0][i] = false;
		}
		else{//both match
			dp[0][i] = dp[0][i-1] || (s2.substr(0,i+1) == s3.substr(0,i+1));
		}
	}

	//fill left most column base calse: dp[i][0] - > s2[0] interleave with s1[0...i] to give s3[0...i+1]
	for(int i = 1; i < n1; i++){
		if(s2[0] == s3[i+1] && s1[i] != s3[i+1]){
			dp[i][0] = (s1.substr(0,i+1) == s3.substr(0,i+1));
		}
		else if(s2[0] != s3[i+1] && s1[i] == s3[i+1]){
			dp[i][0] = dp[i-1][0];
		}
		else if(s2[0] != s3[i+1] && s1[i] != s3[i+1]){
			dp[i][0] = false;
		}
		else{//both match
			dp[i][0] = dp[i-1][0] || (s1.substr(0,i+1) == s3.substr(0,i+1));
		}
	}
	
	for(int i = 1; i < n1; i++){
		for(int j = 1; j < n2; j++){
			if(s1[i] == s3[i+j+1] && s2[j] != s3[i+j+1]){
				dp[i][j] = dp[i-1][j];	
			}
			else if (s1[i] != s3[i+j+1] && s2[j] == s3[i+j+1]){
				dp[i][j] = dp[i][j-1];	
			}
			else if(s1[i] != s3[i+j+1] && s2[j] != s3[i+j+1]){
				dp[i][j] = false;
			}
			else{
				dp[i][j] = dp[i-1][j] || dp[i][j-1];
			}
		}
	}
	return dp[n1-1][n2-1];
    }
};


int main(){
	string s1 = "ab";
	string s2 = "sd";
	string s3 = "absd";
	Solution sol;
	cout << sol.isInterleave(s1, s2, s3) << endl;
}
