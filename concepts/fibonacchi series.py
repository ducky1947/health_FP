def fibonachi(n,a,b):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

a=0
b=1
fibonachi(5,a,b)