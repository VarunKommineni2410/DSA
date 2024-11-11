#l1 = [1,2,4] 
#l2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Initialize l1 and l2 as separate linked lists
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

dummy = cur = ListNode()

while l1 and l2:
    if l1.val < l2.val:
        cur.next = l1
        l1 = l1.next
    else:
        cur.next = l2
        l2 = l2.next
    cur = cur.next

if l1:
    cur.next = l1
elif l2:
    cur.next = l2

result = dummy.next

# Printing the merged linked list
while result:
    print(result.val, end=" ")
    result = result.next