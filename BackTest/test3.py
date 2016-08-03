# -*- coding:utf-8 -*-
# 早晨十字星
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
start = '2016-07-20'
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
    for i in range(len(data)):
        # if i<len(data)-1 and ((1-round(data[i]['open']/data[i]['close'],2)) < -0.04):
            if ((data[i]['open']/data[i]['close'] - 1) * 100) < 0.5:
                if data[i]['open']>data[i]['close']:
                    count += 1
                    print('')
                    print ('No.'),count
                    # 十字星系数好像有点不对　问题不严重
                    print ('十字星系数'),round(((data[i]['open']/data[i]['close'] - 1) * 100),2)
                    print data[i]['tick'],' 首日跌幅为4%以上 ', data[i]['dt'] ,'为早晨十字星 绿'
                    print ('%19s' % 'open '),('%8s' % 'close'),('%8s' % 'amplitude'),('%6s' % 'vol')
                    amplitudelist = []
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        amplitudelist.append(amplitude)
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        if amplitude == max(amplitudelist):
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                '->',('%5.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        if amplitude != max(amplitudelist):
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                ('%8.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                    print ('----------------')
                if data[i]['open']<data[i]['close']:
                    count += 1
                    print('')
                    print ('No.'),count
                    # 十字星系数好像有点不对　问题不严重
                    print ('十字星系数'),round(((data[i]['open']/data[i]['close'] - 1) * 100),2)
                    print data[i]['tick'],' 首日跌幅为4%以上 ', data[i]['dt'] ,'为早晨十字星 红'
                    print ('%19s' % 'open '),('%8s' % 'close'),('%10s' % 'amplitude'),('%6s' % 'vol')
                    amplitudelist = []
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        amplitudelist.append(amplitude)
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        if amplitude == max(amplitudelist):
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                '->',('%5.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        if amplitude != max(amplitudelist):
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                ('%8.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                    print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()