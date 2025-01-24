def display(data):
    print(f"The area is {data}")

def get_input():
    length=input("enter the length: ")
    width=input("enter the width: ")
    return (length,width)

def compute_area(l,w):
    area=int(l)*int(w)
    return area

def main():
    (length,width)=get_input()
    area=compute_area(length,width)
    display(area)
    
main()
    