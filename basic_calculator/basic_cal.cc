#include <iostream>
#include <stack>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

class Solution {
public:
    int calculate(string s) {
	stack<int> numStack;//sores numbers
	stack<char> operStack; //stores operaraotrs

	numStack.push(0);	
	operStack.push('+');

	int n = s.size();
	int i = 0;
	while(i < n){
		if(s[i] == ' '){
			i++;
		}
		else if(s[i] == '('){
			numStack.push(0);	
			operStack.push('+');
			i++;
		}
		else if(s[i] == ')'){
			if(!operStack.empty()){
				char opr = operStack.top();	
				int currNum = numStack.top();
				operStack.pop();
				numStack.pop();
				int prevNum = numStack.top();
				numStack.pop();
				numStack.push(evalu(prevNum, currNum, opr));
			}
			i++;
		}
		else if(s[i] == '+' || s[i] == '-'){
			operStack.push(s[i]);
			i++;
		}
		else{ //integer seen - fetch it
			int len = 0;	
			int j = i;
			while(isdigit(s[i])){
				len++;
				i++;
			}
			int currNum = atoi(s.substr(j, len).c_str());
			char opr = operStack.top();	
			int prevNum = numStack.top();
			operStack.pop();
			numStack.pop();
			numStack.push(evalu(prevNum, currNum, opr));
		}

	}
	return numStack.top();
    }

private:
    int evalu(int prev, int curr, char op){
	if(op == '+'){
		return prev + curr;
	}
	else{
		return prev  - curr;
	}
    }
};

int main(){
	Solution sol;
	cout << sol.calculate("(1+(4+5+2)-3)+(6+8)") << endl;
	return 0;
}
