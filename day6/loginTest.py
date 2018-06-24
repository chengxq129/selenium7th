from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#这里没有隐式等待
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element(By.ID,"username").send_keys("chengxq")
driver.find_element(By.NAME,"password").send_keys("chengxq1234")
driver.find_element(By.CLASS_NAME,"login_btn").click()
#点击链接“进入购物商场”
#显示等待代码
#WebDriverWait(driver,20,0.5).until(expected_conditions)
WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))
#这句显示等待代码，相当于time.sleep(20)的优化
driver.find_element_by_link_text("进入商城购物").click()