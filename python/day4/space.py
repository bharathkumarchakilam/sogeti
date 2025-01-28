def get_input():
    string1=input("enter the sentences: ")
    return string1

def display(result,reversed):
    print(reversed)
    if(result):
        print("The given sentence is palindrome")
    else:
        print("The given sentence is not palindrome")
        

def palin(str):
    if str == str[::-1]:
        return True
    else:
        return False
            
def remove_space(string1):
    list1 = []
    prev_char = None
    for char in string1:
        if char != ' ' or prev_char != ' ':
            list1.append(char)
        prev_char = char
    return ''.join(list1)

def main():
    string1=get_input()
    list1=remove_space(string1)
    reversed_list=list1[::-1]
    result=palin(list1)
    display(result,reversed_list)
    
main()
    