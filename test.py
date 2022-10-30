import random
import unittest
import time
import main

from matplotlib import pyplot as plt


class TestMethod(unittest.TestCase):
    num=[1,2,3,0,1]
    num1=[1,29,102,1,2,0,-10,912,29,39,0]

    def test_min(self):
        self.assertEqual(main._min(self.num1),-10)

    def test_max(self):
        self.assertEqual(main._max(self.num1),912)

    def test_summ(self):
        self.assertEqual(main._sum(self.num), 7)

    def test_mult(self):
        self.assertEqual(main._mult(self.num), 0)

    def test_1(self):
        self.assertEqual(main._min(self.num), 0)
        self.assertEqual(main._max(self.num), 3)
        self.assertEqual(main._sum(self.num), 7)
        self.assertEqual(main._mult(self.num), 0)


    def test_time(self):
        num_c=[1,2,1,3]*1000
        start_time=time.time()
        main._min(num_c)
        end_time=time.time()
        t=end_time-start_time

        num_l=[1,2,1,3]*100
        start_time=time.time()
        main._min(num_l)
        end_time=time.time()
        t_l=end_time-start_time
        print (t)
        #self.assertEqual((t_l/(t*100))<1, True)