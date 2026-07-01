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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *cur = head;
        ListNode *dummy = new ListNode();
        ListNode *d_cur = dummy;
        while (cur) {
            ListNode *m = mid(cur, k);
            if (m == NULL) {
                d_cur->next = cur;
                cur = m;
            } else {
                ListNode *t = m->next;
                ListNode *rev = reverse(cur, k);
                d_cur->next = rev;
                d_cur = cur;
                cur = t;
            }
        }

        return dummy->next;
    }
    ListNode *mid(ListNode *l, int k) {
        ListNode *cur = l;
        for (int i = 1; i < k && cur; i++) {
            cur = cur->next;
        }
        return cur;
    }
    ListNode *reverse(ListNode *l, int k) {
        ListNode *cur = l;
        ListNode *prev = NULL;
        while (cur && k > 0) {
            ListNode *t= cur->next;
            cur->next = prev;
            prev = cur;
            cur = t;
            k--;
        }
        return prev;
    }
};
