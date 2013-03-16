import unittest
import random
from array import array
from infinitearray import infarray

class FuzzTest(unittest.TestCase):
    def test(self):
        array1 = array('B', [0]*100000)
        array2 = infarray('B')
        for i in xrange(10000):
            # Put some random data in
            addr = random.randint(0, 100000-1)
            value = random.randint(0, 255)
            array1[addr] = value
            array2[addr] = value
        for i in xrange(100000):
            # Read some random addresses
            addr = random.randint(0, 100000-1)
            value = random.randint(0, 255)
            self.assertEqual(array1[addr], array2[addr])
        print array2.density()
            
if __name__ == "__main__":
    unittest.main()
        
