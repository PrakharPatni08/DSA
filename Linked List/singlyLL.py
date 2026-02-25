class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else :
            count = 0
            prev_node = None
            current = self.head
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                temp.next = None
                del temp
                return
            else:
                found = False
                prev_node = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev_node = temp
                    temp = temp.next
                
                if found:
                    prev_node.next = temp.next
                    return
                else:
                    print("Node not found")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.insert_at(35, 3)
sll.delete(20)
sll.traverse()