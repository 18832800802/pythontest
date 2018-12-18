def myfun():
    global a#global可让函数使用全局变量
    a = 0
    a += 3
    print('函数内a:',a)
a = 'one'
print(a)
myfun()
print(a)
def users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!!'
        print(msg)
uerename = ['lisan','zhaosi','wangwu']
users(uerename)