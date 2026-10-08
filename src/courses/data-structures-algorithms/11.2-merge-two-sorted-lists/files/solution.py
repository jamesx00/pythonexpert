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


def merge_two_lists(list1, list2):
    return None


def merge_two_lists(list1, list2):
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return dummy.next
