# 1、一行代码实现1--100之和

print(sum([i for i in range(1, 101)]))


# 2、如何在一个函数内部修改全局变量

AT = "ABC"


def m():
    global AT
    AT = "A"


print(AT)
m()
print(AT)


# 3、列出5个python标准库
"""
os提供了不少与操作系统的关联函数
sys 通常用于命令行参数
re 正则匹配
math 数学运算
datetime 处理时间日期
"""

# 4、字典如何删除键和合并两个字典
d = {
    "name": "liuhao",
    "age": "27"
}
del d["name"]
print(d)
d2 = {"name": "liuhao"}
d.update(d2)
print(d)

# 5、谈下python的GIL
"""
GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开、使其他线程运行。
所以在多线程中，线程的运行仍是有先后顺序的，并不是同一时间进行。

多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所有多进程可以实现多个进程的同时运行，
缺点是进程系统资源开销大
"""

# 6、python实现列表去重的方法
lis = [11, 2, 11, 12, 12, 14, 14, 15, 13, 16, 3]
print(list(set(lis)))

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
"""
*:arg和**kwargs主要用于函数定义。你可以将不定数量的参数传递给一个函数。 这里的不定的意思是：预先并不知道，
函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键词。*args是用来发送一个非键值对的可变数量的参数
列表给一个函数。这里有个例子帮你理解这个概念。
"""

# 8、python2和python3的range（100）的区别
"""
python2返回列表，python3返回迭代器，节约内存
"""
# 9、一句话解释什么样的语言能够用装饰器?
"""
函数可以作为参数传递的语言，可以使用装饰器
"""

# 10、python内建数据类型有哪些
"""
str, int, list, dict, set, bool, None, tuple
"""

# 11、简述面向对象中__new__和__init__区别
"""
__init__是初始化方法， 实例对象实例化后调用的方法， 会将实例对象作为参数传递。
__new__是构造方法，实例化对象之前调用的方法，会将类对象作为参数传递
"""


# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
print([i for i in map(lambda x: x**2, [1, 2, 3, 4, 5]) if i > 10])

# 14、python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy
print(random.randint(10, 20))
print(numpy.random.randn(5))
print(random.random())

# 15、避免转义给字符串加哪个字母表示原始字符串？
print(r"\njdj")

# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re
t = """
<div class="nam">中国</div>
"""
print(re.findall("<div class=\"(.*)\">(.*?)</div>", t))

# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
"""
select distinct name from student
"""

# 19、10个Linux常用命令
"""
pwd, cp, mkdir, kill, lsof, zip, unzip, rar, tar, ps, ls, grep, awk, sh, echo
"""

# 20、python2和python3区别？列举5个
"""
1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')

Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比 如 print 'hi'

2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存

3、python2中使用ascii编码，python中使用utf-8编码

4、python2中unicode表示字符串序列，str表示字节序列

python3中str表示字符串序列，byte表示字节序列

5、python2中为正常显示中文，引入coding声明，python3中不需要

6、python2中是raw_input()函数，python3中是input()函数
"""

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
"""
不可变数据类型：数值型、字符串型string和元组tuple
允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，
只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，
在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。
"""
a = ",".join([str(i) for i in range(1)])
b = ",".join([str(i) for i in range(1)])
print(id(a), id(b))
c = dict(a=1, b=2)
print(id(c), c)
c['c'] = 3
print(id(c), c)

# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
print("".join(sorted(set(s))))

# 23、用lambda函数实现两个数相乘
f = lambda x, y: x*y
print(f(2, 3))

# 24、字典根据键从小到大排序
dic={"name": "zs","age":18,"city":"深圳","tel":"1362626627"}
print(dict(sorted(dic.items(), key=lambda x: x[0])))

# 25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
import collections
s = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
print(collections.Counter(s))

# 26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
a = "not 404 found 张三 99 深圳"
import re
sub_str = re.sub("[a-zA-Z0-9]", "", a)
sub_str = " ".join(i for i in sub_str.split(" ") if i)
print(sub_str)

# 27、filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x%2 == 1, a)))

# 28、列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i for i in a if i%2 == 1])

# 29、正则re.complie作用
"""
re.compute是将正则表达式编译成一个对象，加快速度，并重复使用
"""
s = "abcdk"
re_obj = re.compile("a")
print(re_obj.sub("", s))

# 30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
a = (1, )
b = (1)
c = ("1")
print(type(a))
print(type(b))
print(type(c))

# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
a = [1, 5, 7, 9]
b = [2, 2, 6, 8]
print(a+b)
print(id(a))
a.extend(b)
print(id(a), a)

# 32、用python删除文件和用linux命令删除文件方法
"""
python：os.remove(文件名)
linux: rm 文件名
"""

# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
import datetime
now = datetime.datetime.now()
now_f = now.strftime("%y-%m-%d %H:%M:%S")
print(f"{now_f}, 星期：{now.isoweekday()}")

# 34、数据库优化查询方法
"""
加索引，外键、联合查询、选择特定字段等等
"""

# 35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # 设置图形主题，内置主题类型可查看 pyecharts.globals.ThemeType
# from pyecharts.globals import ThemeType
#
# filepath = r'C:\Users\Administrator\Desktop\myEcharts.html'
# bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# bar.render(filepath)
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# ypoints = np.array([6, 2, 13, 10])
#
# plt.plot(ypoints, linewidth='12.5')
# plt.show()

