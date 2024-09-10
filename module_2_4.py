numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers[1:]:

    for j in range(3,9):
        if i % j != 0:
            primes.append(i)
        else:
            not_primes.append(i)
print('Primes:', list(set(primes)))
print('Not_primes:' , list(set(not_primes)))






              
