recoreded_unit=int(input("enter the number of units recoreded : "))
if 0<=recoreded_unit<=200:
    bill_amount=recoreded_unit*0.5
elif 201<=recoreded_unit<=400:
    excess=recoreded_unit-200
    bill_amount=(excess*0.65)+(200*0.5)
elif 401<=recoreded_unit<=600:
    excess=recoreded_unit-400
    bill_amount=(excess*0.80)+(400*0.5)
else:
    excess=recoreded_unit-600
    bill_amount=(excess)+(600*0.5)
    
if bill_amount<100:
    bill_amount=100
    
if bill_amount>400:
    surcharge=(bill_amount/100)*15
    bill_amount+=surcharge
    
print("You have to pay {0} for {1} units of electricty".format(bill_amount,recoreded_unit))
