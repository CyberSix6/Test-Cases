import unittest

from MyModule import add
from MyModule import sub
from MyModule import mul

class TestAdd(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(add(2,4), 6) 
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(2.3,3.6), 5.9)

    def test2(self):
        self.assertEqual(add(2.300,4.300), 6.6)
        self.assertEqual(add('hello','world'), 'helloworld')
        self.assertNotEqual(add(-2,-2), 0)
       
class TestSub(unittest.TestCase): 
    def test1(self):
        self.assertEqual(sub(2,4), -2) 
        self.assertEqual(sub(0,0), 0)
        self.assertNotEqual(sub(2.3,3.6), -1.300)

class TestMul(unittest.TestCase): 
    def test1(self):
        self.assertEqual(mul(2,4), 8) 
        self.assertEqual(mul(0,0), 0)
        self.assertNotEqual(mul(2.3,3.6), 2.300)


   
    
        
    

unittest.main()