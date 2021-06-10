/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(INT_MIN);
        ListNode* head = new ListNode();
        int l1_num, l2_num;
        head = res;
        while(true){
            if(!l2 && !l1) break;
            if(l2) l2_num = l2->val;
            if(l1) l1_num = l1->val;
            if(l1_num >= l2_num && l2){
                insert_after(res, l2->val); 
                l2 = l2->next;
            }else if (l1_num < l2_num && l1){
                insert_after(res, l1->val);
                l1 = l1->next;
            }else if(l1_num >= l2_num && !l2){
                insert_after(res, l1->val);
                l1 = l1->next;
            }else if (l1_num < l2_num && !l1){
                insert_after(res, l2->val);
                l2 = l2->next;
            }
            res = res->next;
        }
        return head->next;
    }
    
    void insert_after(ListNode* head, int val){
        ListNode* temp = new ListNode();
        ListNode* data = new ListNode(val);
        temp = head->next;
        head -> next = data;
        data -> next = temp;
    }
};