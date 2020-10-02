numbers = list(range(3, 30))
my_prime = [2]

print(my_prime)
for number in numbers:
        for prime in my_prime:
            if number%prime==0:
                break
        else:
            my_prime.append(number)
            print(my_prime)
