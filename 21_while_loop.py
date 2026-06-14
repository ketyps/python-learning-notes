i=input("请输入数字(输入q结束):")
sum=0
cnt=0
while i!='q':        #q为字符串类型数据需要引号括起来
    sum+=float(i)    #i由intput函数输入必定是字符串类型数据所以需要转换为int类型
    i=input("下一个累加的数字是:(输入q结束)")
    cnt+=1

print("累加结果为",sum)
print("共累加",cnt,"个数字")

if cnt!=0:          #if判断防/0报错
    ave=float(sum/cnt)
    print("平均值为",ave)