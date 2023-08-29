num = int(input(
    'Please provide the number you\'d like to determine whether it\'s prime or not:'))
event = 0
if num == 1:
    print(num, 'is not a prime number')
if num >= 2:
    for i in range(2, num):
        if (num % i == 0):
            event = 1
            break
        else:
            event = 0
    if event == 0:
        print(num, 'is a prime number')
    else:
        print(num, 'is not a prime number')
