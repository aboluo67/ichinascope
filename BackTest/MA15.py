# # -*- coding:utf-8 -*-
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
datalist = []
ticklen = len(tick.tick)
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2016-07-27'
span = 2

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
counti = []
for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            if data[0]['close'] > ((data[0]['ma']['MA10'] + data[0]['ma']['MA10']) / 2):
                count += 1
                print ''
                print 'No.', count
                print data[0]['tick'], data[0]['dt']
                print 'MA15:',((data[0]['ma']['MA10'] + data[0]['ma']['MA10']) / 2),\
                    ' Close:',(data[0]['close']),' 系数比:',\
                    round(((data[0]['close']-((data[0]['ma']['MA10'] + data[0]['ma']['MA10']) / 2))/((data[0]['ma']['MA10'] + data[0]['ma']['MA10']) / 2))*100,2)
                #系数比 (close-ma15)/ma15
                counti.append(count)
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
print ''
print '---------------------'
print '总结：今日共',ticklen,'只股票.'
print '其中 收盘价 高于 MA15 的股票共',count,'只,'
print '占比','%.2f%%' % ((float(counti[-1]) / ticklen) * 100)

