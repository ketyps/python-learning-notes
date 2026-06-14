#python的文件操作演示，文件操作是python的一个精髓，在数据分析等实际生产环境广泛运用

#open后第一个传参为文件路径，有相对路径和绝对路径的区分，这里是相对路径
#第二个传参表示文件操作的类型，这里的r表示只读，不做任何修改，encoding这个传参可有可无，没有时默认为utf-8标准
#with open（）as f：  这个语句表示打开目标文件后对文件执行with后缩进的指令，然后自动关闭
with open(".\data.txt","r",encoding="utf-8") as f:
    # content=f.read()
    # print(content)


    # print(f.readline())
    # print(f.readline())

    lines=f.readlines()
    for line in lines:
        print(line)