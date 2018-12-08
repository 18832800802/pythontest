miantiao = {'型号':'拉面','配料':['多加10元的肉','多放辣椒']}
print('您点了一份：' + miantiao['型号'] + '，您提出了以下配料要求') 
for topping in miantiao['配料']:
    print('\t'+ topping)
#copy复制字典
dict = miantiao.copy()
print(dict)
print('字典长度为:%d' % len(miantiao))
# miantiao.clear()#clear（）清空字典
print('字典长度为:%d' % len(miantiao))

print('本面馆提供%s'% miantiao.get('型号'))
print('本面馆提供%s'% miantiao.get('配料'))
#setdefault与get类似但是会添加不存在的键值
print('本面馆提供%s'% miantiao.setdefault('炒饼'))
print(miantiao)
miantiao['炒饼'] = '本店没有'
print(miantiao)
miantiao_0 = {'新增':'西红柿炒鸡蛋'}
#update（）更新字典，将另外一个字典的值放入原字典
miantiao.update(miantiao_0)
print(miantiao)

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