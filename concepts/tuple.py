a = (1, 2, 3,9,8,6,4,2,5)
# a[0] = 10  not allowed, tuples are immutable
print(a[0:2])
print (a)
b= (101,102,103,104,105)
c= a[2:4] + (14,12,13,) + b[1:3]
print(c)  
