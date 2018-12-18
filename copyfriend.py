def copy(friend,relatives):
    while friend:
        current_design = friend.pop()
        print('复制好友:   ' + current_design)
        relatives.append(current_design)
def qinren(relatives):
    print('\n下面的好友已经完成复制')
    for completed_model in relatives:
        print(completed_model)
friend = ['1','2','3','4','5']
relatives=[]
copy(friend,relatives)
qinren(relatives)
sum = lambda arg1,arg2:arg1+arg2
print(sum(10,20))
print(sum(1,20))
