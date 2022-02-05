T = 1
n, x = 5 ,2
arr =[]
e= [2 ,1 ,4 ,6 ,3]
e.insert(0,0)
for i in range(0,x+1):
    for j in range(0,len(e)):
        or_opern = e[j]|e[j-1]
        arr.append(or_opern)
arr.pop(0)   
print(arr)
