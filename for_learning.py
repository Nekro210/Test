a = [2,2,1,2,1,3]
for i in range(len(a)):
    try:
       a[a.index(a[i])+1:].index(a[i])
    except:
        print(a[i])