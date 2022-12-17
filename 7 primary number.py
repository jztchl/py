limit=int(input("enter the limit"))
print("primary numbers")
for i in range(2,limit+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
         print(i)