# -*- coding:utf-8 -*-
# report Xdays' close price

import xlrd
import tick
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
#
#----------------------------------------------------------
#---------------------此处修改参数---------------------------


db = conn.db.data201516
datalist = ['2016-07-18','2016-07-19']


#----------------------------------------------------------
#---------------------此处修改参数---------------------------

count = 0
for tick in tick.tick:
    for i in range(0,2):
        for item in db.find({'dt':datalist[i],'tick':tick}):
            data.append(item)
    if data != []:
        # 跌幅大于４％　0.04
        try:
            if (1-round(data[0]['open']/data[0]['close'],2)) < -0.04 :
                if data[1]['open']>data[1]['close']:
                    if ((data[1]['open']/data[1]['close'] - 1) * 100) < 0.5:
                        count += 1
                        print ('No.'),count
                        # 十字星系数好像有点不对　问题不严重
                        print ('十字星系数'),round(((data[1]['open']/data[1]['close'] - 1) * 100),2)
                        print data[0]['dt'],' open ',data[0]['open'],'close',data[0]['close']
                        print data[1]['dt'],' open ',data[1]['open'],'close',data[1]['close']
                        print(data[0]['tick']),('  前一日跌幅为4%以上 今日为早晨十字星 绿')
                        print ('----------------')
                if data[1]['open'] < data[1]['close']:
                    if ((data[1]['close'] / data[1]['open'] - 1) * 100) < 0.5:
                        count += 1
                        print ('No.'),count
                        print ('十字星系数'), round(((data[1]['open'] / data[1]['close'] - 1) * 100), 2)
                        print data[0]['dt'], ' open ', data[0]['open'], 'close', data[0]['close']
                        print data[1]['dt'], ' open ', data[1]['open'], 'close', data[1]['close']
                        print(data[0]['tick']), ('  前一日跌幅为4%以上 今日为早晨十字星 红')
                        print ('----------------')
        except:pass
    del data[:]

