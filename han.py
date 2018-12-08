#定义函数求和
def tp1_sum(T):
    result = 0
    for i in T:
        result += i #result=result + i
    return result
a = (1,2,3,4)
b =[2,3]
c = [2.3,3]
print(tp1_sum(a))#使用函数
print(tp1_sum(b))#使用函数
print(tp1_sum(c))#使用函数 
def printme(str):
    print(str);
    return;
printme(str='python')
def printinfo(name,age=35):
    print('名字',name);
    print('年龄',age);
    return;
printinfo(age = 50,name = '张三')
printinfo(name = '李四')
printinfo(name = '王五',age = 32)
#不定长参数
#定义是参数前面加个*号，代表一个列表
print('--------------------------------------------------')
def printle(age,*age_0):
    print('输出')
    print(age);
    for i in age_0:
        print(i);
    return;
printle(age=2)
printle(1,3,4,5,6)
#按照引用传递参数
def chuandi(mylist):
    mylist.append([1,2,3,4,5]);
    print('函数内部取值:', mylist)
    return;
mylist = [10,20,30]
chuandi(mylist)
print('函数外部值为：',mylist)
