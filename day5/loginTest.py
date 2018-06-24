import time
import unittest

from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这时这个类不需要再写setUp和tearDown方法，只需要写测试用例方法即可
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.ID,"username").send_keys("chengxq")
        driver.find_element(By.NAME,"password").send_keys("chengxq1234")
        old_title = driver.title
        driver.find_element(By.CLASS_NAME,"login_btn").click()

        #写一个断言判断是否登录成功
        time.sleep(5)
        new_title = driver.title
        print("旧页面："+old_title)
        print("新页面："+new_title)

        self.assertNotEqual(old_title,new_title,'登录失败')
        print(driver.current_url)

if __name__ == '__main__':
    #MyTestCase.main()
    unittest.main()