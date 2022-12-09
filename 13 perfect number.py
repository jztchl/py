def perfect_number(start,end):
    for i in range(start,end):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if i==sum:
            print(i)
print("perfect numbers")
perfect_number(1,1000)