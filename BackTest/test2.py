# -*- coding:utf-8 -*-
# 模仿回测 按照某只股票近几日的走势 查找近一段时间所有的股票是否有类似
import sys
import tick
import schedule
from pymongo import MongoClient
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
conn = MongoClient('localhost',27017)
# 回测数据
data = []
datalist = []
# 参照数据
reference_data = []
reference_datalist = []
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
reference_tick = '300282'
reference_start = '2016-04-15'
reference_span = 3

start = '2016-03-01'
span = 50

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

reference_index = schedule.schedule.index(reference_start)
for i in range(reference_index,reference_index + reference_span):
    reference_datalist.append(schedule.schedule[i])
    for item in db.find({'dt':schedule.schedule[i],'tick':reference_tick}):
        reference_data.append(item)
print reference_data[0]['close'],reference_data[0]['open']
print reference_data[1]['close'],reference_data[1]['open']
print reference_data[2]['close'],reference_data[2]['open']
reference_price = []
for i in range(len(reference_data)):
    reference_price.append(round((1-reference_data[i]['close']/reference_data[i]['open'])*100,2))
print reference_price
reference_price1 = map(lambda x: x-0.10, reference_price)
reference_price2 = map(lambda x: x+0.10, reference_price)
print 'reference_price1:',reference_price1
print 'reference_price2:',reference_price2
datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print('datalist:',len(datalist))
count = 0
data3 = []
ticklen = len(tick.tick)
for ticki in tick.tick:
    try:
        for i in range(len(datalist)):
            for item in db.find({'dt':datalist[i], 'tick':ticki}):
                data.append(item)
        data2 = []
        for i in range(len(data)):
            data2.append(round((1 - data[i]['close'] / data[i]['open']) * 100, 2))
        for i in range(len(data) - reference_span + 1):
            # if reference_price1[0] < data2[i:i+reference_span] <reference_price2[0] and \
            #     reference_price1[1] < data2[i+1:i + reference_span+1] < reference_price2[1] and \
            #         reference_price1[2] < data2[i+2:i + reference_span+2] < reference_price2[2]:
            #             print data[i]['tick'],data[i]['dt']
            if reference_price1[0] < data2[i] < reference_price2[0] and \
                    reference_price1[1] < data2[i + 1] < reference_price2[1] and \
                        reference_price1[2] < data2[i + 2] < reference_price2[2]:
                            print data[i]['tick'], data[i]['dt']

    except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()

    # a = [1, 2, 3, 4, 5, 6]
    # b = [2, 3, 4]
    # b1 = [1.9, 2.9, 3.9]
    # b2 = [2.1, 3.1, 4.1]
    # for i in range(len(a) - len(b) + 1):
    #     if b1 < a[i:i + len(b)] < b2:
    #         print 'O',
    #     else:
    #         print 'X',
#
# ['2016-04-15', '2016-04-18', '2016-04-19']
# reference_day [0.98, 0.99, 1.0]
# ('datalist:', 100)
# 进度 : 72 / 2886 2016-04-21 2016-04-22 2016-04-25
# 300392 300392 300392
# 0.91593046452 0.954470471791 1.005521049
# 进度 : 96 / 2886 2016-03-21 2016-03-22 2016-03-23
# 300087 300087 300087
# 0.997557003257 0.999163179916 0.972928630025
# 进度 : 151 / 2886


# 33.4 34.25
# 32.69 32.89
# 32.84 32.7
# [2.48, 0.61, -0.43]
# reference_price1: [2.38, 0.51, -0.53]
# reference_price2: [2.58, 0.71, -0.32999999999999996]
# ('datalist:', 50)
# 进度 : 25 / 2886 300282 2016-04-15
