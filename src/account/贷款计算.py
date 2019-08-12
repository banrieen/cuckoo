""" 最优还款方式计算
1. 微笔还
2. 大笔还
3. 每月还
"""
from datetime import datetime 



def baidu_YouQianHua(days):
    # 百度有钱花 日利率：0.05% 借款方：一般还款日
    # 利率计算： https://jingyan.baidu.com/article/a3aad71a0d2043b1fb0096d6.html
    dayRate = 0.005
    # 日期计算  https://blog.csdn.net/wo1182929447/article/details/77841529
    monthRate = dayRate * 30
    yearRate = monthRate * 12

    days = 0
    huan = 1000 * (1 + 0.0005) * days


def jiebai(days):
    # 支付宝借呗 日利率：0.04.5% 借款方：一般还款日
    dayRate = 0.005
    monthRate = dayRate * 30
    yearRate = monthRate * 12

    days = 0
    huan = 1000 * (1 + 0.0005) * days

def weixin_weiLiDai():
    # 支付宝借呗 日利率：0.04.5% 借款方：一般还款日
    dayRate = 0.005
    monthRate = dayRate * 30
    yearRate = monthRate * 12

    days = 0
    huan = 1000 * (1 + 0.0005) * days