class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(node):
    result = []
    seen = set()
    while node and id(node) not in seen:
        seen.add(id(node))
        result.append(node.val)
        node = node.next
    return result


def reverse_k_group(head, k):
    return head


def reverse_k_group(head, k):
    def get_kth(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, curr = group_next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next
