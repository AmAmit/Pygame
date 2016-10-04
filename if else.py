num1= int(input("Enter a number:"))
num2= int(input("Enter one more number:"))
print("What do you want to carry out: \n a)Addition \n b)Substraction \n c)Multiplication \n d)Division \n Enter your choice")
choice = input()
    if choice=='a':
            result=num1+num2
    elif choice=='b':
            result= num1-num2
    elif choice=='c':
            result= num1*num2
    else:
        result = num1/num2
    print("Result is", result)


