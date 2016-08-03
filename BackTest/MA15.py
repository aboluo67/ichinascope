# # -*- coding:utf-8 -*-
# # 回测  早晨十字星
# # 再加一个第三根K线的 收盘价超第一次的开盘价
# #时间问题 停牌问题　停牌因素是否引起计数图形的无效性
# import sys
# import tick
# import schedule
# from pymongo import MongoClient
# conn = MongoClient('localhost',27017)
# data = []
# datalist = []
# #十字星有红绿 最好第一天跌幅能在input时手动输入%之多少 提示一般为X
# #十字星上下影线长度灵活设定  是否上影线越长越好
# #----------------------------------------------------------
# #---------------------此处修改参数---------------------------
#
# db = conn.db.data201516
# start = '2016-01-04'
# span = 3
# capital_base = 10000
# #----------------------------------------------------------
# #---------------------此处修改参数---------------------------
# print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
# print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
# print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
#
# datalistindex = schedule.schedule.index(start)
#
# for i in range(datalistindex,datalistindex+span):
#     datalist.append(schedule.schedule[i])
#
# print(datalist)
# ticklen = len(tick.tick)
# for ticki in tick.tick:
#     for i in range(0,span):
#         for item in db.find({'dt':datalist[i],'tick':ticki}):
#             data.append(item)
#         if data != []:
#             try:
#                 # print(data[i]['dt'],data[i]['tick'])
#                 if data[i]['open']>((data[i]['ma']['MA10']+data[i]['ma']['MA10'])/2):
#                     print('')
#                     print data[i]['tick'],data[i]['dt'],data[i+1]['dt']
#             except:
#                 pass
#     del data[:]
#     print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
#     sys.stdout.flush()

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
capital_base = 10000
#十字星有红绿 最好第一天跌幅能在input时手动输入%之多少 提示一般为X
#十字星上下影线长度灵活设定  是否上影线越长越好
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data201516
start = '2016-01-04'
span = 10

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
        # 跌幅大于４％　0.04
        try:
            print('')
            for i in range(len(data)):
                if data[i]['open']>((data[i]['ma']['MA10']+data[i]['ma']['MA10'])/2):
                    print data[i]['tick'],data[i]['dt'],capital_base
                i += 1
                if data[i]['open']<((data[i]['ma']['MA10']+data[i]['ma']['MA10'])/2):
                    print data[i]['tick'],data[i]['dt'],capital_base
        except:pass
    del data[:]
    # print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    # sys.stdout.flush()