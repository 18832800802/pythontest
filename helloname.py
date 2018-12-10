def greet_user(name):
    """显示简单的问候语"""
    print('Hello' + name.title() + '!')
    return
#greet_user(input('请输入名字 '))
#在形参上面添加一个空字符串可让参数变为可选择的
def get_formatted_name(fist_name,last_name,age=''):
    """返回整洁的姓名"""
    if age:#非空字符串为Ture
        full_name=fist_name +' '+last_name+' '+age
    else:
        full_name=fist_name +' '+last_name
    return full_name.title()
name =get_formatted_name('li','dong')
print(name)
name =get_formatted_name('li','dong','23')
print(name)
while True:
    print('\n请输入您的姓名')
    print('\n输入q退出')
    f_name=input('fist_name: ')
    if f_name =='q':
        break
    l_name=input('list_name: ')
    if l_name =='q':
        break
    a_age=input('age= ')
    if a_age =='q':
        break
    formatted=get_formatted_name(f_name,l_name,a_age)
    print('\nHello,' +formatted+'!')