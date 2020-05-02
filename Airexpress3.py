import sys
import re
import json
import pickle

class Data:
    exchangerate = 7
    discount = 0.65
    producttitle = None
    finalprice = None
    productname = None
    chinaprice = None
    productprice = None
    weight = None
    freightcharges = None
    chinaproducturl = None
    profit = None
    shippmentcharge = None
    opponentprice = None
    promotioncost = None
    airexpresscommission = None
    Feature = None
    Specication = None
    shippmentchargejudge = None
    productbiantiname = None

    def As_dict_save(self):
        d2 = Data.__dict__
        print({key: d2[key] for key in d2 if '_' not in key})
        # with open ('上架产品数据.json','w',encoding='utf-8') as f:
        #     json.dumps(d2,f)

        with open ('上架产品数据.pkl','wb') as f:
            pickle.dumps(d2,f)

    def Open_json(self):
        # with open ('上架产品数据.json','w',encoding='utf-8') as f:
        #     obj = json.loads(f)
        #     print(obj)
        with open ('上架产品数据.pkl','rb') as f:
            obj = pickle.loads(f)
            print(obj)



class Operation:
    # 输入上架产品的文本信息(已完善)
    def getinformation(self):
        t = 1
        print("请输入商品名称:")
        Data.productname = input()

        while t:
            print("请输入产品标题")
            Data.producttitle = sys.stdin.readline()
            print('标题字符串的个数是：', len(Data.producttitle), '个')
            producttitle1 = re.compile(r'\b[a-zA-Z]+\b', re.IGNORECASE).findall(Data.producttitle)
            # 将列表中的大写字母转换成小写
            # 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法
            producttitle2 = [s.lower() for s in producttitle1 if isinstance(s, str) == True]
            print(producttitle2)
            t = 0
            for i in producttitle2:
                count = producttitle2.count(i)
                print('标题中每个单词的出现次数是:')
                print(i, ':', count)
                if count >= 3:
                    print("出现标题关键词次数违规：")
                    print(i, ':', count)
                    print("请重新输入标题！")
                    t = 1

        print("请输入货源url")
        Data.chinaproducturl = input()

    # 输入上架变体的文本信息
    def getbiantiinformation(self):
        print("请输入变体名称:")
        Data.productbiantiname = input()

    # 输入对手的竞品的信息
    def getopponentinfo(self):
        print("####接下来是竞品信息####")
        print("对手是否包邮(0包邮/1不包邮)：")
        Data.shippmentchargejudge = input()
        if int(Data.shippmentchargejudge) == 1:
            print('请输入邮费：')
            Data.shippmentcharge = float(input())
        else:
            print('包邮')

        print("请输入竞品价格")
        Data.opponentprice = float(input())
        if int(Data.shippmentchargejudge) == 1:
            Data.opponentprice = Data.opponentprice + Data.shippmentcharge

    # 输入价格的计算参数
    def getcaculateinformation(self):
        print('请输入重量:')
        Data.weight = input()

        print("请输入物流价格:")
        Data.freightcharges = float(input())

        print("请输入拿货价格:")
        Data.chinaprice = float(input())

        print("请输入目标利润:")
        Data.profit = float(input())

    def caculation(self):
        Data.productprice = ((Data.profit + Data.freightcharges + Data.chinaprice) / Data.exchangerate) / 0.87
        Data.finalprice = Data.productprice / 0.65
        Data.airexpresscommission = Data.productprice * 0.08
        Data.promotioncost = Data.productprice * 0.05

    def outpuyproductbiantiinfo(self):
        print("#################################变体信息##################################")
        print('变体名称：', Data.productbiantiname)
        print('重量:', Data.weight)
        print("#######平台抽成#######")
        print('平台佣金：美元$', Data.airexpresscommission)
        print('推广成本：美元$', Data.promotioncost)
        # print('\033[1;33m 仔细点 \" %s .\"\033[3;31m')
        print("#######价格信息#######")
        print('目标利润: 人民币￥', Data.profit)
        print("物流价格：人民币￥", Data.freightcharges)
        print('拿货价格：人民币￥', Data.chinaprice)
        print('折扣价格：美元$', Data.productprice)
        print('输出价格：美元$', Data.finalprice)

    def outputproductinfo(self):
        print(
            "#######################################################商品信息###########################################################")
        print('商品名称：', Data.productname)
        print('商品标题：', Data.producttitle)
        print('重量:', Data.weight)
        print('货源地址：', Data.chinaproducturl)
        print("#######平台抽成#######")
        print('平台佣金：美元$', Data.airexpresscommission)
        print('推广成本：美元$', Data.promotioncost)
        # print('\033[1;33m 仔细点 \" %s .\"\033[3;31m')

        print("#######价格信息#######")
        print('目标利润: 人民币￥', Data.profit)
        print("物流价格：人民币￥", Data.freightcharges)
        print('拿货价格：人民币￥', Data.chinaprice)
        print('折扣价格：美元$', Data.productprice)
        print('输出价格：美元$', Data.finalprice)

    def ouputopponentinfo(self):
        print("######竞品数据#######")
        print("对手是否包邮：", Data.shippmentcharge)
        print('竞品价格：美元$', Data.opponentprice)


if __name__ == '__main__':
    t1 = 1
    t2 = 1
    O = Data()
    print("是否查看产品数据文件(0（不打开）/1(打开))")
    t3 = int(input())
    if(t3 == 1):
        O.Open_json()

    while t1:
        d = Data()
        o = Operation()
        o.getinformation()
        o.getcaculateinformation()

        #输入竞争对手的信息
        o.getopponentinfo()

        o.caculation()
        o.outputproductinfo()

        #输出竞争对手的信息
        o.ouputopponentinfo()
        print("是否有其他变体需要计算(0/1):")
        t2 = int(input())
        while t2:

            o.getbiantiinformation()
            o.getcaculateinformation()

            # 输入竞争对手的信息
            o.getopponentinfo()

            o.caculation()
            o.outpuyproductbiantiinfo()
            o.ouputopponentinfo()

            # 输出竞争对手的信息
            o.ouputopponentinfo()


            print("是否有其他变体需要计算(0/1):")
            t2 = int(input())
        d.As_dict_save()
        print("是否有其他商品需要计算(0/1):")
        t1 = int(input())



