def display(small,large):
    print(f"The smallest element in the list: {small}")
    print(f"The largest element in the list: {large}")
    
def list_size():
    size = int(input("Enter the size of the list: "))
    return size

def get_input(n):
    list2 = []
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        list2.append(num)
    return list2

def sort_list(list2):
    list.sort(list2)
    return list2
    

def find_small(l2):
    return l2[0]

def find_large(l2):
    return l2[-1]

def main():
    rang = list_size()
    list_2 = get_input(rang)
    list2 = sort_list(list_2)
    small = find_small(list2)
    large = find_large(list2)
    display(small,large)

main()