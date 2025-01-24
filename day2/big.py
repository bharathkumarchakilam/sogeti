import array as arr
def display(num):
    print(f"The biggest number is {num}")
    
def length():
    n=int(input("enter the n value: "))
    return n
    
def input_val(arrr,n):
    for i in range(n):
        a=int(input(f"enter {i+1} number: "))
        arrr.insert(i,a)
    return arrr

def biggest(ar):
    max=ar[0]
    for num in ar:
        if num > max:
            max=num
    return max

def main():
    n=length()
    arrr=arr.array('i',[])
    ar=input_val(arrr,n)
    maximum=biggest(ar)
    display(maximum)
    
main()
    
    

