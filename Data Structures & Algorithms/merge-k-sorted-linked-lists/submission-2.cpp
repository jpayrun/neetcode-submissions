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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        ListNode *dummy = new ListNode();
        ListNode *cur = dummy;

        auto cmp = [](ListNode *a, ListNode *b) {
            return a->val > b->val;
        };

        priority_queue <ListNode*, vector<ListNode*>, decltype(cmp)> minHeap(cmp);

        for (ListNode *l : lists) {
            if (l != nullptr) {
                minHeap.push(l);
            }
        }
        while (!minHeap.empty()) {
            ListNode *l = minHeap.top();
            minHeap.pop();
            cur->next = l;
            l = l->next;
            if (l != nullptr) {
                minHeap.push(l);
            }
            cur = cur->next;
        }
        return dummy->next;
    }
};

