## you have to make  afunction which will take strung and it will return reveresed string 
## abcd so it should return dcba


def ummbanana(x):
    j = -1
    s = ""
    for i in x:
        s = s + x[j]
        j = j - 1
    return s

print(ummbanana("andy"))
