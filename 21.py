s=int(input("Enter starting day number : "))
l=int(input("Enter length of stay : "))
r=l%7
s=s+r
s=s%7
if s==0 :
    print("return on Sunday")
elif s==1:
    print("Return on Monday")
elif s ==2:
    print("Return on Tueday")
elif s==3:
    print("Return on Wednesday")
elif s==4:
    print("Return on Thursday")
elif s==5:
    print("Return on Friday")
elif s==6:
    print("Return on Saturday")