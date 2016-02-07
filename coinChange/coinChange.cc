class Solution {
private:
	vector<int> memo;
	bool minCoins(vector<int>& coins, int amount, int& ans){
		if(amount < 0){
			return false;
		}
		if(memo[amount] == INT_MAX){
			return false;
		}
		else if(memo[amount] != -1){
			ans = memo[amount];	
			return true;
		}
		else{
			bool isPossible = false;
			int minCurrent = INT_MAX;
			for(int i = 0; i < coins.size(); i++){
				int ans = 0;
				if(minCoins(coins, amount - coins[i], ans)){
					minCurrent =  min(minCurrent, ans);
					isPossible = true;
				}
			}
			if(isPossible){
				memo[amount] = 1 + minCurrent;
				ans = memo[amount];
				return true;
			}
			else{
				memo[amount] = INT_MAX;
				return false;
			}
		}
	}
public:
    int coinChange(vector<int>& coins, int amount) {
		if(amount == 0)
			return 0;
		int n = coins.size();
		if(n == 0)
			return -1;
		memo.resize(amount+1, -1);
		memo[0] = 0;
		for(int i = 0; i < n; i++){
			if(coins[i] <= amount)
				memo[coins[i]] = 1;
		}
		int ans = 0;
		if(minCoins(coins, amount, ans))
			return ans;
		else
			return -1;
    }
};
