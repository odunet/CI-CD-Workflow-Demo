import unittest
import sumi

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        z,y = sumi.ave()
        k = round(sum(y)/len(y),2)
        self.assertTrue(z,k)

if __name__ == '__main__':
    unittest.main()
