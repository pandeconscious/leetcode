/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
	    if(head == NULL)
		    return NULL;
	    if(head->next == NULL)
		    return head;
	    int n = 0;
	ListNode* tail = NULL;
	ListNode* temp = head;
	while(temp != NULL){
		n++;
		if(temp->next == NULL){
			tail = temp;
		}
		temp = temp->next;	
	}
	
	k = k%n;
	
	if(k == 0)
		return head;

	temp = head;
	for(int i = 1; i <= n-k-1; i++){
		temp = temp->next;
	}
	tail->next = head;
	head = temp->next;
	temp->next = NULL;
	return head;
        
    }
};
