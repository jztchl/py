given_string=input("enter the string  :")
string_without_vowels=""
for x in given_string:
    if x in ['a','e','i','o','u']:
        continue
    else:
        string_without_vowels=string_without_vowels+x
if string_without_vowels=="":
    print("nothing to print")
else:
    print("given string: "+given_string+"string without vowels: "+string_without_vowels)