def pali(number):
    number_copy=number
    reverse_number=0
    while number_copy>0:
     reverse_number=(reverse_number*10)+(number_copy%10)
     number_copy//=10
    return reverse_number
    if number

number=int(input("enter the number"))
check(number)

