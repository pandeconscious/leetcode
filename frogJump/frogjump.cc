#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    bool canCross(vector<int>& stones) {
       int n = stones.size();
      	int MAXJUMP = n; 
	vector<vector<bool> > dp(n);
	for(int i = 0; i < n; i++){
		dp[i].resize(MAXJUMP);
	}
	
	for(int i = 0; i < n; i++){
		for(int j = 0; j < MAXJUMP; j++){
			dp[i][j] = false;
		}
	}
	
	//dp[i][j] means if stone at index i can be reached by making a jump of j units from the previous stone

	dp[1][1] = stones[1] == 1 ? true: false;
	
	for(int i = 2; i < n; i++){
		for(int j = 1; j <= i; j++){//stone at index i can be reached on by a max possible jump of i
			//find the index that contains position stones[i] - j
			vector<int>::iterator itr = lower_bound(stones.begin(), stones.begin()+i, stones[i]-j);		
			if(itr != stones.begin()+i){//this means all are strictly less than stones[i]-j
				int k = itr - stones.begin();
				if(stones[k] == stones[i]-j){//if such a stone found
					dp[i][j] = dp[k][j] || dp[k][j-1];	
					if(j+1 < MAXJUMP){
						dp[i][j] = dp[i][j] || dp[k][j+1];
					}
				}
			}
		}
	}

	for(int j = 1; j < MAXJUMP; j++){
		if(dp[n-1][j] == true)
			return true;
	}
	return false;
    }
};


int main(){
	Solution sol;
	vector<int> v;
	v.push_back(0);
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(4);
	v.push_back(8);
	v.push_back(9);
	v.push_back(11);
	cout << sol.canCross(v) << endl;
}
