# make a function when you will pass it a number
# it will take even numbers till that number
# at th end it will show us sum

## example 
## n = 10 itit will print 0 2 4 6 8 
## it will take sum of these numbers which will be 20



def buttfly(a):
    banana = []
    for i in range(0, a):
        if i % 2 == 0:
            banana.append(i)
    su = 0
    for i in banana:
        su += i
    return su


print(buttfly(200000))