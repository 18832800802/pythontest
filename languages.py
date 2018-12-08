favorite = {'张三':'python','李四':'C','王五':'Ruby','赵六':'Java'}
#for name in favorite.keys():
 #   print(name.title())
for name in sorted(favorite.keys()):
    print(name + '是我的好同事')
print(favorite.values())