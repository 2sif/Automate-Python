def collatz(number):
    if number % 2 == 0: # Even numbers
        result = number // 2
    else: # Odd numbers
        result = number * 3 + 1
    print(result)
    return result

print('Enter an integer: ')
try:
    collatz_result = collatz(int(input()))
    while collatz_result != 1:
        collatz_result = collatz(collatz_result)
except ValueError:
    print('Error: Please enter a valid integer.')