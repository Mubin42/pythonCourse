for n in range(1,101):
    isPrime = False
    if (n == 1):
        pass
    else:
        for i in range(2, n):
            if (n % i == 0):
                break
        else:
            isPrime = True

    if (isPrime == False):
        pass

    else:
        print(n, end=" ")