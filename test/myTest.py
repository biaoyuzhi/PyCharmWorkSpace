#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author: wuzh
# @time  : 2019/2/1
import unittest
from service.linkDataBase import LinkDataBase


class MyTest(unittest.TestCase):    # 继承unittest.TestCase
    def setUp(self):
        # 每个测试用例执行之前做操作
        pass

    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        pass

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        pass

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例1

    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例2

    def test_all(self):  # 测试用例3，用来测试项目中各个类中的各个方法的实现，从上到下依次测试
        obj = LinkDataBase().get_data('1')
        print(obj)


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
