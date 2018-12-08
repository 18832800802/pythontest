#集合是一个无序不重复的序列。如果有重复会进行删除
#集合可以进行集合运算
name = {'1','2','3','4','4'}
print(name)
a = set('abcde')
b = set('abc')
print(a - b)  #a和b的差集
print(a | b)  #a和b的并集
print(a & b)  #a和b的交集
print(a ^ b)  #a和b中不同时存在的元素