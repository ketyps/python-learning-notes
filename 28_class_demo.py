class Student:
#class定义一个类，类似于C的结构体
#def __init__用于定义和初始化这个类具有的成员
#sel.成员名称=传参   用这样的格式对类的成员进行定义和规定输入接口格式
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}
    #创建一个更改某个学科成绩的方法
    #def 方法名() 用于定义这个类可以使用的函数，即为这个类的一个方法，类似于C语言里只对某个特定类型的结构体才能使用的函数
    #方法的传参里第一个传入的值默认为self，表示可以对类的数据进行操作
    def set_grades(self,course,grade):
         if course in self.grades:
            self.grades[course]=grade
    #一个打印一个学生所有学科成绩的方法，没有操作类的数据，所以不需要self以外的传参，打印需要的数据都已包含在self里
    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


chen=Student("小陈","100618")
chen.set_grades("语文",92) 
chen.set_grades("数学",94)
chen.print_grades()


# zeng=Student("小曾","100622")
# print(chen.name)
# print(zeng.grades)

# zeng.set_grades("数学",95)
# print(zeng.grades)