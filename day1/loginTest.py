#这个文件用来实现登录功能的自动化操作
#1、打开浏览器
import time
from selenium import webdriver
#从 谷歌公司的一个项目（ selenium.zip） 导入 网络驱动 用代码来操作浏览器
#下载谷歌最新驱动网址：http://npm.taobao.org/mirrors/chromedriver/
driver = webdriver.chrome()
#设置隐式等待：一旦找到页面元素，马上执行后面的语句
#如果超过20s，仍找不到页面元素，那么程序将会报超时错误
driver.implicitly_wait(20)
#2、打开海盗商城网站
driver.get("http://localhost/")
#3、打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4、输入用户名和密码
driver.find_element_by_id("username").send_keys("chengxq")
driver.find_element_by_name("password").send_keys("chengxq1234")
#5、点击登录按钮
#所有调用方法都会有提示信息，没有提示信息则说明没有这个方法
driver.find_element_by_class_name("login_btn").click()
#6、检查登录是否成功，按照现在所学还不能定位用户名信息，稍后考虑这个问题
#Alt+enter,导包快捷键，选择import this name，选择最短的time
#
#这里的意义是点击登录后等待5s后，再检查用户名是否正常显示
#弊端是因为网络延迟，不知道是每次等1s合适还是
#time.sleep(5)
username_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text

print(username_text)
#我们可以通过if语句判断页面显示的文本和预期的文本H是否一致，来判断测试用例是否正常执行
if username_text=='您好 chengxq':
    print("测试执行通过")
else:
    print("测试执行失败")
#因为selenium主要做回归测试，所以测试脚本刚开始都是pass的，只有开发变更了代码，我们的测试用例才有可能失败
#一般工作中不用if。。else语句做判断，后面再详细讨论这个问题
#7、点击进入商城购物按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
#xpath有一个缺点，定位元素的可读性比较差，有没有可读性好一点的方法？可通过连接文本的方式进行定位
driver.find_element_by_link_text("进入商城购物").click()
#8、在商城主页，输入搜索条件'iphone'
driver.find_element_by_name("keyword").send_keys("iphone")
#9、点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#10、在搜索结果页面，点击第一个商品的图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click()
driver.close()#关闭selenium正在工作的窗口
driver.switch_to.window(driver.window_handles[-1])#窗口切换
#11、点击“加入购物车”
#time.sleep(5)
driver.find_element_by_id("joinCarButton").click()