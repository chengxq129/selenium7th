#如何把这个文件封装成一个登录方法
#python中类的关键字和java一样，是class
#python中方法也有一个关键字，是def，def是define的缩写，表示定义方法



#1、打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#首先声明一个类
#python中使用冒号代替java中的大括号，在冒号后点击回车，可自动缩进4个空格，()可以不写，如class Login:
#所有属于类的语句都必须缩进4个空格
class Login():
    #def是方法的关键字，表示这是一个方法
    #loginWithDefaultUser这是我们随意起的方法名，意思是使用默认账户登录
    #方法后面必须要有括号，可以用来声明函数
    #括号中默认有一个参数(self)，self表示类本身，类似于java中this关键字
    #self参数后面再详细讲解，暂时我们用不到self参数
    #方法的声明后面也有一个冒号，方法下面所有语句也要再缩进4个空格
    #这样登录功能的代码就被封装到loginWithDefaultUser方法中了，以后只需要写一句话调用这个方法即可登录网站了
    def loginWithDefaultUser(self,driver):
        #driver = webdriver.Chrome()
        #2、打开海盗商城网站
        driver.get("http://localhost")
        #3、删除登录链接的target属性
        #在python中字符串可以用双引号，也可使用单引号
        #若字符串本身包含双引号，则我们就在两边使用单引号
        #driver.execue_script
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        #4、点击登录按钮，跳转到登录页面
        driver.find_element_by_link_text("登录").click()
        #5、输入用户名
        driver.find_element_by_id("username").send_keys("chengxq")
        #6、输入密码
        #ActinChains需要导包，导包快捷键Alt+Enter
        #action动作行为的意思，Chains是链表的意思，链表类似于数组，所以ActionChains是一组动作和行为的意思
        #下面这句话的作用是实例化一个ActionChains这个类的对象，这个对象用来执行一组动作和行为
        #和java的区别就是少了一个new
        #python语言中实例化对象，不需要声明变量的类型
        actions = ActionChains(driver)
        #如果你想使用键盘上的任意控件，直接去Keys类中找即可
        #所有的actions中的方法都必须以perform()结尾才能被执行
        actions.send_keys(Keys.TAB).send_keys("chengxq1234").perform()
        #7、点击登录按钮
        #actions.send_keys(Keys.ENTER).perform()
        #假如不支持回车键登录，我们可以直接定位登录按钮并点击
        #假如也很难定位登录按钮，我们还可以用submit()方法
        #submit是提交的意思，用于提交表单
        #想象一下，用户名和密码等信息是不是同时发送给后台服务器？
        #开发人员通过form表单把这些信息同时提交到服务器上
        #可以用任何一个表单中的元素执行submit()方法来提交表单中的所有数据
        #比如，我们可以用用户名来提交表单数据
        driver.find_element_by_id("username").submit()