#第一个单元测试框架的示例-demo
#1.要想使用unittest框架，首先要导包
#unittest比selenium更常用，几乎所有的测试都要用unittest组织测试，所有python把unittest集成在python SDK中了
#不需要单独下载只要安装python就有，unittest是python内置的代码库
import unittest

#2.创建一个类，用例编写自动化测试用例
# 这个自动化测试用例的类需要继承unittest框架中的TestCase类
#我们继承了TestCase这个类就说明我们这个类是一个测试用例类
#python中的类名最好和文件名不一样，文件名首字母小写，类名首字母大写
# 类名和文件名不一致不做强制要求，仅是一个python习惯
#()表示继承，继承是指子类完全继承父类的所有方法和属性，并且有自己扩展的内容
class FirstUnitTest(unittest.TestCase):
#3.重写父类的setUp和tearDown方法
    def setUp(self):
        #setUp()方法是在测试用例执行之前要做的操作
        #类似于手工测试的预置条件
        #setUp和tearDown方法在每个测试用例方法执行时都会执行一下
        print(1)
    def tearDown(self):
        #tearDown()方法是在测试用例执行之后要做的操作
        #比如可能需要还原测试场景，消除脏数据
        print(2)
    def test_login(self):
        #这个方法用来编写测试步骤
        #框架规定测试用例方法必须以test开头，只有以test开头的方法才能被当做测试用例，直接执行
        print(3)
    def switch_window(self):
        #窗口切换方法不是以test开头，不能直接运行，只有被调用才能使用
        print(4)
    def test_zhuce(self):
        #在python中，类里面的每一个方法都有一个默认参数，叫self
        #self类似于java中this关键字，仅代表类本身
        #如果你想使用类的属性和方法，那么必须在前面加self关键字
        #根据光标所在位置决定执行什么测试用例
        #光标在哪个方法中，那么就会只运行哪个测试用例
        #光标在unittest.main()方法中就会执行全部测试用例
        self.switch_window()
#一个类中，所有测试用例方法的执行顺序是根据方法名的字母顺序执行的
    #这两个方法不常用，了解一下即可
    @classmethod
    def setUpClass(cls):
        print(5)

    #@classmethod在python中为装饰器，在java中叫注释

    @classmethod
    def tearDownClass(cls):
        print(6)
    #classmethod只在类中所有方法前或者方法后执行一次

#if __name__ = '__main__':这是一个固定写法
#在程序运行时，通过这句话，可以自动判断当前文件是不是程序的入口
#如果当前文件是程序的入口，那么就会执行if子句中的内容
#__name__指的是当前文件，__main__指的是程序入口

if __name__ == '__main__':
    #unittest.main()方法可以理解为当前文件的主函数，会自动调用类中的所有测试方法
    unittest.main()
