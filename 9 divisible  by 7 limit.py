sum=0
no=0
i=100
while i!=NULL
    if i%7==0:
        sum+=i
        no+=1
    else:
        continue
    if i==200:
       break
print("no. of integer divisible by 7 is {0} and sum is {1}".format(no,sum))
