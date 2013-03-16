# An infinite and sparse array; automatically set to all zeros.
# By Nick O'Dell

from array import array
from collections import defaultdict
from math import floor
ALLOC_SIZE = 24 # Number of elements to allocate at once
class infarray:
    def __init__(self, typecode, block_size = ALLOC_SIZE):
        self._initial_list = [0] * block_size
        self._initializer = lambda: array(typecode, \
                                          self._initial_list)
        self._datastore = defaultdict(self._initializer)
        self._sets = 0
        self._alloc_size = block_size
        self._example_array = self._initializer()
    def _keycheck(self, key):
        if type(key) not in (type(0), type(0L)):
            raise ValueError("key must be integer")
        if key < 0:
            raise ValueError("It's not infinite in that \
                    direction")
    def __getitem__(self, key):
        self._keycheck(key)
        outer_addr = int(floor(key/self._alloc_size))
        inner_addr = key % self._alloc_size
        if outer_addr in self._datastore:
            return self._datastore[outer_addr][inner_addr]
        else:
            return self._example_array[0]
    
    def __setitem__(self, key, value):
        self._keycheck(key)
        outer_addr = int(floor(key/self._alloc_size))
        inner_addr = key % self._alloc_size
        if self._datastore[outer_addr][inner_addr] == 0:
            self._sets += 1
        self._datastore[outer_addr][inner_addr] = value
        
    def density(self):
        length = float(len(self._datastore))
        return self._sets / (self._alloc_size * length)
