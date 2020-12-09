def fizzBuzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


for num in range(1, 101):
    print(fizzBuzz(num))
