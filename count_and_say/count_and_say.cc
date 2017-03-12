class Solution {
public:
    string countAndSay(int n) {
	if(n == 1)
		return "1";
	if(n == 2)
	    return "11";
	
	string str = "11";
	for(int j = 3; j <= n; j++){
		string temp = "";
		int n = str.size();
		int count = 1;
		for(int i = 1; i < n; i++){
			if(str[i] == str[i-1]){
				count++;
			}
			else{
			    stringstream ss;
               		    ss << count;
			    temp += ss.str();
			    temp += str[i-1];
			    count = 1;
			}
		}
		stringstream ss;
	        ss << count;
		temp += ss.str();
		temp += str[n-1];
		str = temp;

	}
	return str;
    }
};
