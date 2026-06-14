#python的测试演示，需要引入python内置的unittest模块
import unittest
#from 方法所在文件名 import 方法名   此语法里的from用来规定对象所在的文件，也就是一个python程序，import后跟着的是被测试的方法的名称
from shopping_list import ShoppingList
#测试类必须传入 unittest.TestCase，这样 unittest 才能识别并运行其中的测试方法
#类名通常以 Test 开头，清晰表明这是一个测试类
class TestShoppingList(unittest.TestCase):
    #setUp 是 TestCase 类中的特殊方法，在每个测试方法执行之前自动运行
    #该方法里创建的实例赋值给 self.shopping_list，后续的测试方法可以直接使用，无需重复创建，减少代码量，提高可读性
    def setUp(self):
        self.shopping_list=ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})

#命名规范：测试方法必须以 test 开头，否则 unittest 不会执行它
    def test_get_item_count(self):
        #self.assertEqual(a, b)：断言 a == b。如果相等，测试通过；否则失败并报告差异
        self.assertEqual(self.shopping_list.get_item_count(),3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(),53)