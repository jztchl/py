first=int(input("enter first operand :"))
second=int(input("enter second operand :"))
operator=int(input("choose operation  1.addition 2.subtration 3.multiplication 4.division"))
if operator==1:
    print("{0}+{1}={2}".format(first,second,first+second))
elif operator==2:
    print("{0}-{1}={2}".format(first,second,first-second))
elif operator==3:
    print("{0}*{1}={2}".format(first,second,first*second))
elif operator==4:
    print("{0}/{1}={2}".format(first,second,first/second))
else:
    print("please choose a valid operator")