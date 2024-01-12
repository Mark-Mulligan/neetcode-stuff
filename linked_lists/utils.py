from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(list_values: List[int]):
    list_nodes: List[ListNode] = []

    for item in list_values:
        list_nodes.append(ListNode(item))

    for i, node in enumerate(list_nodes):
        if i < len(list_nodes) - 1:
            node.next = list_nodes[i + 1]

    return list_nodes[0]


def print_linked_list(head: ListNode):
    curr = head

    while curr:
        print(curr.val)
        curr = curr.next


if __name__ == "__main__":
    print("Script run directly")
    head = create_linked_list([1, 2, 3, 4, 5])

    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
else:
    print("Script imported as a module")
