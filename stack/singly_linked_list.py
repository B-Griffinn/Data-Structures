class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    # get the node value
    def get_value(self):
        return self.value

    # get the next node pointer
    def get_next(self):
        return self.next_node

    # set given node to be the new next_node
    def set_next(self, new_next):
        # set this nodes next_node reference to the passed in node
        self.next_node = new_next

# ll = Node(1)
# ll.next_node = Node(2)
# ll.next_node.new_node = Node(3)

########### END OF NODE CLASS ###########

########### BEGIN LINKED LIST ###########


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None

    # add to the end of our list
    def add_to_tail(self, value):
        # regardless if the list is empty or not, we need to wrap the value in a node
        new_node = Node(value)
        # what if list is empty?
        if not self.head:
            self.head = new_node
        # what if list is not empty?
        else:
            # what node do we want to add the new node to?
            # the last node in the list
            # we can get the last node in the list by traversing it
            current = self.head  # start at the head
            while current.get_next() is not None:  # while there is a next node in line keep going
                # update current to be next node in line until next_node == NONE
                current = current.get_next()
            # we are at the end of the linked list
            # current is now the last node in the list so we need to set the new node to be currents next_node
            current.set_next(new_node)

    def add_to_head(self, value):
        # regardless if the list is empty or not, we need to wrap the value in a node
        new_node = Node(value)

        # what if list is empty?
        if not self.head:
            self.head = new_node
        # what if list is NOT empty?
        else:
            # what node do we want to add the new node to?
            # the first node in the list
            # we can get the head from self.head
            # change current head pointer to be next
            current = self.head
            current.set_next(None)
            self.head = new_node

    # remove node from the head of list
    def remove_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if the list is NOT empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # replace the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value
