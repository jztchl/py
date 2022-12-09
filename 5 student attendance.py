class_held=int(input("enter number of class held  :"))
class_attended=int(input("enter number of class attended  :"))
percentage=class_attended/class_held*100
if percentage>75.0:
    print("student attendance:{}%  eligible to sit in exam".format(percentage))
else:
     print("student attendance:{}%  not eligible to sit in exam".format(percentage))