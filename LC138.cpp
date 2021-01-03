/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

//难点在于，有一个random指针指向一个已创建的node，如果在递归过程中，这个random指针指向的node还没有被创建，那就创建，但是你不知道random指针对应的是哪个已知或者未知的node，
//解决方法是搞个表，记录哪些已经拷过了，哪些没有 https://www.cnblogs.com/grandyang/p/4261431.html
class Solution {
public:
    Node* copyRandomList(Node* head) {
        vector<Node*> visited;
        Node* res=helper(head, visited);
        
        return res;
    }
    Node* helper(Node* current, vector<Node*>& visited){
        if(!current) return nullptr;
        auto it=find(visited.begin(), visited.end(), current);
        if(it!= visited.end()) return *it;
        visited.push_back(current);
        Node *temp_copied = new Node(current->val);
        temp_copied->next = helper(current->next, visited);
        temp_copied->random = helper(current->random, visited);
        return temp_copied;
    }
};