number=input("enter the number")
sum=0
dproduct=1
for x in number:
    sum+=int(x)
    dproduct*=int(x)
print("product :{0} sum :{1}".format(dproduct,sum))