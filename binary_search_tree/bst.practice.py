"""
 * My Practice BST methods
"""


class BST:
    # intialize a value, left, and right
    def __init__(self, value):  # now we always have a value at the beginning of our tree
        self.value = value  # self.value is our root node
        self.left = None
        self.right = None

    # insert the given value into the tree using recursion
    def insert(self, value):
        # PLAN #
        # decide which way to look first
        # compare value to the left side
        if value < self.value:  # if our value is smaller than the root node we will look left
            if self.left is None:
                # if there is no left we need to add a new node to the left leaf using our value input
                self.left = BST(value)
            else:
                # otherwise we call on our left node to recurse until left is none so we can isnert the new node value
                self.left.insert(value)
        # OTHERWISE we look right and try to insert as soon as we find an empty position for our value
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    # search for the target in our BST
    # if target exists return true
    # else return false
    def contains(self, target):
        # PLAN #
        # check if root value is the target first BASE CASE
        # compare target to root value
        # if target is < root value then we look left
        # if target is >= root value then we look right
        # return our recursive call being that we are looking for something and not executing something

        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # being that the right most node is our largest value then we know we need to look all the way right
        ## PLAN ##
        # check if there is a right node and if there is
        # return our recursive function which will get us to the end of our list
        # otherwise if there is not right then we are at the largest node so return its value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on the root node
        fn(self.value)
        # then check if there is a left node
        # if there is - call the fn on that entire side
        # then check the right side
        # if there is a right - call the fn on that entire side

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
