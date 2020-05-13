"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create list node
        new_node = ListNode(value)
        # increment the list by 1
        self.length += 1
        # check if list is empty
        if not self.head and not self.tail:
            # then we need to assign out head and tail to be our new_node
            self.head = new_node
            self.tail = new_node
        else:
            # prepend our new_node to the head.
            new_node.next = self.head  # our new node's next prop is going to be the original head
            # our original head's prev pointer is pointing to our new_node
            self.head.prev = new_node
            # udpate our head to be the new node - this order preserves our original head
            self.head = new_node
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # save the heads value so we do not lose it in reassignment
        value = self.head.value
        # call the delete method on the head and let it handle all the pointers
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create list node
        new_node = ListNode(value)
        # increment the list by 1
        self.length += 1
        # check if list is empty
        if not self.head and not self.tail:
            # then we need to assign out head and tail to be our new_node
            self.head = new_node
            self.tail = new_node
        else:
            # prepend our new_node to the head.
            new_node.prev = self.tail  # our new node's next prop is going to be the original tail
            # our original tail's prev pointer is pointing to our new_node
            self.tail.next = new_node
            # udpate our tail to be the new node - this order preserves our original tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if we are at head
        if node is self.head:
            return
        # add new node
        # add that node to head
        # delete old node
        self.add_to_head(node.value)
        # use self.delete() to handle all meta data stuff
        self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # add new node
        # add that node to tail
        # delete old node
        if node is self.tail:
            return
        value = node.value
        self.add_to_tail(node.value)
        # use self.delete() to handle all meta data stuff
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        # TODO - do we need error checking if node is not in list?
        # if node to delete is the only node...
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # what if we want to delete the head?
        elif node is self.head:
            # reassing the head to the nodes next
            self.head = node.next
            node.delete()  # delete the node
        # what if we want to delete the tail?
        elif node is self.tail:
            # reassing the tail to the nodes prev
            self.tail = node.prev
            node.delete()
        # what if we want to delete a node between 2 nodes?
        else:
            # just delete it bc we know where it is if we get here
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # tracking node - start at head
        current = self.head
        max_val = self.head.value
        # loop through the nodes list
        while current is not None:
            # compare a current 2nd place to 1st place
            if current.value >= max_val:
                max_val = current.value
            current = current.next
        # return max found
        return max_val
