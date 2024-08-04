import copy


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def sorted_insert(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node
    current = sorted_head
    while current.next and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return sorted_head

def insertion_sort(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        current.next = None
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next

# Приклад використання
llist1 = LinkedList()
llist1.append(30)
llist1.append(20)
llist1.append(40)

llist2 = LinkedList()
llist2.append(20)
llist2.append(40)
llist2.append(60)

print("List 1:")
llist1.print_list()

print("List 2:")
llist2.print_list()

llist1_copy = copy.deepcopy(llist1) # to avoid overwriting whole structure
reversed_list = reverse_linked_list(llist1_copy.head)
print("Reversed List 1:")
current = reversed_list
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

sorted_list1 = insertion_sort(llist1.head)
print("Sorted List 1:")
current = sorted_list1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
sorted_list2 = insertion_sort(llist2.head)
print("Sorted List 2:")
current = sorted_list2
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

merged_list = merge_sorted_lists(sorted_list1, llist2.head)
print("Merged Sorted List:")
current = merged_list
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")