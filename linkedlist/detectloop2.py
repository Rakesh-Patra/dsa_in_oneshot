class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast==slow:
            slow=head
            if slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        return None