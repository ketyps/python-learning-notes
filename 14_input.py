#BMI=体重/（身高**2）
# float在这里表示指定输入的数据的类型，类似于C语言里的强制类型转换
# input在这里表示输入但和C的逻辑很不一样，执行时在输入前可以附带输出一次信息
user_weight=float(input("请输入您的体重(单位:kg)"))
user_height=float(input("请输入您的身高(单位:m)"))
user_BMI = user_weight/(user_height)**2
print("您的BMI值为:" + str(user_BMI)) 
#str把user_BMI转换为字符串后才能print输出，是的，C的字符串数据类型是char，而python里的字符串数据类型为str