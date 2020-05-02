def similar(a,b):
    if a==b:
        return False
    elif len(a)%2!=0:
        return False
    else:
        i=len(a)//2
        return ((similar(a[:i],b[:i]) and similar(a[i:],b[i:])) or (similar(a[:i],b[i:]) and similar(a[i:],b[:i]))
a=input()
b=input()
print(similar(a,b))

