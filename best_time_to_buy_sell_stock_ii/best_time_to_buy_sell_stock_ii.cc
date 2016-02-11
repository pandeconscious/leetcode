class Solution {
public:
    int maxProfit(vector<int>& prices) {
		int profit = 0;
		int i = 0;
		int minInd = -1;
		int maxInd = -1;
		int n = prices.size();
		bool maxIndUpdated = false;
		if(n == 0 || n == 1)
			return 0;
		while(i < n-1){
			while(i < n-1 && prices[i] >= prices[i+1]){
				i++;	
			}
			if(i <= n-1){
				minInd = i;
				i++;
			}
			while(i < n-1 && prices[i] < prices[i+1]){
				i++;
			}
			if(i <= n-1){
				maxInd = i;
				maxIndUpdated = true;
				i++;
			}
			if(maxIndUpdated){
				profit += prices[maxInd] - prices[minInd];
				maxIndUpdated = false;
			}
		}
		return profit;	
    }
};
