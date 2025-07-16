class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next   # Save next node
            curr.next = prev        # Reverse the link
            prev = curr             # Move prev forward
            curr = next_temp        # Move current forward

        return prev  # New head
    
# Helper: Convert Python list to linked list
def create_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper: Convert linked list to Python list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("Reversed List:", result)

# ---- MAIN DRIVER ----
if __name__ == "__main__":
    try:
        user_input = input("Enter linked list values separated by spaces: ")
        values = list(map(int, user_input.strip().split()))
        head = create_list(values)

        sol = Solution()
        reversed_head = sol.reverseList(head)

        print_list(reversed_head)
    except Exception as e:
        print("Invalid input. Please enter only integers separated by spaces.")
        print("Error:", e)
