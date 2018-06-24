from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
#1、登录海盗商城后台
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("username").submit()
#2、选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#3、点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
#4、输入商品名称
#操作子框架中的元素首先要进行frame切换
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("饮水机")
#driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(1) > input").send_keys("饮水机")
#5、选择商品分类（双击或点击“选择当前分类”）
driver.find_element_by_id("1").click()
driver.find_element_by_link_text("手机通讯").click()
driver.find_element_by_link_text("手机").click()
driver.find_element_by_link_text("苹果 (Apple)").click()
driver.find_element_by_id("jiafen").click()
#ActionChains(driver).double_click()
#6、在下拉框中选择商品品牌
sp_drop = driver.find_element_by_id("brand_id")
print(type(sp_drop))
sp_select = Select(sp_drop)
print(type(sp_select))
sp_select.select_by_value("1")
driver.find_element_by_name("is_sales").click()
driver.find_element_by_name("is_new").click()
driver.find_element_by_name("keyword").send_keys("iphone6s")
driver.find_element_by_name("brief").send_keys("限时促销，七折优惠")
#7、点击提交按钮
driver.find_element_by_css_selector(".button_search").click()
#根据以上7步，找出第一个不能实现的地方























