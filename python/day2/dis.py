import dis

def display(mul):
    print(f"the product is {mul}")

dis.dis(display)
    
def input_val():
    first=int(input("enter the first number: "))
    second=int(input("enter second number: "))
    return first,second

def product(first,second):
    return first*second

def main():
    first,second=input_val()
    mul=product(first,second)
    display(mul)
main()