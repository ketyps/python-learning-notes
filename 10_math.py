import math #这是python用到的数学函数库的模块，在这里提供sqrt函数使用
#模拟一元二次方程求根公式运算，理解python的数学逻辑
a=1
b=9
c=20

delta=b**2-4*a*c #运算并赋值一个德尔塔
print((-b+(b**2-4*a*c)**(1/2))/(2*a)) # b**2 表示对b进行幂指数运算，值为b的二次方
print((-b-math.sqrt(delta))/(2*a)) # 直接使用已定义的delta配合sqrt函数（此函数用于开方运算）表示德尔塔看起来会更直观