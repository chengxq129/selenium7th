#这种框架设计思想叫做page-object设计模式，是一种高级框架设计思想
#这种思想的主旨是把业务逻辑和代码技术分离开
#测试用例的类，专门负责业务逻辑
#元素定位和操作交给网页对象（page-object）
#在pageObject这个类中，把每个网页看成一个类
#其中网页中的每个元素看成类中的一个属性
#针对这个元素的操作看成类中的一个方法
#元素的信息，定位是名词性，所有可以看成属性（成员变量）
#元素的操作是名词性，所有可以看成是方法
#那么下面我们封装一下登录这个网页

#这个类主要做的是把元素定位和操作改一个易于理解的名字
#driver.get("http://localhost/index.php?m=user&c=public&a=login")
#driver.find_element(By.ID,"username").send_keys("chengxq")
#driver.find_element(By.NAME,"password").send_keys("chengxq1234")
#driver.find_element(By.CLASS_NAME,"login_btn").click()

#最后要把上面的代码封装成下面这个样子
#login_page.open()
#login_page.input_username()
#login_page.input_password()
#login_page.click_login_button()
#memeber_center_page.verify_username()

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #为这个网页创建一个构造函数
    #在python中构造函数固定名字__init__()
    def __init__(self,driver):
        #因为setUp方法中已经创建了一个浏览器
        self.driver = driver
        #self.driver = webdriver.Chrome()
        self.url = "http://localhost/index.php?m=user&c=public&a=login"

#声明一个变量保存元素定位需要的两个参数
    #python的元组，类似于数组--(By.ID,"username")
    #声明了一个数组叫username_input_loc，有两个元素，分别为By.ID和"username"
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.NAME,"password")
    login_button_click_loc = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)

    #username="chengxq"：给参数设置默认值，
    # 如果调用方法时传入一个新的用户名，那么使用新的；
    # 如果调用方法时不传参，那么使用默认值
    def input_username(self,username="chengxq"):
        #这个类中涉及到三个元素定位，因为元素定位不太稳定，经常需要修改，所以应该把定位方式声明成类中的一个属性
        #self.driver.find_element(By.ID,"username").send_keys(username)
        #星号*表示给find_element()这个方法传入的不是一个元组，
        #而是把元组中的每个元素都分别传入find_element()这个方法，作为单独的参数
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password="chengxq1234"):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_click_loc).click()

