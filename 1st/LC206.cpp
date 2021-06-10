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
//iterative 有时间可以考虑一下
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head) return nullptr;
        ListNode* temp = new ListNode;
        return helper(head, temp);
        
    }
    
    ListNode* helper(ListNode* head, ListNode* res){
        
        res->val = head->val;
        if(!head->next) return res;
        ListNode* temp = new ListNode;
        temp->next = res;
        return helper(head->next, temp);
    }
};