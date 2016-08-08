data12 = [1,2,13,4,5,6,7,8,9,10,11,12]

print (max(data12[:6])*1.0/min(data12[6:12]))
if data12[-1]>data12[-2]:
    print('yes')
print max(data12)*0.7

if (max(data12[:6])/min(data12[6:12]))>1.1:
    if data12[-1]>data12[-2]:
        if data12[-1]>(max(data12)*0.7):
            print ''
            print '3'
            print 'data12'
            # print data[0]['dt'], data[0]['tick'], '--', data[11]['dt']
del data12[:]