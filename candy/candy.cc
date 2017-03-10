#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
	int n = ratings.size();
	if(n == 1)
		return 1;
	vector<int> ind_cont_decr(n); //for each position store till what next position there is continuous decrease in values
	vector<int> ind_cont_incr(n); //for each position store till what next position there is continuous increase in values
	ind_cont_decr[n-1] = n-1;
	ind_cont_incr[n-1] = n-1;
	for(int i = n-2; i >= 0; i--){
		if(ratings[i] > ratings[i+1]){
			ind_cont_decr[i] = ind_cont_decr[i+1];
		}
		else{
			ind_cont_decr[i] = i;
		}
		if(ratings[i] < ratings[i+1]){
			ind_cont_incr[i] = ind_cont_incr[i+1];
		}
		else{
			ind_cont_incr[i] = i;
		}
	}

	vector<int> candies_given(n);	

	int i = 0;
	while(i < n){
		if(ind_cont_decr[i] == i && ind_cont_incr[i] == i){//means neither decrease nor increase post this position
			candies_given[i] = 1;	
			i++;continue;
		}
		if(ind_cont_incr[i] > i){//increase after this
			int incr_till = ind_cont_decr[ind_cont_incr[i]] == ind_cont_incr[i] ? ind_cont_incr[i] : ind_cont_incr[i]-1;
			candies_given[i] = 1;	
			for(int j = i+1; j <= incr_till; j++){
				candies_given[j] = candies_given[j-1] + 1;
			}
			i = incr_till+1;continue;
		}
		if(ind_cont_decr[i] > i){//decrease after this
			if(i == 0 || candies_given[i-1] == 1 || ratings[i-1] == ratings[i]){
				int decr_till = ind_cont_decr[i]-1;
				int start_val = ind_cont_decr[i] - i + 1;
				candies_given[i] = start_val;
				for(int j = i+1; j <= decr_till; j++){
					candies_given[j] = candies_given[j-1]-1;
				}
				i = decr_till+1;continue;
			}
			//this is the case where the peak value is decided based on looking down both sides of the peak
			int expected_val_as_per_left = candies_given[i-1]+1;
			int expected_val_as_per_right = ind_cont_decr[i] - i +1;
			int actual_val = max(expected_val_as_per_left, expected_val_as_per_right);
			candies_given[i] = actual_val;
			int next_val = expected_val_as_per_right-1;	
			candies_given[i+1] = next_val;
			int decr_till = ind_cont_decr[i]-1;
			for(int j = i+2; j <= decr_till; j++){
				candies_given[j] = candies_given[j-1]-1;	
			}
			i = decr_till+1;continue;
		}
	
	}

	int total = 0;	
	for(int i = 0; i < n; i++){
		total += candies_given[i];
		cout << candies_given[i] << endl;
	}
	cout << endl;

       	return total;
    }
};


int main(){
	vector<int> ratings;
	/*
	ratings.push_back(1);
	ratings.push_back(2);
	ratings.push_back(4);
	ratings.push_back(4);
	ratings.push_back(3);*/
	ratings.push_back(3);
	ratings.push_back(1);
	ratings.push_back(2);
	ratings.push_back(1);
	ratings.push_back(1);
	ratings.push_back(2);
	ratings.push_back(5);
	ratings.push_back(5);
	ratings.push_back(7);
	ratings.push_back(4);
	ratings.push_back(5);
	ratings.push_back(2);
	ratings.push_back(2);
	ratings.push_back(2);
	ratings.push_back(1);
	Solution sol;
	std::cout << sol.candy(ratings) << std::endl;
	return 0;
}
