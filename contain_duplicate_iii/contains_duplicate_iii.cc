#include <iostream>
#include<set>

using namespace std;


class Solution {
private:
	bool foundWithinBounds(set<int>& currSet, int val, int t){
		set<int>::iterator itr = currSet.upper_bound(val);
		if(itr == currSet.end()){
			if((long long)val - (long long)*currSet.rbegin() <= (long long)t)
				return true;
		}
		else if(itr == currSet.begin()){
			if((long long)*currSet.begin() - (long long)val <= (long long)t)
				return true;	
		}
		else{
			long long larger_val = (long long)*itr; 
			--itr;
			long long smaller_val = (long long)*itr;

			if(larger_val - val <= (long long)t)
				return true;
			if(val - smaller_val <= (long long)t)
				return true;
		}
		return false;
	}

public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
	int n = nums.size();
	if(n == 0 || n == 1 || k <= 0 || t < 0){
		return false;
	}
	set<int> currSet;
	int i = 0;
	while(i < n){
		if(currSet.size() >= k+1){
			currSet.erase(nums[i-k-1]);
		}
		if(!currSet.empty()){
			if(foundWithinBounds(currSet, nums[i], t))
				return true;
		}
		currSet.insert(nums[i]);
		i++;
	}
	return false;
    }
};

int main(){
	
	return 0;
}
