def caculation():
    global profit
    global exchange_rate
    global freight_charges
    global china_price
    global discount
    global product_name
    global product_price
    global weight
    global china_product_url
    global final_price
    global airexpress_commission
    global promotion_cost
    global shippment_charge_judge
    global shippment_charge

    product_price = ((profit+freight_charges+china_price)/exchange_rate)/0.87
    final_price = product_price/0.65
    airexpress_commission = product_price * 0.08
    promotion_cost = product_price * 0.05

    #print(product_price,final_price)

def product_info():

    global profit
    global exchange_rate
    global freight_charges
    global china_price
    global discount
    global final_price
    global product_name
    global product_price
    global weight
    global china_product_url
    global promotion_cost
    global airexpress_commission
    global product_title

    print("######商品信息######")
    print('商品名称：',product_name)
    print('商品标题：',product_title)
    print('重量:',weight)
    print('货源地址：',china_product_url)
    print("对手是否包邮：",shippment_charge)

    print("#######平台抽成#######")
    print('平台佣金：美元$', airexpress_commission)
    print('推广成本：美元$', promotion_cost)
    print('\033[1;33m 仔细点 \" %s .\"\033[3;31m' )


    print("#######价格信息#######")
    print('目标利润: 人民币￥',profit)
    print("物流价格：人民币￥",freight_charges)
    print('拿货价格：人民币￥',china_price)
    print('折扣价格：美元$',product_price)
    print('竞品价格：美元$',opponent_price)
    print('输出价格：美元$',final_price)




if __name__ == '__main__':
    t=1
    while t:
        get_information()
        caculation()
        product_info()
        print('是否有变体且需要计算(0/1)：')
        t = int(input())
