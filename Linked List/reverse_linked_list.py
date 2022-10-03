import linked_list

list = linked_list.LinkedList()
list.headval = linked_list.Node(1)
e2 = linked_list.Node(2)
e3 = linked_list.Node(3)
e4 = linked_list.Node(4)
e5 = linked_list.Node(5)

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

# Link third Node to fourth node
e3.nextval = e4

# Link fourth Node to fifth node
e4.nextval = e5


def reverseList(self):
    curr = self.headval
    prev = None
    while curr is not None:
        next = curr.nextval
        curr.nextval = prev
        prev = curr
        curr = next
    self.headval = prev




reverseList(list)

list.listprint()