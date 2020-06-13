import unittest
import sumi

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        z,y = sumi.ave([4,5,6,7,8])
        print(z,y)
        self.assertTrue(z,5)

if __name__ == '__main__':
    unittest.main()
