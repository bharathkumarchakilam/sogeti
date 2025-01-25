def display(num,var):
    print(f"The biggest number is {num} stored in {var}")
    
def get_input():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=int(input("enter third number: "))
    d=int(input("enter fourth number: "))
    return a,b,c,d

def find_biggest(a,b,c,d):
    if(a>b and a>c and a>d):
        return a,'a'
    elif(b>a and b>c and b>d):
        return b,'b'
    elif(c>a and c>b and c>d):
        return c,'c'
    else:
        return d,'d'
    
def main():
    a,b,c,d=get_input()
    max,var=find_biggest(a,b,c,d)
    display(max,var)
    
main()