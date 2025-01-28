def get_input():
    nums = [int(input(f"Enter number {i+1}:")) for i in range((int(input("Enter the size of nums:"))))]
    return nums

def smallest(nums):
    small = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < small:
            small = nums[i]
    
    return small

def biggest(nums):
    big = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > big:
            big = nums[i]

    return big

def main():
    nums = get_input()
    print("Smallest Number:", smallest(nums))
    print("Biggest Number:", biggest(nums))

main()