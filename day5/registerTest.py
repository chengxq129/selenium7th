#1.导包
import unittest

import time
from selenium import webdriver

#2.继承unittest.TesrCase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    #3.重写setUp和tearDown方法
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        #time.sleep(30)
        cls.driver.quit()

    #4.编写一个测试用例方法（以test开头的方法）
    def test_register(self):
        for row in CsvFileManager4().read('test_data.csv'):
            driver= self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            #driver.find_element_by_name('username')=driver.find_element(By.NAME,'username')
            #这两种方法没有任何区别，但是后面的这种方法扩展性更好，便于我们的框架封装
            #driver.find_element_by_name('username')
            driver.find_element(By.NAME,'username').send_keys(row[0])
            driver.find_element(By.NAME,'password').send_keys(row[1])
            driver.find_element(By.NAME,'userpassword2').send_keys(row[2])
            driver.find_element(By.NAME,'mobile_phone').send_keys(row[3])
            driver.find_element(By.NAME,'email').send_keys(row[4])
            #driver.find_element(By.LINK_TEXT,'注册').click()
            check_tip = driver.find_element(By.CSS_SELECTOR,'form > ul > li:nth-child(1) > div > span').text
            print(check_tip)

            #if check_tip =="通过信息验证！":
            #    print("测试通过")
            #else:
            #    print("测试失败")

            self.assertEqual("通过信息验证！",check_tip)
            #虽然第一行测试数据执行失败了，但是后面的测试是不依赖于前面的，
            # 不应该因为第一条失败就导致其他行数据不执行测试
            #所以我们不应该用for循环的方式执行不同的测试数据，
            # 因为在方法中写了for循环虽然执行了多次，但是unittest仍然认为它是一条测试用例
            #一旦断言失败就会终止这条测试用例
            #所以我们应该采用ddt框架实现数据驱动
            

if __name__ == '__main__':
    unittest.main()


