class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize the dummy node and the current node
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Iterate while there are nodes to process or a carry to add
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of values and carry
            total = val1 + val2 + carry
            
            # Update the carry for next iteration
            carry = total // 10
            
            # Create new node for the sum of this digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next node if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next