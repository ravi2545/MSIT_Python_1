my_prime = []
for pr in range(2, 30):
    isPrime = True
    for i in range(2, pr):
        if pr % i == 0:
            isPrime = False
        if isPrime:
            my_prime.append(pr)
        print(my_prime)
