#include<iostream>
#include<queue>

using namespace std;



class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
    
    }
   
    void adjust(int num){
	if(maxQ.top() < num){
		minQ.push(num);
	}
	else{
		minQ.push(maxQ.top());
		maxQ.pop();
		maxQ.push(num);
	}
    }

    void addNum(int num) {
	if(minQ.size() == 0 && maxQ.size() == 0){
		maxQ.push(num);
	}
	else if(maxQ.size() == 1 && minQ.size() == 0){
		adjust(num);	
	}
	else{
		if(minQ.size() == maxQ.size()){
			if(maxQ.top() < num){
				minQ.push(num);	
			}
			else{
				maxQ.push(num);		
			}
								
		}
		else if(minQ.size() < maxQ.size()){
			if(num > maxQ.top()){
				minQ.push(num);
			}
			else{
				minQ.push(maxQ.top());
				maxQ.pop();
				maxQ.push(num);
			}
		}
		else{
			if(num < minQ.top()){
				maxQ.push(num);
			}
			else{
				maxQ.push(minQ.top());
				minQ.pop();
				minQ.push(num);
			}
		}	

	}
    }
    
    double findMedian() {
    	if(maxQ.size() == minQ.size()){
		return ((double)maxQ.top() + (double)minQ.top())/2;
	}	
	else if(maxQ.size() < minQ.size()){
		return (double)minQ.top();
	}
	else{
		return (double)maxQ.top();
	}
    }

private:
	priority_queue<int, vector<int> ,greater<int> > minQ; 
	priority_queue<int, vector<int> > maxQ;	    
};

int main(){
       	MedianFinder* obj = new MedianFinder();
	obj->addNum(2);
	cout << obj->findMedian() << endl;
	obj->addNum(3);
	cout << obj->findMedian() << endl;
	obj->addNum(4);
	cout << obj->findMedian() << endl;
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
