class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

# Helper to create linked list from list
def create_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper to print linked list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("Reordered List:", result)

if __name__ == "__main__":
    try:
        user_input = input("Enter linked list values separated by space: ")
        values = list(map(int, user_input.strip().split()))

        head = create_list(values)
        sol = Solution()
        result_head = sol.oddEvenList(head)
        print_list(result_head)
    except Exception as e:
        print("Invalid input. Only integers separated by space.")
        print("Error:", e)
