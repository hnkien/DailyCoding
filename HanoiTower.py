# Recursive algorithm for n disk from column a to column b
step = 0
def HaNoiTower(n, a, b):
    global step
    temp = 6-a-b

    if n>1:
        HaNoiTower(n-1, a, temp)
        step = step + 1
        print("Step ", step ,  ": Move from column " , a , " to column ", b)
        HaNoiTower(n - 1, temp, b)
    else:
        step = step + 1
        print ("Step ", step ,  ": Move from column " , a , " to column ", b )

HaNoiTower(3, 1, 3)