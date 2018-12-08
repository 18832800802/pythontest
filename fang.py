dict = {'数学':'99','语文':'96','英语':'95'}
print('数学的成绩为:',dict['数学'])
print('语文的成绩为:',dict['语文'])
print('英语的成绩为:',dict['英语'])
dict['物理'] = 100
print('物理的成绩为:',dict['物理'])
dict['物理'] = 90 #更改字典的值
print('物理的成绩为:',dict['物理'])
del dict['数学']
print(dict)
print(type(dict))
