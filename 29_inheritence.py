#创建一个通用的父类，存通用的属性和方法
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def print_info(self):
        print(f"员工名字：{self.name},工号：{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id,monthly_salary):
        #用super继承父类的属性
        super().__init__(name, id)
        #继续创建子类特有的属性
        self.monthly_salary=monthly_salary
        #创建子类的方法
    def calculate_monthly_pay(self):
        return self.monthly_salary

#第二个子类依旧继承父类的属性和方法，以及子类特有的属性和方法
class PartTimeEmployee(Employee):
    def __init__(self, name, id,daily_salary,work_days):
        super().__init__(name, id)
        self.daily_salary=daily_salary
        self.work_days=work_days

    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days

#通过组合使用父类的属性和方法，子类的属性和方法，使代码的可读性和可维护性提高
zhangsan=FullTimeEmployee("张三","1001",6000)
lisi=PartTimeEmployee("李四","1002",230,15)
zhangsan.print_info()
lisi.print_info()
print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())