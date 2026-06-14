# Python 学习笔记与练习 🐍

> **从 C 语言视角学 Python** —— 每一行代码的注释都在对比 C 与 Python 的异同。

跟着网课学习 Python 的完整代码记录，从 Hello World 到面向对象编程。最大的特点是：**所有注释都站在 C 语言学习者的角度**，用类比的方式理解 Python 的新概念。

## 🎯 代码特色（与 C 对比）

| C 语言 | Python | 注释中的对比 |
|--------|--------|-------------|
| `char` 字符串 | `str` 类型 | `"C的字符串数据类型是char，而python里的字符串数据类型为str"` |
| `printf` | `print` | 打印语句里用 `+` 连接不同字符串 |
| 强制类型转换 `(float)` | `float()` 函数 | `"float在这里表示指定输入的数据的类型，类似于C语言里的强制类型转换"` |
| 结构体 `struct` | 类 `class` | `"class定义一个类，类似于C的结构体"` |
| `scanf` | `input()` | `"input在这里表示输入但和C的逻辑很不一样"` |
| 字符数组 | 列表 list | `"python的列表极其灵活，如果用C语言实现它的效果是比较复杂的"` |
| 字符数组索引 | `s[0]` | `"类比C里的字符数组"` |

每份代码文件都保留了原汁原味的学习注释，记录了从 C 到 Python 的思维转换过程。

## 📚 涵盖内容

- **基础语法** — print 输出、变量与类型、字符串操作
- **数学运算** — 数学函数、一元二次方程求解
- **输入与输出** — input、类型转换、BMI 计算器
- **条件判断** — if/elif/else、条件逻辑
- **数据结构** — 列表 (list)、字典 (dict)
- **循环** — while 循环、累加与平均值
- **函数** — 函数定义与调用、BMI 计算函数
- **面向对象** — 类与对象、继承、super()、多态
- **文件操作** — 文件读取与写入
- **单元测试** — unittest 框架、测试用例编写

## 📂 文件结构

| 文件 | 内容 |
|------|------|
| `1_print_demo.py` ~ `7_more_print.py` | print 基础与进阶 |
| `3_variables.py` | 变量与类型、len/type 函数 |
| `10_math.py` | 数学运算、sqrt 函数 |
| `14_input.py` | 输入、BMI 计算器 |
| `15_conditions.py` ~ `16_more_conditions.py` | 条件判断 |
| `18_list.py` | 列表操作 |
| `19_dictionary.py` | 字典、流行语词典 |
| `21_while_loop.py` | while 循环 |
| `24_functions.py` | 函数定义 |
| `28_class_demo.py` | 类与对象、学生成绩管理 |
| `29_inheritence.py` | 继承、员工工资计算 |
| `31_read_file.py` ~ `32_write_file.py` | 文件读写 |
| `shopping_list.py` | 购物清单类 |
| `test_shopping_list.py` | 单元测试示例 |

## 🚀 快速运行

```bash
python 文件名.py
```

## 📌 环境要求

- Python 3.6+
- 无需第三方依赖
