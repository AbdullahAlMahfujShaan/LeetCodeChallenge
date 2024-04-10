class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        
        ListNode* l3 = new ListNode(0);
        ListNode* head = l3;
        while(true){
            
            int sum = l3->val;
            
            if(l1 != NULL){
                sum += l1->val;
                l1 = l1->next;
            }
            
            if(l2 != NULL){
                sum += l2->val;
                l2 = l2->next;
        }
            
            l3->val = (sum%10);
            if ((l1==NULL) && (l2 == NULL) && sum<10){
                break;
            }
            
            l3->next = new ListNode(sum/10);
            l3 = l3->next;   
    }
        return head;
    }
};