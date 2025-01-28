def get_input():
    str=[input("enter the String: ")]
    return str

def palin(str):
    if str == str[::-1]:
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")
        
def main():
    str=get_input()
    palin(str)
    
main()
    
    