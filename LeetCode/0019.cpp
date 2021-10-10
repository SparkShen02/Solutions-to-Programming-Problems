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
    // Time complexity: O(n), Space complexity: O(1). 
    ListNode* removeNthFromEnd(ListNode* head, int n) {        
        // Count the size of the linked list
        int size = 0;
        ListNode* node = head; 
        while (node != nullptr)
        {
            size += 1;
            node = node->next; 
        } 

        int target = size - n; 
        // Special case, remove the head node 
        if (target == 0)
            return head->next; 

        // Get to the node before the node we want to remove
        int nodeInd = 1;
        node = head;
        for (; nodeInd < target; nodeInd++)
            node = node->next;

        // Remove the next node
        node->next = node->next->next;

        return head;
    }
};