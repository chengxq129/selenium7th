#用unittest写一个后台登录的测试用例
#1.导包
import unittest

import time
from selenium import webdriver

#2.建类，并集成unittest。TestCase
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    #3.重写setUp和tearDown方法
    @classmethod
    def setUpClass(self):
        #做web自动化测试，是不是所有的测试用例都要先打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #窗口最大化的代码，要求驱动器版本必须和浏览器精准匹配
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        #为了保证可以看清测试结果，可以在tearDown方法中加一个30s的延时等待
        time.sleep(30)
        #每次执行完测试用例，应该把打开的浏览器关闭
        # 释放内存，清楚cookie和缓冲，为下次执行测用例做准备
        #这里调用的driver是声明在setUp方法中局部变量
        # 局部变量是不允许被其他方法访问的，所有我们应该把setUp方法中声明的driver改成一个全局变量
        #self表示类本身，所有我们只要在变量前加上self.就表示这个变量是属于类的
        self.driver.quit()


    def test_login(self):
        #因为每次使用driver变量时，都需要前面加一个self
        #为了简化代码，可以把成员变量self.driver赋值给局部变量driver
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        #有些常用的键也可以用转义字符代替，其中\t表示tab键，\n表示enter键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

    def test_product_add(self):
        driver = self.driver
        #添加商品代码
        #如果第二个方法重新打开一个浏览器，登录就无效了,此时可以将setUp和tearDown方法变更为setUpClass和tearDownClass方法
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #除了用name属性切换frame，也可以通过八种定位元素方法定位元素，然后切换
        id_frame = driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(id_frame)
        #等于driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("name").send_keys("apple手机")
        #变量名文件名的命名规则：数字、大小写字母、下划线，一般要求以字母开头
        #如果id是纯数字，用#1方式不能定位，可以用[]定位，所有的属性都可以用[]定位
        #driver.find_element_by_id("1").click()
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("6").click()
        #driver.find_element_by_id("7").click()
        #driver.find_element_by_id("jiafen").click()
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        sp_drop = driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(3) > select")
        sp_select = Select(sp_drop)
        sp_select.select_by_value("1")
        driver.find_element_by_name("is_sales").click()
        driver.find_element_by_name("is_hot").click()
        driver.find_element_by_name("is_new").click()
        driver.find_element_by_name("keyword").send_keys("iphone6s")
        driver.find_element_by_name("brief").send_keys("限时促销，七折优惠")
        driver.find_element_by_class_name("button_search").click()

if __name__ == '__main__':
    unittest.main()