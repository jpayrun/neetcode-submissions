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
        auto comp = [](ListNode *l1, ListNode *l2) {
            return l1->val > l2->val;
        };
        priority_queue <ListNode*, vector<ListNode*>, decltype(comp)> heap(comp);
        for (const auto l : lists) {
            heap.push(l);
        }

        while (!heap.empty()) {
            ListNode *temp = heap.top();
            heap.pop();
            cur->next = temp;
            cur = cur->next;
            temp = temp->next;
            if (temp != nullptr) {
                heap.push(temp);
            }
        }
        return dummy->next;
    }
};

