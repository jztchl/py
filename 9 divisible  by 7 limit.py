sum=0
no=0
for i in range(100,200):
    if i%7==0:
        sum+=i
        no+=1
print("no. of integer divisible by 7 is {0} and sum is {1}".format(no,sum))