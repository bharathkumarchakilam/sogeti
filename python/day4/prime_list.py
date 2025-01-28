import math
def list_display(num1,num2):
    list_prime=[]
    for i in range(num1,num2+1):
        if prime(i):
            list_prime.append(i)
    print(list_prime)
    list_small(list_prime)
    list_large(list_prime)
    
def list_small(list_prime):
    print(f"The smallest prime in the list is {list_prime[0]}")
    
def list_large(list_prime):
    print(f"The largest prime in the list is {list_prime[-1]}")
    
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
    list_display(num1,num2)
    
main()
    