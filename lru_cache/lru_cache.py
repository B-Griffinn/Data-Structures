from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        # self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # What if key is not in cache - return none
        if key not in self.storage:
            return None

        else:
            # if key is in cache
            # then move it to MRU
            # create a placeholder for our node in our storage
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value
            # node value is in our tuple sub 1
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # set scenarios

        # if item/key already exists
        if key in self.storage:
            # overwrite value
            # where is the value stored?
            # we can get the node from our storages key
            node = self.storage[key]
            # the nodes value is a new tuple with the old key and new value
            node.value = (key, value)
            # move value to the tail (whic is most recently used)
            self.order.move_to_end(node)
            return  # exit function

        # size is at limit
        if len(self.order) == self.limit:
            # evict oldest node
            # we have 2 references to it already - (LL and dict)
            # remove from LL and dict
            index_of_oldest = self.order.head.value[0]
            # now delete the found index
            del self.storage[index_of_oldest]
            # once removed from dict
            self.order.remove_from_head()

        # add newest node to end/tail
        # size is not a limit
        # 1a. add it to order
        # 1b. a tuple is used bc we just need to store key/vals
        self.order.add_to_tail((key, value))

        # add it to storage
        # adding the whole node to the stoarage[key] bc it will let us find both from item when getting or moving things around
        self.storage[key] = self.order.tail
