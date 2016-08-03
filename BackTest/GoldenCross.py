# -*- coding:utf-8 -*-
# 早晨十字星
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

db = conn.db.data2016
start = '2016-07-27'
span = 3

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)

count = 0
ticklen = len(tick.tick)

for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            if data[0]['macd']['DIFF']<0 and data[0]['macd']['DEA'] < 0:
                if data[1]['macd']['DIFF']<0 and data[1]['macd']['DEA'] < 0:
                    if data[2]['macd']['DIFF']<0 and data[2]['macd']['DEA'] < 0:
                        if data[0]['macd']['DEA']>data[0]['macd']['DIFF']:
                            if abs(data[2]['macd']['MACD']) <= 0.1:
                                count += 1
                                print('')
                                print 'No. ',count
                                print data[2]['dt']
                                print data[2]['tick']
                                print '----------------'
        except:pass
    del data[:]
    # print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    # sys.stdout.flush()