#printing the average
def print_avg(avg):
    print(f"the average of the numbers is {avg}")
 
 #input   
def get():
    n=int(input("enter n value:"))
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=int(input("enter third number: "))
    d=int(input("enter fourth number: "))
    return n,a,b,c,d

#calculating the sum
def calculate_sum(a,b,c,d):
    sum=a+b+c+d
    return sum

#calculating the average
def calculate_avg(sum,n):
    avg=sum/n;
    return avg

#main function
def main():
    n,a,b,c,d=get()
    sum=calculate_sum(a,b,c,d)
    avg=calculate_avg(sum,n)
    print_avg(avg)
    
main()
    


    