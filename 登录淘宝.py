# -*- coding: utf-8 -*-

'''
目的： 实现登录淘宝
利用工具：selenium，这个是web应用程序测试工具，可以直接运行在浏览器中
python可以利用selenium来模拟正常用户访问浏览器
实现步骤：
step 1: 定义一个淘宝类，里面有一个初始化方法，


step2:初始化要登陆的url信息,实例化浏览器驱动的设置并设置(开发者模式，不加载图片.....),
      实例化浏览器，传入chrome驱动路径和设置，用于打开浏览器
      设置等待启动webdriver的时间

step3:在淘宝这个类里面定义一个登录的方法

step4:再这个登录的方法里面，首先向初始化的浏览器传入url打开网址
      获取网页内的‘密码登录’的id->并选中这个标签->点击
      获取网页内的‘微博登录’的id->并选中这个标签->点击
      获取网页内的‘账号’的id->并选中这个标签->传入账号信息
      获取网页内的‘密码’的id->并选中这个标签->传入密码信息
      获取网页内的‘登录的按钮’的id->并选中这个标签->点击
      直到获取到淘宝昵称等信息表示登录成功
'''

from selenium import webdriver
from selenium.webdriver.common.by import By #By这个类里面有各种方法用来定位元素
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaoBao_Info():


    # 对象初始化
    # 特殊方法“__init__”前后分别有两个下划线！__init__方法的第一个参数永远是self，表示创建的实例本身
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
    # 但self不需要传，Python解释器自己会把实例变量传进去：
    def __init__(self):
        url = "https://login.taobao.com/member/login.jhtml"
        self.url = url

        option = webdriver.ChromeOptions()

        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        option.add_experimental_option("prefs",{'profile.managed_default_content_settings.images':2})

        option.add_experimental_option('excludeSwitches',['enable-automation'])

        # browser ={WebDriver}<selenium.webdriver.chrome.webdriver.WebDriver (session="c76c6459cff670170d1eeae38bf9d5ed")>
        self.browser = webdriver.Chrome(executable_path=webdriverpath,options=option)

        # wait ={WebDriverWait}<selenium.webdriver.support.wait.WebDriverWait (session="c76c6459cff670170d1eeae38bf9d5ed")>
        # WebDriverWait() 显示等待:
        # WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
        self.wait = WebDriverWait(self.browser, 10)


    def login_taobao(self):
        # 打开网页
        # a = TaoBao_Info()  a是个类，而login是类里面的方法
        # a.login()  # 登录

        # 首先要将类实例化  才能  调用类里面的方法
        # 类其中的__init__()方法会自动调用，这个是特殊方法
        # 每个类 可以通过self.属性 共享 __init__()里面初始化的属性, 这些属性是同一个存储位置
        # self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        # 在一开始已经经browser调用了chrome驱动，所以通过其get函数获取url并打开

        # 调试信息：
        # self={TaoBao_Info} <_main_.taobao_infos object at 0x0000024DBA3AE9A0>
        # chromedriver={WebDriver}<selenium.webdriver.chrome.webdriver.WebDriver (session="60b8302f407e6be03bae134883ffa94f")>
        # url={str}'https://login.taobao.com/member/login.jhtml'
        # wait={WebDriverWait}<selenium.webdriver.support.wait.WebDriverWait (session="60b8302f407e6be03bae134883ffa94f")>
        # self.url={str}'https://login.taobao.com/member/login.jhtml'

        self.browser.get(self.url)


        # presence_of_element_located : 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
        # EC.presence_of_element_located((By.ID,"acdid"))
        # 元素定位之CssSelector
        # '.qrcode-login > .login-links > .forget-pwd' 这些.xxxxx是类名
        # 子元素A > B 层级
        # 4.通过父子关系定位：
        #selenium里的until(可执行方法，方法错误时返回的信息)，until的值应该是可执行方法返回的值，猜的，懒得查文档
        # 这里的子元素为爷父子关系

        # 等待 密码登录选项 出现
        password_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()
        #调试信息
        #password_login={WebElement}<selenium.webdriver.remote.webelement.WebElement (session="ac18f7e50be5b46987374f60d5509f92", element="29d8b45d-256c-4e33-9108-ea017f43abd0")>

        # 等待 微博登录选项的出现，通过这个类选择该登录模块
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.weibo-login')))
        # 点击微博登录
        weibo_login.click()

        # 这里选择关于id是username的子元素
        weibo_username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.username>.W_input')))
        weibo_username.send_keys(username)
        weibo_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        weibo_password.send_keys(password)





        print("老板输入成功")


        login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn_tip > a > span')))
        login.click()

     # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                      '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))

        print(taobao_name.text)
        print("恭喜老板登录成功")



if __name__ == "__main__":
    webdriverpath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    username = "123456"
    password = "123456"
    a = TaoBao_Info()
    a.login_taobao()


