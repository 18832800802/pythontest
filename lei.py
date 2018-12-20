class MyClass:
    """一个简单的实例"""
    i = 12345
    def f(self):
        return 'Hello Word'
x = MyClass()
print('类MyClass中的属性i为:',x.i)
print('类MyClass中的方法f输出为',x.f())
class SmplClass:
    def info(self):
        print('我定义的类!')
    def mycacl(self,x,y):
        return x+y
sc = SmplClass()
print('调用info方法的结果： ')
sc.info()
print('调用mycacl方法的结果： ')
print(sc.mycacl(10,20))