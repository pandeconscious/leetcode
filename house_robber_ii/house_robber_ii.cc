class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0)
            return 0;
        if(n == 1)
            return nums[0];
        if(n == 2)
            return max(nums[0], nums[1]);
        if(n == 3)
            return max(max(nums[0], nums[1]), nums[2]);
        vector<int> dpInc(n); //means 0th index house is included in the solution
        vector<int> dpExc(n); //means 0th index house is excluded in the solution
        dpInc[0] = nums[0];
        dpExc[0] = 0;
        dpInc[1] = nums[0];
        dpExc[1] = nums[1];
        for(int i = 2; i < n; ++i){
            if(i == n-1){
                return max(nums[n-1] + dpExc[n-3], max(dpInc[n-2], dpExc[n-2]));
            }
            else{
                dpInc[i] = max(dpInc[i-1], nums[i] + dpInc[i-2]);
                dpExc[i] = max(dpExc[i-1], nums[i] + dpExc[i-2]);
            }
        }
    }
};
