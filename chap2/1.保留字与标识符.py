# 1. 可以使用 python 内置模块 进行查询关键字
import keyword
print(keyword.kwlist) # 打印保留字
print(len(keyword.kwlist)) # 打印保留字个数

# 2.保留字严格区分大小写
true = '真' # 可以用
# True = '真' # True 是保留字 SyntaxError: cannot assign to True



"""
# Python 标识符的命名规则
》可以是字符（英文、中文）、下划线“”和数字，并且第一个字符不能是数字
》不能使用Python中的保留字
》标识符严格区分大小写
》以下划线开头的标识符有特殊意义，一般应避免使用相似的标识符
》允许使用中文作为标识符，但不建议使用
》模块名尽量短小，并且全部使用小写字母，可以使用下划线分隔多个字母。例如： grame _main
》包名尽量短小，并且全部使用小写字母，不推荐使用下划线。例如：com.ysjpython ，不推荐使用com _ysjpython
》类名采用单词首字母大写形式(Pascal风格)。例如：MyClass
》模块内部的类采用 “” + Pascal 风格的类名组成，例如：在MyClass中的内部类_InnerMyClass函数、类的属性和方法的命名，全部使用小写字母，多个字母之间使用下划线分隔
》常量命名时采用全部大写字母，可以使用下划线
》使用单下划线 ”_”开头的模块变量或函数是受保护的，在使用"from xxx import *”语句从模块中导入时，这些模块变量或函数不能被导入
》使用双下划线”__”开头的实例变量或方法是类私有的
》 以双下划线开头和结尾的是Python的专用标识，例如： __init__() 表示初始化函数
"""
