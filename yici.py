user = {'网名':'浪潮之巅','外号':'浪潮第一帅','职业':'程序员'}
for key, value in user.items():#创建两个变量，对应键与值
    print('\nkey: ' + key)
    print('value: ' + value)
print(list(user.values()))