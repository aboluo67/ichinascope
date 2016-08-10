a = [1,2,3,4,5,6]
b = [2,3,4]
b1 = [1.9,2.9,3.9]
b2 = [2.1,3.1,4.1]
for i in range(len(a)-len(b)+1):
    if b1<a[i:i+len(b)]<b2:
        print 'O',
    else:print 'X',


# for i in range(len(a)):
#     for ii in range(len(b)):
#         print b[ii],a[i]
#         if b[ii] == a[i]:
#             print '-------'
#             print 'YES'

# print a[1:4]
#
# if b == a[1:4]:
#     print 'YES'
# print '-----'
#
# a = [1,2,3,4,5,6]
# b = [2.1,3.1,4.9]
# for i in range(len(a)-len(b)+1):
#     if a[i:i+len(b)]<b< :
#         print 'O',
#     else:print 'X',


c=[]
c.append(1.1)
print c