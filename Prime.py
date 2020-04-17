#num = int(input('Enter a no.'))
def isPrime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
