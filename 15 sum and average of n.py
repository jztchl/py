number=int(input("enter no. of numbers"))
sum=0
for i in range(number):
    no=int(input("enter {}th number".format(i+1)))
    sum+=no
print("sum={0} and average={1}".format(sum,sum/number))
