g1 = float(input("Please Enter Your Marks \n"))
g2 = float(input("Please Enter Your Marks \n"))
g3 = float(input("Please Enter Your Marks \n"))
g4 = float(input("Please Enter Your Marks \n"))
g5 = float(input("Please Enter Your Marks \n"))

tt = float(g1+g2+g3+g4+g5)/5

if(tt > 100):
    print("enter corrrect marks ")


if (tt >= 90 and tt == 100):
    print("Congratulation your Grade is Ex","And Your Percentage is",tt)
elif(tt >=80 and tt<90):
    print("Congratulation your Grade is A","And Your Percentage is",tt)
elif(tt >=70 and tt<80):
    print("Congratulation your Grade is B","And Your Percentage is",tt)
elif(tt >=60 and tt<70):
    print("Congratulation your Grade is c","And Your Percentage is",tt)
elif(tt >=50 and tt<60):
    print("Congratulation your Grade is D","And Your Percentage is",tt)
elif(tt >=40 and tt<50):
    print("Congratulation your Grade is E","And Your Percentage is",tt)
elif(tt >=30 and tt<40):
    print("Congratulation your Grade is F","And Your Percentage is",tt)
elif(tt >= 0 and tt <30):
    print("Fail", "Percentage",tt)

else:
    print("Worrng Input", "Percentage",tt)




