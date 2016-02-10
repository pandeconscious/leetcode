class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
		if(n == 0 || n == 1)
			return 0;
		int minInd = 0;
		int maxSoFar;
		while(minInd <= n-2 && prices[minInd] > prices[minInd+1]){
			minInd++;
		}
		if(minInd == n-1)
			return 0;
		maxSoFar = prices[minInd+1] - prices[minInd];
		int i = minInd+2;
		while(i < n){
			if(prices[i] >= prices[minInd] && prices[i] - prices[minInd] > maxSoFar)
				maxSoFar = prices[i] - prices[minInd];
			else if(prices[i] < prices[minInd])
				minInd = i;
			i++;
				
		}

		return maxSoFar;
    }
};
