# -*- coding:utf-8 -*-
# 回测  早晨十字星
# 再加一个第三根K线的 收盘价超第一次的开盘价
#时间问题 停牌问题　停牌因素是否引起计数图形的无效性
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
datalist = []
#十字星有红绿 最好第一天跌幅能在input时手动输入%之多少 提示一般为X
#十字星上下影线长度灵活设定  是否上影线越长越好
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data201516
start = '2016-01-04'
end = '2016-07-28'

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

datalistindexstar = schedule.schedule.index(start)
datalistindexend = schedule.schedule.index(end)

for i in range(datalistindexstar,datalistindexend+1):
    datalist.append(schedule.schedule[i])

# print(datalist)
lendata = len(datalist)
ticklen = len(tick.tick)
for ticki in tick.tick:
    for i in range(lendata):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            # for i in range(len(data)):
            #     MA15 = (data[i]['ma']['MA10']+data[i]['ma']['MA20'])/2
            #     MA15_2 = (data[i+1]['ma']['MA10']+data[i+1]['ma']['MA20'])/2
            #     if data[i]['open']>data[i]['close'] and data[i]['open']> MA15:
            #         if data[i+1]['open']>data[i+1]['close'] and data[i+1]['open']>MA15_2:
            #             # if data[i+2]['open']>data[i+2]['close'] and data[i+2]['open']>((data[i+2]['ma']['MA10']+data[i+2]['ma']['MA20'])/2):
            #                 # if data[i+3]['open']>data[i+3]['close'] and data[i+3]['open']>((data[i+3]['ma']['MA10']+data[i+3]['ma']['MA20'])/2):
            #                     print ''
            #                     print data[i]['dt'],data[i]['tick']
            #                     print ('----------------')
            count = 0
            for i in range(len(data)):
                if data[i]['open']>((data[i]['ma']['MA10']+data[i]['ma']['MA20'])/2):
                    count += 1
            print data[0]['tick'],
            print count
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()