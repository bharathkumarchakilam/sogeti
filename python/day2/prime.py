import math
def display(num1,num2):
    for i in range(num1,num2+1):
        if prime(i):
            print(i)
    
def get_input1():
    num1=int(input("enter lower boundary: "))
    return num1

def get_input2():
    num2=int(input("enter upper boundary: "))
    return num2

def prime(num):
    if (num==0 or num==1):
        return False
    if (num==2):
        return True
    if (num%2==0):
        return False
    i=3
    while(i<=math.sqrt(num)):
        if(num%i==0):
            return False
        i+=2
    return True

def main():
    num1=get_input1()
    num2=get_input2()
    while(num1<0 or num2<0 or num1>num2):
        if (num1<0):
            print()
            print("please enter positive value")
            print("provide another lower boundary")
            num1=get_input1()
        elif (num2<0):
            print()
            print("please enter positive value")
            print("provide another upper boundary")
            num1=get_input1()
        else:
            print()
            print("The lower boundary is greater than upper boundary")
            print("provide another lower and upper boundaries")
            num1=get_input1()
            num2=get_input2()
    display(num1,num2)
    
main()
    