import sys
import re

class Data:
    exchange_rate = 7
    discount = 0.65
    product_title = None
    final_price = None
    product_name = None
    china_price = None
    product_price = None
    weight = None
    freight_charges = None
    china_product_url = None
    profit = None
    shippment_charge = None
    opponent_price = None
    promotion_cost = None
    airexpress_commission = None
    Feature = None
    Specication = None
    shippment_charge_judge = None
    product_bianti_name = None

    #输入上架产品的文本信息(已完善)
    def get_information(self):

        t = 1
        print("请输入商品名称:")
        Data.product_name = input()

        while t:
            print("请输入产品标题")
            Data.product_title = sys.stdin.readline()
            print('标题字符串的个数是：', len(Data.product_title), '个')
            product_title1 = re.compile(r'\b[a-zA-Z]+\b', re.IGNORECASE).findall(Data.product_title)
            # 将列表中的大写字母转换成小写
            # 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法
            product_title2 = [s.lower() for s in product_title1 if isinstance(s, str) == True]
            print(product_title2)
            t = 0
            for i in product_title2:
                count = product_title2.count(i)
                print('标题中每个单词的出现次数是:')
                print(i, ':', count)
                if count >= 3:
                    print("出现标题关键词次数违规：")
                    print(i, ':', count)
                    print("请重新输入标题！")
                    t = 1


        print("请输入货源url")
        Data.china_product_url = input()

    #输入上架变体的文本信息
    def get_bianti_information(self):
        print("请输入变体名称:")
        Data.product_bianti_name = input()

    #输入对手的竞品的信息
    def get_opponent_info(self):
        print("####接下来是竞品信息####")
        print("对手是否包邮(0包邮/1不包邮)：")
        Data.shippment_charge_judge = input()
        if int(Data.shippment_charge_judge) == 1:
            print('请输入邮费：')
            Data.shippment_charge = float(input())
        else:
            print('包邮')

        print("请输入竞品价格")
        Data.opponent_price = float(input())
        if int(Data.shippment_charge_judge) == 1:
            Data.opponent_price = Data.opponent_price + Data.shippment_charge

    # 输入价格的计算参数
    def get_caculate_information(self):
        print('请输入重量:')
        Data.weight = input()

        print("请输入物流价格:")
        Data.freight_charges = float(input())

        print("请输入拿货价格:")
        Data.china_price = float(input())

        print("请输入目标利润:")
        Data.profit = float(input())


    def caculation(self):
        Data.product_price = ((Data.profit + Data.freight_charges + Data.china_price) / Data.exchange_rate) / 0.87
        Data.final_price = Data.product_price / 0.65
        Data.airexpress_commission = Data.product_price * 0.08
        Data.promotion_cost = Data.product_price * 0.05

        # print(product_price,final_price)

    def outpuy_product_bianti_info(self):
        print("#################################变体信息##################################")
        print('变体名称：', Data.product_bianti_name)
        print('重量:', Data.weight)
        print("#######平台抽成#######")
        print('平台佣金：美元$', Data.airexpress_commission)
        print('推广成本：美元$', Data.promotion_cost)
        # print('\033[1;33m 仔细点 \" %s .\"\033[3;31m')
        print("#######价格信息#######")
        print('目标利润: 人民币￥', Data.profit)
        print("物流价格：人民币￥", Data.freight_charges)
        print('拿货价格：人民币￥', Data.china_price)
        print('折扣价格：美元$', Data.product_price)
        print('输出价格：美元$', Data.final_price)

    def output_product_info(self):
        print("#######################################################商品信息###########################################################")
        print('商品名称：', Data.product_name)
        print('商品标题：', Data.product_title)
        print('重量:', Data.weight)
        print('货源地址：', Data.china_product_url)
        print("#######平台抽成#######")
        print('平台佣金：美元$', Data.airexpress_commission)
        print('推广成本：美元$', Data.promotion_cost)
        #print('\033[1;33m 仔细点 \" %s .\"\033[3;31m')

        print("#######价格信息#######")
        print('目标利润: 人民币￥', Data.profit)
        print("物流价格：人民币￥", Data.freight_charges)
        print('拿货价格：人民币￥', Data.china_price)
        print('折扣价格：美元$', Data.product_price)
        print('输出价格：美元$', Data.final_price)

    def ouput_opponent_info(self):
        print("######竞品数据#######")
        print("对手是否包邮：", Data.shippment_charge)
        print('竞品价格：美元$', Data.opponent_price)


if __name__ == '__main__':
    t1 = 1
    t2 = 1
    t3 = 1
    while t1:
        d = Data()
        d.get_information()
        d.get_caculate_information()

        #输入竞争对手的信息
        d.get_opponent_info()

        d.caculation()
        d.output_product_info()

        #输出竞争对手的信息
        d.ouput_opponent_info()
        print("是否有其他变体需要计算(0/1):")
        t2 = int(input())
        while t2:

            d.get_bianti_information()
            d.get_caculate_information()

            # 输入竞争对手的信息
            d.get_opponent_info()

            d.caculation()
            d.outpuy_product_bianti_info()
            d.ouput_opponent_info()

            # 输出竞争对手的信息
            d.ouput_opponent_info()

            print("是否有其他变体需要计算(0/1):")
            t2 = int(input())
        print("是否有其他商品需要计算(0/1):")
        t1 = int(input())


