# [3] ->[4]
# data, next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
print(node.data)

class LinkedList:
    def __init__(self, data):
        self.head =Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            cur.next = Node(data)
            print(cur.data)

    def print_all(self):
        print("hihihi")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


# [3] -> [4] -> [5] -> [6] -> None

linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
