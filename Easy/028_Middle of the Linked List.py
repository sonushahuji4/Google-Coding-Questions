# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
