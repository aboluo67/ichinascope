# -*- coding:utf-8 -*-
# 模仿回测 按照某只股票近几日的走势 查找近一段时间所有的股票是否有类似
import sys
import tick
import schedule
from pymongo import MongoClient
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
reference_tick = '600149'
reference_start = '2016-07-25'
reference_span = 3

start = '2016-03-23'
span = 30

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

reference_index = schedule.schedule.index(reference_start)
for i in range(reference_index,reference_index + reference_span):
    reference_datalist.append(schedule.schedule[i])
    for item in db.find({'dt':schedule.schedule[i],'tick':reference_tick}):
        reference_data.append(item)
# print 'reference_data', reference_data
print reference_datalist
if reference_data == []:
    print reference_tick,'数据不存在,请确认是否停牌'
reference_day = []
for i in range(len(reference_data)):
    reference_day.append(round(reference_data[i]['close']/reference_data[i]['open'],2))

print 'reference_day', (reference_day)

datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)
count = 0
data3 = []
ticklen = len(tick.tick)
for ticki in tick.tick:
    try:
        for i in range(len(datalist)):
            for item in db.find({'dt':datalist[i], 'tick':ticki}):
                data.append(item)
        for i in range(reference_span):
            if (reference_day[i]*0.98)<data[i]['close']/data[i]['open']<(reference_day[i]*1.02):
                data3.append(data[i])
                print len(data3)
        if len(data3) == reference_span:
            print data3[0]['dt'],data3[1]['dt'],data3[2]['dt']
            print data3[0]['tick'],data3[1]['tick'],data3[2]['tick']
            print data3[0]['close']/data3[0]['open'],data3[1]['close']/data3[1]['open'],\
                data3[2]['close']/data3[2]['open']
        del data3[:]
    except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()







# for ticki in tick.tick:
#     try:
#         for i in range(len(datalist)):
#             for item in db.find({'dt':schedule.schedule[i],'tick':ticki}):
#                 data.append(item)
#         for i in range(len(data)):
#             if (reference_day[i]*0.9)<(data[i]['close']/data[i]['open'])<(reference_day[i]*1.1):
#                 data3.append(data[i])
#         if len(data3) == len(reference_data):
#             print data3[0]['tick'],data3[0]['dt']
#     except:pass
#     del data[:]
#     print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
#     sys.stdout.flush()