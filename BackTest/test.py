# -*- coding:utf-8 -*-
import os
import time
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
report_time = time.strftime("%Y-%m-%d", time.localtime())
if os.path.exists('/home/feheadline/PycharmProjects/ichinascope/Report/'+report_time+'-每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/home/feheadline/PycharmProjects/ichinascope/Report/'+report_time+'-每日复盘')
    print 'Created Report '+report_time+'-每日复盘'

report_address = '/home/feheadline/PycharmProjects/ichinascope/Report/' + report_time + '-每日复盘/MorningCross.txt'
f = open(report_address, 'a+')
print('--')
f.write('\n')
f.write('aaa\n')
f.write('bbb\n')