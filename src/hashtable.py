# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the key
        hashKey = self._hash_mod(key)

        # check for capacity
        # if hashKey >= self.capacity:
        #     self.resize()

        if self.storage[hashKey] is None:
            # store the value
            self.storage[hashKey] = LinkedPair(key, value)

        else:
            # reference the current node and loop through linked list
            curr_node = self.storage[hashKey]
            inserted = False

            # loop through linked list
            while inserted is False:

                # if next node exists
                if curr_node.next is not None:
                    # set current node to next node iterate
                    curr_node = curr_node.next
                else:
                    curr_node.next = LinkedPair(key, value)
                    inserted = True

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashKey = self._hash_mod(key)
        self.storage[hashKey] = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # hash the key
        hashKey = self._hash_mod(key)

        # check if exists
        if self.storage[hashKey] is None:
            print("Initial None check")
            return None

        curr_node = self.storage[hashKey]
        found = False

        # retrieve the value
        while found is False:
            if curr_node is None:
                return None

            if curr_node.key == key:
                found = True
                return curr_node.value
            else:
                curr_node = curr_node.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # store the old storage stuff
        old_storage = self.storage
        # double the capacity
        self.capacity *= 2
        # setup new storage
        self.storage = [None] * self.capacity

        # move values over
        for bucket in old_storage:

            # use insert method to populate new storage
            if bucket is not None:
                self.insert(bucket.key, bucket.value)

                if bucket.next is not None:
                    next_bucket = bucket.next
                    while next_bucket is not None:
                        self.insert(next_bucket.key, next_bucket.value)
                        next_bucket = next_bucket.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
