import unittest
import sumi

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        z,y = sumi.ave([10,11,12,13,14])
        print(z,y)
        self.assertEqual(z,12)

if __name__ == '__main__':
    unittest.main()
