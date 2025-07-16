class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        # Step 1: Use fast and slow pointer to find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Calculate max twin sum
        max_sum = 0
        first = head
        second = prev
        while second:
            twin_sum = first.val + second.val
            max_sum = max(max_sum, twin_sum)
            first = first.next
            second = second.next

        return max_sum

# Helper to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# --- MAIN DRIVER ---
if __name__ == "__main__":
    try:
        user_input = input("Enter even number of node values separated by space: ")
        values = list(map(int, user_input.strip().split()))

        if len(values) % 2 != 0:
            print("Error: The number of nodes must be even.")
        else:
            head = create_linked_list(values)
            sol = Solution()
            result = sol.pairSum(head)
            print("Maximum twin sum:", result)
    except Exception as e:
        print("Invalid input. Please enter integers only.")
        print("Error:", e)
