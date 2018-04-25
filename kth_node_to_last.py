class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def kth_to_last_node(self, k, head):
        list_length = 1
        current_node = head

        while current_node.next:
            current_node = current_node.next
            list_length += 1

        how_far_to_go = list_length - k
        current_node = head
        for i in xrange(how_far_to_go):
            current_node = current_node.next

        return current_node
            

        
a = LinkedListNode("Angel food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

kth_to_last_node(2,a)
