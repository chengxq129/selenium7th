#selenium执行javascript中的两个关键字：return(返回值)和arguments（参数）
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/")
#点击“登录”链接
#用javascript方法找登录链接的代码：
# document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")
#用selenium方法找登录链接的代码:
#driver.find_element_by_link_text("登录")
#我们可以把selenium找到的这个元素，传入到javascript方法里，代替原来的javascript定位
#然后使用removeAttribute("target")移除这个元素的target属性
login_link = driver.find_element_by_link_text("登录")
#把原来的javascript看成一个无参无返的方法，现在直接从外面传入一个页面元素，就变成一个有参无返的方法
#arguments参数的复数形式，[0]表示第一个参数，指的是js后面的login_link
#下面代码相当于把driver.find_element_by_link_text("登录")带入到javascript语句中
#变成了driver.find_element_by_link_text("登录").removeAttribute("target")
driver.execute_script('arguments[0].removeAttribute("target")',login_link)
login_link.click()
#登录
#方法1
#driver.find_element_by_id("username").send_keys("chengxq")
#driver.find_element_by_id("password").send_keys("chengxq1234")
#driver.find_element_by_class_name("login_btn").click()
#方法2
driver.find_element_by_id("username").send_keys("chengxq")
ActionChains(driver).send_keys(Keys.TAB).send_keys("chengxq1234").send_keys(Keys.ENTER).perform()
#返回商城首页
driver.find_element_by_link_text("返回商城首页").click()
#搜索iphone
#方法1
#driver.find_element_by_class_name("input_ss").send_keys("iphone")
#driver.find_element_by_class_name("btn1").click()
#方法2
driver.find_element_by_class_name("input_ss").send_keys("iphone")
driver.find_element_by_class_name("input_ss").submit()
#点击商品
#使用javascript
#通过xpath定位元素
#因为img没有target属性，所以我们复制css时要找到它的父节点
#iphone_link_xpath = "/html/body/div[3]/div[2]/div[3]/div/div[1]/a"
#iphone_link = driver.find_element_by_xpath(iphone_link_xpath)
#driver.execute_script('arguments[0].removeAttribute("target")',iphone_link)
# 通过css_selector定位元素
#因为img没有target属性，所以我们复制css时要找到它的父节点
#复制的css往往比较长，我们可以适当缩写长度
#定位元素的目标节点是最后一个节点
#大于号>前面是父节点，后面是子节点
#小数点后面接的是class属性
#nth_child[n]表示该节点是它的父节点的第n个子节点
#"#号"表示后面接的是id属性
#空格前面是祖先节点，空格后面是子孙节点
#[]：除了id和class，css可以用任何属性进行定位，只需要在属性两边加上中括号即可
#学会css_selector就可以用任何属性进行元素定位
iphone_link_css = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a"
iphone_link = driver.find_element_by_css_selector(iphone_link_css)
driver.execute_script('arguments[0].removeAttribute("target")',iphone_link)
iphone_link.click()
#在商品详情页面，点击加入购物车
driver.find_element_by_id("joinCarButton").click()
#点击去购物车结算
#driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算按钮
#在每个class前面都加一个小数点，并且去掉中间的空格，则可以同时用两个属性定位一个元素
#driver.find_elements_by_css_selector(".shopCar_btn_03.fl")
driver.find_element_by_link_text("结算").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()
#输入收货人等信息（选择地区-难点）
driver.find_element_by_name("address[address_name]").send_keys("李斯")
driver.find_element_by_name("address[mobile]").send_keys("15701261234")

#选择省
dropdown1 = driver.find_element_by_id("add-new-area-select")
#dropdown1的类型是一个普通的网页元素
#下面的代码意思是：把一个普通的网页元素，转换成一个下拉框的特殊网页元素
print(type(dropdown1))#dropdown1是WebElement类型
#WebElement类型
#下拉框是一种特殊的网页元素，与普通网页元素不太一样
#selenium为这种特殊的元素，专门创建了一个类select
select1 = Select(dropdown1)
print(type(select1))
select1.select_by_value("410000")#这时我们可以通过选项的值来定位
time.sleep(2)
select1.select_by_visible_text("江苏省")

#选择市
#因为是动态id，所以不能用id定位元素；因为class重复，所以不能用class定位元素
#我们可以用find_elements方法找到页面中所有class=add-new-area-select的元素
#然后通过下标的方式选择第n个元素
dropdown2 = driver.find_elements_by_class_name("add-new-area-select")[1]
print(type(dropdown2))
select2 = Select(dropdown2)
print(type(select2))
select2.select_by_visible_text("南通市")

#选择县区
#dropdown3 = driver.find_elements_by_class_name("add-new-area-select")[2]
#tag_name()大多数情况都能找到一堆元素，所以find_element_tag_name()这个方法很少用
#find_elements_tag_name()这个方法
dropdown3 = driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("如东县")

driver.find_element_by_name("address[address]").send_keys("江苏省南通市如东县第三大道21号")
driver.find_element_by_name("address[zipcode]").send_keys("321456")
#点击保存，保存收货人信息
driver.find_element_by_css_selector(".aui_state_highlight").click()