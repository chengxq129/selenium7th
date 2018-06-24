import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.DBconnection import DBConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        #数据库验证测试的正常情况
        self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        self.driver.find_element(By.NAME, 'username').send_keys("chengxq4")
        self.driver.find_element(By.NAME, 'password').send_keys("chengxq1234")
        self.driver.find_element(By.NAME, 'userpassword2').send_keys("chengxq1234")
        self.driver.find_element(By.NAME, 'mobile_phone').send_keys("13912345434")
        self.driver.find_element(By.NAME, 'email').send_keys("13912345434@126.com")
        self.driver.find_element(By.CLASS_NAME,'reg_btn').click()
        time.sleep(3)
        sql = 'select * from hd_user order by id desc;'
        new_record = DBConnection().execute_sql_command(sql)
        self.assertEqual("chengxq4",new_record[1])
        self.assertEqual("13912345434@126.com",new_record[2])
        print(new_record)