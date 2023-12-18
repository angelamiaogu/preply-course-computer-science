## you have to make this sequence
## for example if i pass a list
## x = [10,20,30,40,50]
# it will return me list with shape [10,10,10,10] # second return me sum()->40


# x = [10,12,15,18]
# y = [2,3,3] sum ---> 8

def flybutt(x):
    y = []
    for i in range(0,len(x) - 1):
        print(i)
        y.append(x[i+1] - x[i])
    return y,sum(y)

print(flybutt([3,6,10,14,20]))







