import dis
import array as arr
def display(num,loc):
    print(f"The biggest number is {num} and stored in ar({loc})")
    
def length():
    n=int(input("enter the n value: "))
    return n
    
def input_val(arrr,n):
    for i in range(n):
        a=int(input(f"enter {i+1} number: "))
        arrr.insert(i,a)
    return arrr

def biggest(ar,n):
    max=ar[0]
    t=''
    for i in range(n):
        for num in ar:
            if num > max:
                max=num
                t=i
    return max,i

def main():
    n=length()
    arrr=arr.array('i',[])
    ar=input_val(arrr,n)
    maximum,location=biggest(ar,n)
    display(maximum,location)
main()
    
    

