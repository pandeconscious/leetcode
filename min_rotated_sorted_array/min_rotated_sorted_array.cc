class Solution {
public:
    int findMin(vector<int>& nums) {
	int n = nums.size();
	return findMinUtil(nums, 0, n-1);	
    }
private:
    int findMinUtil(vector<int>& nums, int left, int right){
	if(left == right)
		return nums[left];
	if(right - left == 1)
		return min(nums[left], nums[right]);
	if(right - left == 2)
		return min(min(nums[left], nums[left+1]), nums[left+2]);
	if(nums[left] < nums[right])
		return nums[left];
	int m = left+ (right - left)/2;
	if(nums[m] < nums[m-1])
		return nums[m];
	if(nums[m] > nums[m+1])
		return nums[m+1];
	if(nums[m] < nums[left]){
		return findMinUtil(nums, left, m-1);
	}
	if(nums[m] > nums[right]){
		return findMinUtil(nums, m+1, right);
	}
	return min(findMinUtil(nums, left, m-1), findMinUtil(nums, m+1, right));
    }
};



