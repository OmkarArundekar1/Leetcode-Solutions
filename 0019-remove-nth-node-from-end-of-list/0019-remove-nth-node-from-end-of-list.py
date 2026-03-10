# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trial=ListNode(0,head)
        p=trial
        q=trial
        for i in range(n+1):
            q=q.next
        while q:
            q=q.next
            p=p.next
        p.next=p.next.next
        return trial.next
        
        