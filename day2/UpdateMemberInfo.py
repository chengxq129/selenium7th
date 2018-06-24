#1、登录海盗商城
#因为大部分测试用例都会用到登录功能，那我们可不可以
import time
from selenium import webdriver

#文件名、类名、包名、变量名进行命名时都应该以字母开头，可以有数字和下划线，但不能有空格和中文
from selenium.webdriver.support.select import Select

from day2.loginTest import Login

#我们现在已经创建好一个空白的浏览器了，后续的所有操作都应该在这个浏览器上执行
driver = webdriver.Chrome()

#每次创建浏览器时，固定写一次，对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要是检测页面的加载时间，检测什么时候页面加载完，什么时候执行操作
driver.implicitly_wait(20)

#实例化对象会占用内存，pycharm会自动帮助我们释放内存
#代码运行完成后检测到Login()这个对象不再被使用，系统会自动释放内存
#所有的类实例化占用的都是堆内存
#把driver浏览器传入到登录方法中
#让登录方法和下面的点击账号设置使用同一个浏览器
Login().loginWithDefaultUser(driver)
#2、点击“账号设置”
#本来点击账号设置需要使用driver这个变量，但现在文件中没有driver变量
#可以重新声明一个
driver.find_element_by_link_text("账号设置").click()

#3、点击“个人资料”
#partial_link_text可以使用链接的一部分进行元素定位
#当链接文本过长时，推荐使用partial_link_text
#使用partial_link_text方法时，可以用链接中的任意一部分，只要在网页中唯一即可
#driver.find_element_by_link_text("个人资料").click()
driver.find_element_by_partial_link_text("个人资料").click()
#xpath方法比较通用，可以使用工具自动生成，但不推荐使用，作为一种没有办法时使用
#driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()

#4、修改真实姓名
#如果输入框中原本有内容，那么我们修改内容时往往需要先清空原来的值，用clear()方法
#实际上一个良好的编程习惯是在每次send_keys之前，都应该先进行clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("程昱")

#5、修改性别
#通过观察发现保密、男、女三者唯一的区别就是value属性的值不同
#所以我们可以通过value属性来定位，实际上我们可以通过任何属性来定位
#要想通过value属性定位有两种方法：xpath和css_selector
#通过css_selector定位元素，只需要在唯一元素两边加上中括号[]即可
#driver.find_element_by_css_selector('[value="1"]').click()

#在xpath中，//表示采用相对路径定位元素，
# /单斜杠表示绝对路径，一般都是从/HTML根节点开始定位元素
#相对路径一般通过元素的特殊属性查找元素
#绝对路径一般通过元素的位置，层级关系查找元素
#绝对路径写起来比较长，涉及到的节点比较多，当开发人员修改页面布局时受到影响的可能性比较大，代码的稳定性比较差
#相对路径，查询速度比较慢，因为可能需要遍历更多的节点
#工作中一般用css_selector，因其查询速度比xpath快一点
#xpath在某些浏览器上支持的不太好，比如IE8
#所有前端开发都会使用css_selector,便于沟通交流
#*表示任意节点
#[@]表示通过属性定位
#driver.find_element_by_xpath('//*[value="2"]').click()

#javascript的getElementsByClassName()可以找到页面上符合条件的所有元素
#然后再通过下标选取其中的第n个元素，也可以用于定位
#所以selenium也可以通过下标选取其中的第n个元素，用于定位
#要找页面上符合条件的所有元素就用find_elements这个方法
#要找页面上符合条件的唯一元素就用find_element这个方法
driver.find_elements_by_id("xb")[1].click()
#6、修改生日
#一下一下点年、月、日是可以实现的，但是稳定性比较差，很容易点错，并且很难修改日期，故尽量不要用click()点击选择输入日期
#因为readonly为只读，导致输入框不可进行输入，需写一个javascript删除readonly属性，再进入输入
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1994-05-21")
#7、修改qq
driver.find_element_by_id("qq").send_keys("324567")
#8、点击“确定”，保存成功
driver.find_element_by_class_name("btn4").click()
time.sleep(5)
driver.switch_to.alert.accept()
