/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
		if(n == 0){
			vector<TreeNode*> x;
			return x;
		}

 	   vector<vector<vector<TreeNode*> > > dp(n+1);//dp[i][j] stores all the BSTs possible for {i, i+1,...,j}  
    	for(int i = 0; i < n+1; ++i){
			dp[i].resize(n+1);
		}
		for(int L = 1; L <= n; ++L){
			for(int i = 1; i <= n - L + 1; ++i){
				int j = i + L -1;
				if(L == 1){
					TreeNode* node = new TreeNode(i);
					dp[i][i].push_back(node);
				}
				else{
					for(int k = i; k <= j; ++k){
						if(k == i){
							int num = dp[k+1][j].size();
							for(int a = 0; a < num; ++a){
								TreeNode* node = new TreeNode(k);
								node->left = NULL;
								node->right = dp[k+1][j][a];
								dp[i][j].push_back(node);
							}
						}
						else if(k == j){
							int num = dp[i][k-1].size();
							for(int a = 0; a < num; ++a){
								TreeNode* node = new TreeNode(k);
								node->right = NULL;
								node->left = dp[i][k-1][a];
								dp[i][j].push_back(node);
							}
						}
						else{
							int numL = dp[i][k-1].size();
							int numR = dp[k+1][j].size();
							for(int a = 0; a < numL; a++){
								for(int b = 0; b < numR; b++){
									TreeNode* node = new TreeNode(k);
									node->left = dp[i][k-1][a];
									node->right = dp[k+1][j][b];
									dp[i][j].push_back(node);
								}
							}
						}
					}
				}
			}
		}
		return dp[1][n];
	}
};
