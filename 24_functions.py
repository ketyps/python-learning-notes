
def calculate_BMI(height,weight):
    BMI = weight/(height)**2
    if BMI<=18.5:
        print("您的BMI值分类为偏瘦。")
    elif 18.5<BMI<=25:
        print("您的BMI值分类为正常。")
    elif 25<BMI<=30:
        print("您的BMI值分类为偏胖。")
    else:
        print("您的BMI值分类为肥胖。")
    return BMI

height=float(input("您的身高是:"))
weight=float(input("您的体重是:"))
print("您的BMI值为",calculate_BMI(height,weight))

#python创建函数的规则
# def 函数名(参数1, 参数2, ...):
#     """可选的文档字符串"""
#     #函数体
#     return 返回值可选，若无则返回 None