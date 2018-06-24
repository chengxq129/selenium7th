#在这个python文件中，实现注册功能自动化
from selenium import webdriver
driverzc = webdriver.Chrome()
driverzc.get("http://localhost/")
driverzc.get("http://localhost/index.php?m=user&c=public&a=reg")
driverzc.find_element_by_name("username").send_keys("chengxq1")
driverzc.find_element_by_name("password").send_keys("chengxq1")
driverzc.find_element_by_name("userpassword2").send_keys("chengxq1")
driverzc.find_element_by_name("mobile_phone").send_keys("15701261611")
driverzc.find_element_by_name("email").send_keys("chengxq@126.com")
driverzc.find_element_by_class_name("reg_btn").click()




