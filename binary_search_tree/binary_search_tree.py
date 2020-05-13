"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BinarySearchTree class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BinarySearchTree class.
"""

# each node in a BST is a BST !!!


class BinarySearchTree:
    def __init__(self, value):
        # ROOT VALUE #
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # PLAN #
        # check if empty
        # if empty put node here/at root
        ## ** We cant do the above because our BTSNode is initialized with a value ** ##
        # if new < node.value
        # leftnode.insert value
        # if left does not exist
        # create left
        #   else:
        # leftnode.insert value
        # if >=
        # if right does not exist
        # create right
        # else:
        # rigtnode.insertvalue
        # rightnode.insert value

        if value < self.value:              # if our incoming value < the root value
            if self.left is None:           # and if self.left is None
                # then our left value is a new node/BST with the value passed in
                self.left = BinarySearchTree(value)
            else:
                # otherwise we call on our left node and recurse until left is none so we can insert the new node value
                self.left.insert(value)

        else:   # if root value is >= the incoming value
            if self.right is None:
                # create a right node/BST
                self.right = BinarySearchTree(value)
            else:
                # otherwise we will recurse right until we can insert a value to the right
                self.right.insert(value)

##############            ##############
############## END INSERT ##############
##############            ##############

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                # we must return our function call in order to get an output
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        # if node is none return False BASE CASE
        # if node.value == findvalue: return True
        # else:
        # if find < node.value:
        # if node.left then find on left node:
        # else:
        # if node.right: find on right node

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # follow the right until the end
        # if we have a right node then return it recursively
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn function on each node
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
