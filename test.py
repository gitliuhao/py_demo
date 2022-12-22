# 假设此时a的引用为1
a = [1, 2]

# 假设此时b的引用为1
b = [3, 4]

# 循环引用
a.append(b)
# b的引用+1=2
b.append(a)
del b

print(a, len(a))
# print(b)
