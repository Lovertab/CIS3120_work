import unittest
def is_odd(n):
    return n%2 ==1

class TestOddCheck(unittest.TestCase):
    def test_is_odd(self):
        self.assertEqual(is_odd(3), True)
        self.assertEqual(is_odd(4), False)
        self.assertEqual(is_odd(5), True)
        self.assertEqual(is_odd(6), False)
        
if __name__=='__main__':
    unittest.main()