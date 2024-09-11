# coding: utf-8
x = [0,1,2,3,4,5,6,7,8,9]
x[0] = -1
print(x)
first_three = x[:3]
print(first_three)
three_to_end = x[3:]
print(three_to_end)
one_to_four = x[1:4]
print(one_to_four)
one_to_four = x[1:5]
print(one_to_four)
last_three = x[-3:]
print(last_three)
without_first_and_last = x[1:-1]
print(without_first_and_last)
copy_of_x = x[:]
print(copy_of_x)
every_third = x[::3]
print(every_third)
every_fourth = x[::4]
print(every_fourth)
five_to_three = x[5:2:-1]
print(five_to_three)
five_to = x[5:2:-2]
print(five_to)
pattern = x[1:5:2]
print(pattern)
pattern_two = x[8:1:-3]
print(pattern_two)
1 in [1,2,3]
3 in [1,2,3,4,5]
0 in [1,2,3]
x = [1,2,3]
x.extend([4,5,6])
print(x)
x = [1,2,3]
y = x + [4,5,6]
print(y)
print(x)
x.append(0)
print(x)
y =x[-1]
print(y)
z = len(x)
print(z)
x, y =[1,2]
print(x)
print(y)
_, y = [1,2]
print(_,y)
print(y)
get_ipython().run_line_magic('cd', '')
