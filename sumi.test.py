import unittest
import sumi

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        z,y = sumi.ave([10,11,12])
        print(z,y)
        self.assertEqual(z,11)

if __name__ == '__main__':
    unittest.main()
