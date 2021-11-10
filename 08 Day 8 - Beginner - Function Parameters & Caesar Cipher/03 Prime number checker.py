def print_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Is prime number")
    else:
        print("Is not prime number")

n = int(input("Check this number: "))
print_number(number=n)