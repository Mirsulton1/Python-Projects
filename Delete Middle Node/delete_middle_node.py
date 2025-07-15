class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None    # Only one node, return empty list
        
        slow = head
        fast = head
        prev = None

        # Find middle using slow/fast pointers
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Delet the middle node
        prev.next = slow.next
        return head

# Helper: Create linked list from Python list
def create_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next
   
# Helper: Print linked list as list
def print_list(head):
    result = []
    while head: 
        result.append(head.val)
        head = head.next
    print(result)

# Test examples
sol = Solution()

head1 = create_list([1,3,4,7,1,2,6])
print_list(sol.deleteMiddle(head1))

head2 = create_list([1,2,3,4])
print_list(sol.deleteMiddle(head2))

head3 = create_list([1])
print_list(sol.deleteMiddle(head3))
