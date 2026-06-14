#python的列表极其灵活，如果用C语言实现它的效果是比较复杂的
#使用方法简单，初始化之后用 对象.方法 的语句操作已初始化列表

shopping_list = []
shopping_list.append("键盘") #演示.append添加列表成员
shopping_list.append("键帽")
shopping_list.append("键帽")
shopping_list.append("音响")
shopping_list.append("电竞椅")

print(shopping_list)

shopping_list.remove("键帽") #演示.remove 删除成员，会删除第一个匹配的
shopping_list[1]="硬盘" #用中括号和序号进行索引，达到精准输出和输入的效果
print(shopping_list[1])
print(len(shopping_list)) #依旧len函数可以取模

# 常见的函数调用
price=[799,1024,200,800]
max_price=max(price)
min_price=min(price)
sorted_price=sorted(price) #sorted是排序函数
print(max_price)
print(min_price)
print(sorted_price)