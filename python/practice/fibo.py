def fibonacci(number):
    if number <= 1:
        return number
    previous_number, current_number = 0, 1
    for _ in range(2, number + 1):
        previous_number, current_number = current_number, previous_number + current_number
    return current_number

number = int(input())
print(fibonacci(number))
