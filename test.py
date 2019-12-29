import unittest
from project1 import ListOfRandomIntegers
from project2 import WordList

class TestProject1(unittest.TestCase):

    def setUp(self):
        self.LORI = ListOfRandomIntegers()
        self.LORI.sequence = [-1, 2, 3, 4]
        
    def testSequence(self):
        self.assertEqual(self.LORI.sequence, [-1,2,3,4])

    def testLength(self):
        self.assertEqual(self.LORI.getLength(), 4)

    def testLargest(self):
        self.assertEqual(self.LORI.getLargest(), 4)

    def testSmallest(self):
        self.assertEqual(self.LORI.getSmallest(), -1)

    def testSum(self):
        self.assertEqual(self.LORI.getSum(), 8)

    def testGenerateSeq(self):
        self.LORI.LOWER = 1
        self.LORI.UPPER = 5
        self.LORI.LENGTH = 5
        self.LORI.generateSequence()
        self.assertEqual(self.LORI.getLength(), 5)

if __name__ == "__main__":
    unittest.main()