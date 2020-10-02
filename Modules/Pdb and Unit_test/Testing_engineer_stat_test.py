import unittest
from Devp import mean,median,mode


class StatsTest(unittest.TestCase):
    def setUp(self):
        self.data = [10,20,30]

    def testMean(self):
        self.assertEqual(20,mean(self.data))
        self.data.append(90)
        self.assertEqual(37.5,mean(self.data))

    def testMedian(self):
        self.assertEqual(20,median(self.data))
        self.data.insert(0,12)
        self.assertEqual(16.0,median(self.data))

    def testMode(self):
        self.data.append(20)
        self.assertEqual(20,mode(self.data))
        
        
        

unittest.main()
