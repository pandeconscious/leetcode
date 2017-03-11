#include<vector>
#include<iostream>
#include<algorithm>
#include<cstdlib>

using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
	int n = nums.size();	        
	//do partitioning of negative and positive numbers
	int last_neg = 0, curr = 0; //last_neg is the index to the right of last non positive element in the paritioned array so far
	while(curr < n){
		if(nums[curr] <= 0){
			if(nums[curr] == 0)
				nums[curr] = -1; //zeros will be confusing as sentinels because their negative and positive value is same
			swap(nums[last_neg], nums[curr]);
			last_neg++;
		}			
		curr++;
	}
	/*cout << last_neg << endl;

	for(int i = 0; i < n; i++){
		cout << nums[i] << " ";
	}
	cout << endl;*/

	if(last_neg == n)
		return 1;
	

	//ith index will correspond to i+1th value
	for(int i = last_neg; i < n; i++){
		//cout << "outer nums i  " << nums[i] << endl;
		if(abs(nums[i]) <= n && abs(nums[i]) >= 1){
			//cout << "nums i  " << nums[i] << endl;
			if(abs(nums[i])-1 < last_neg && nums[abs(nums[i])-1] < 0){
				//cout << "ind " << i << endl;
				nums[abs(nums[i])-1] *= -1;
			}
			else if(abs(nums[i])-1 >= last_neg && nums[abs(nums[i])-1] > 0){
				nums[abs(nums[i])-1] *= -1;
			}
		}
	}

	/*cout << endl;
	
	for(int i = 0; i < n; i++){
		cout << nums[i] << " ";
	}
	
	cout << endl;*/

	for(int i = 0; i < n; i++){
		if(i < last_neg && nums[i] < 0){
			return i+1;
		}
		if(i >= last_neg && nums[i] > 0){
			return i+1;
		}
	}

	return n+1;
    }
};


int main(){
	Solution sol;
	vector<int> vec;
	vec.push_back(1);
	vec.push_back(2);
	/*
	vec.push_back(-1);
	vec.push_back(-9);
	vec.push_back(0);
	vec.push_back(0);
	vec.push_back(10);
	vec.push_back(8);
	vec.push_back(2);
	vec.push_back(8);*/
	cout << endl;
	cout<< sol.firstMissingPositive(vec) << endl;
	return 0;
}
