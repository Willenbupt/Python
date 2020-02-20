# -*- coding: utf-8 -*-
'''
目的：爬取天猫里的内容
关键url: https://list.tmall.com/search_product.htm?q=羽毛球
step 1: 登录淘宝，结合前边的代码使用
step 2: 加载全部天猫商品  By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap
step 3: 获取天猫商品的总页数 By.CSS_SELECTOR, .ui-page > div.ui-page-wrap > b.ui-page-skip > form 并返回该数字
step 4: 定义翻页的方法，通过在页数的输入框输入指定页数进行翻页，清空输入框，传入页数，点击确定
step 5: 通过运行JS代码实现向下滑动
step 6: 开始爬取天猫数据：进入指定物品搜索页->先确定是否可以找到该商品->可以则返回确定消息
step 7: 获取上方法实现的页数
step 8: 遍历所有页数{1、等待页面商品加载完毕，2、等待页面input输入框}，获取当前页数以及总页数->获取当前页源码->解析源码
step 9: 在解析的源码存储 所有商品的信息，通过读取这个总类的标签-> 遍历每一件商品->打印信息
step 10: 遍历完后便向下滑动，翻页
step 11：若有验证码通过验证码模块移除验证
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pyquery import PyQuery as pq
from time import sleep


# 定义一个taobao类
class taobao_infos:

    # 对象初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 延时操作,并可选择是否弹出窗口提示
    def sleep_and_alert(self, sec, message, is_alert):

        for second in range(sec):
            if (is_alert):
                alert = "alert(\"" + message + ":" + str(sec - second) + "秒\")"
                self.browser.execute_script(alert)
                al = self.browser.switch_to.alert
                sleep(1)
                al.accept()
            else:
                sleep(1)

    # 登录淘宝
    def login(self):

        # 打开网页
        self.browser.get(self.url)

        # 自适应等待，点击密码登录选项
        self.browser.implicitly_wait(30)  # 智能等待，直到网页加载完毕，最长等待时间为30s
        self.browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click()

        # 自适应等待，点击微博登录宣传
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath('//*[@class="weibo-login"]').click()

        # 自适应等待，输入微博账号
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_name('username').send_keys(weibo_username)

        # 自适应等待，输入微博密码
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_name('password').send_keys(weibo_password)

        # 自适应等待，点击确认登录按钮
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                      '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
        # 输出淘宝昵称
        print(taobao_name.text)

    # 获取天猫商品总共的页数
    def search_toal_page(self):

        # 等待本页面全部天猫商品数据加载完毕
        # 把包含所有商品的整个类导入
        good_total = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap')))

        # 获取天猫商品总共页数
        number_total = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form')))
        #需要注意 replace 不会改变原 string 的内容,把出现的中文字都替换成空，只保留数字
        page_total = number_total.text.replace("共", "").replace("页，到第页 确定", "").replace("，", "")

        return page_total

    # 翻页操作
    def next_page(self, page_number):
        # 等待该页面input输入框加载完毕
        input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > input.ui-page-skipTo')))

        # 等待该页面的确定按钮加载完毕
        submit = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > button.ui-btn-s')))

        # 清除里面的数字
        input.clear()

        # 重新输入数字
        input.send_keys(page_number)

        # 强制延迟1秒，防止被识别成机器人
        sleep(5)

        # 点击确定按钮
        submit.click()

    # 模拟向下滑动浏览
    # 滚动条是无法直接用定位工具来定位的。selenium里面也没有直接的方法去控制滚动条，
    # 这时候只能借助J了，还好selenium提供了一个操作js的方法:
    # execute_script()，可以直接执行js的脚本
    #1.滚动条回到顶部：
    # js="var q=document.getElementById('id').scrollTop=0"
    # driver.execute_script(js）
    # 2.滚动条拉到底部
    # js="var q=document.documentElement.scrollTop=10000"
    # driver.execute_script(js)
    # 3.这里可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部。
    def swipe_down(self, second):
        for i in range(int(second / 0.1)):
            js = "var q=document.documentElement.scrollTop=" + str(300 + 200 * i)
            self.browser.execute_script(js)
            sleep(0.1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        sleep(0.2)

    # 爬取天猫商品数据
    def crawl_good_data(self):

        # 对天猫商品数据进行爬虫
        #可以修改网址后面的名称指定搜索内容
        #先进入到相关产品的搜索页
        self.browser.get("https://list.tmall.com/search_product.htm?q=羽毛球")

        #//div/*           div下面的所有的元素
        # //div//p         先在整个文档里查找div，再在div里查找p节点(只要在内部，不限定是否紧跟) ；等价于 css_selector里的('div p')
        # //div/p          p是div的直接子节点； 等价于 css_selector里的('div > p')
        # //*[@style]      查找所有包含style的所有元素，所有的属性要加@；  等价于 css_selector里的('*[style]')
        # //p[@spec='len'] 必须要加引号；等价于 css_selector里的("p[spec='len']")
        # //p[@id='kw']    xpath中对于id,class与其他元素一视同仁，没有其他的方法


        # // div / p[2]                   选择div下的第二个p节点 ；等价于css_selector里的div > p: nth - of - type(2)  符合p类型的第二个节点
        # // div / * [2]                   选择div下第二个元素
        # // div / p[position() = 2]        position() = 2   指定第二个位置；  等价于上面的 // div / p[2] 
        #           position() >= 2      位置大于等于2
        #           position() < 2       位置小于2
        #           position() != 2     位置不等于2
        # // div / p[last()]              选择div下的倒数第一个p节点； last()
        # 倒数第一个
        # // div / p[last() - 1]            选择div下的倒数第二个p节点；
        # // div / p[position() = last()]   倒数第一个
        # // div / p[position() = last() - 1] 倒数第二个
        # // div / p[position() >= last() - 2]
        # 倒数第一个，第二个，第三个

        # 寻找属性id='content'的下的div下的第二层div的text内容
        #[x] 代表第几个元素
        #原网页是
        #<div id = "content">
        #  <div class = "main    ">
        #      .......
        #      <div class="searchTip" data-spm="a220m.1000858.1000727">
        #           <h2>喵~没找到与“ GTA外挂 ”相关的 商品 哦，要不您换个关键词我帮您再找找看</h2>
        #           <h3>建议您：</h3>
        # 第六种：父节点：
        # // div[ @ id = 'a'] /..选择目标div的父节点
        #该文本处于div3的原因是因为 相对与content节点是第三个
        #貌似也可以F2在网页对应元素位置 右键copy xpath
        err1 = self.browser.find_element_by_xpath("//*[@id='content']/div[1]/div[3]").text
        err1 = err1[:5]
        if (err1 == "喵~没找到"):
            print("找不到您要的")
            return

        try:

            #这应该是查询物品太少时的响应功能
            self.browser.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]")
            err2 = self.browser.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]").text
            # print(err2)

            err2 = err2[:5]

            if (err2 == "我们还为您"):
                print("您要查询的商品书目太少了")
                return
        except:
            print("可以爬取这些信息")

        # 获取天猫商品总共的页数
        page_total = self.search_toal_page()
        print("总共页数" + page_total)

        # 遍历所有页数
        for page in range(2, int(page_total)):

            # 等待该页面全部商品数据加载完毕
            good_total = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap')))

            # 等待该页面input输入框加载完毕
            input = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > input.ui-page-skipTo')))

            # 获取当前页
            now_page = input.get_attribute('value')
            print("当前页数" + now_page + ",总共页数" + page_total)

            # 获取本页面源代码
            html = self.browser.page_source

            # pq模块解析网页源代码
            # 通过保存网页源码，接下来直接对保存在本地的源码进行操作
            doc = pq(html)

            # 存储天猫商品数据
            good_items = doc('#J_ItemList .product').items()

            # 遍历该页的所有商品
            for item in good_items:
                good_title = item.find('.productTitle').text().replace('\n', "").replace('\r', "")
                good_status = item.find('.productStatus').text().replace(" ", "").replace("笔", "").replace('\n',
                                                                                                           "").replace(
                    '\r', "")
                good_price = item.find('.productPrice').text().replace("¥", "").replace(" ", "").replace('\n',
                                                                                                         "").replace(
                    '\r', "")
                good_url = item.find('.productImg').attr('href')
                print(good_title + "   " + good_status + "   " + good_price + "   " + good_url + '\n')

            # 精髓之处，大部分人被检测为机器人就是因为进一步模拟人工操作
            # 模拟人工向下浏览商品，即进行模拟下滑操作，防止被识别出是机器人
            self.swipe_down(2)

            # 翻页，下一页
            self.next_page(page)

            # 等待滑动验证码出现,超时时间为5秒，每0.5秒检查一次
            # 大部分情况不会出现滑动验证码，所以如果有需要可以注释掉下面的代码
            # sleep(5)
            WebDriverWait(self.browser, 5, 0.5).until(EC.presence_of_element_located((By.ID, "nc_1_n1z")))  # 等待滑动拖动控件出现
            try:
                swipe_button = self.browser.find_element_by_id('nc_1_n1z')  # 获取滑动拖动控件

                # 模拟拽托
                action = ActionChains(self.browser)  # 实例化一个action对象
                action.click_and_hold(swipe_button).perform()  # perform()用来执行ActionChains中存储的行为
                action.reset_actions()
                action.move_by_offset(580, 0).perform()  # 移动滑块

            except Exception as e:
                print('get button failed: ', e)


if __name__ == "__main__":
    

    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "********"  # 改成你的微博账号
    weibo_password = "********"  # 改成你的微博密码

    a = taobao_infos()
    a.login()  # 登录
    a.crawl_good_data()  # 爬取天猫商品数据
