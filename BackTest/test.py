a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,4,5]

for i in range(len(b)):
    if a[i:i+len(b)] > b:
        print 'O',
    else:print('X'),

# for i in range(len(b)):
#     print a[i:i+len(b)]

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# print [l for l in list1 if l in list2]
# print [l for l in a if l not in b]
# print a[:3]

# a = ['g','b','a','c','a','c']
# b = ['a','c','a']
# try:
#     for i in range(len(a)):
#         print(i),
#         if b[0]==a[i] and b[1]==[i+1] and b[2]==a[i+2]:
#             print('O')
#         else:print('X')
#         print('----')
#         print b[0],a[i]
#         print b[1],a[i+1]
#         print b[2],a[i+2]
#         print('----')
# except:pass
#
# print('')
# print('')
#
# if b[0]==a[0] and b[1]==a[1] and b[2]==a[2]:
#     print('O')
# else:print('X')
#
# if b[0]==a[1] and b[1]==a[2] and b[2]==a[3]:
#     print('O')
# else:print('X')
#
# if b[0]==a[2] and b[1]==a[3] and b[2]==a[4]:
#     print('O')
# else:print('X')
#
# if b[0]==a[3] and b[1]==a[4] and b[2]==a[5]:
#     print('O')
# else:print('X')
# for i in range(len(a)):
#     for i in range(len(b)):
#         if b[i] == a[i]:
#             print('O'),
#         else:print('X')
#     # i =+ 1
#     i += 1
#
# print('-------------')
# try:
#     for i in range(len(b)):
#         for i in range(len(a)):
#             if b[i] == a[i]:
#                 print('O'),i
#             else:
#                 print('X'),i
# except:pass
#
# print('')
# print('')
#
# try:
#     for i in range(len(a)):
#         for i in range(len(b)):
#             if a[i] == b[i]:
#                 print('O'),
#             else:print('X'),
# except:pass
#
# print('')
# print('')
#
# lenb = len(b)
#
# for i in range(len(a)):
#     for ii in range(lenb):
#         print a[ii],
#         ii += 2

