from selenium import webdriver
driver = webdriver.Chrome()
#1、打开主页
driver.get("http://localhost/")
#2、点击登录按钮
driver.find_element_by_link_text("登录").click()
#如果我们想在新的标签页上操作页面元素，怎么办？
#需要进行窗口切换
#driver.switch_to.window(第二个窗口的名字)
#接下来问题是如何获取第二个窗口的名字
#selenium提供了浏览器中所有窗口名字的集合
#handle是句柄的意思，把句柄理解为名字即可
#driver.winow_hangles可以理解为一个数组，我要求第二个窗口的名字怎么做
#[1]表示数组的第二个元素，所以第二个窗口的名字是driver.window_handles[1]
#窗口切换语句是：
driver.switch_to.window(driver.window_handles[-1])
#3、在搜索框中输入iphone
#这时再试一下iphone会被输入到哪个搜索框中
driver.find_element_by_name("keyword").send_keys("iphone")
#[1]表示第二个元素，[-1]表示最后一个元素
#在python中元组和列表可以正着从0开始数，也可以从负着从-1开始数，倒数第一个-1，倒数第二个-2
#所以上面的代码可以改成什么，如下所示
#driver.switch_to.window(driver.window_handles[-1])

