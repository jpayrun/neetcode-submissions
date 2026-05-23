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

        auto cmp = [](ListNode *a, ListNode *b) {
            return a->val > b->val;
        };

        priority_queue <ListNode*, vector<ListNode*>, decltype(cmp)> minheap(cmp);

        for (ListNode *l : lists) {
            minheap.push(l);
        }

        ListNode *res = new ListNode(0);
        ListNode *cur = res;

        while (!minheap.empty()) {
            ListNode *node = minheap.top();
            minheap.pop();
            cur->next = node;
            cur = cur->next;

            node = node->next;
            if (node != nullptr) {
                minheap.push(node);
            }
        }
        return res->next;
    }
};
