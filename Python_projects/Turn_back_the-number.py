n = int(input("Enter a number: "))
while True:
    if n == 0:
        break
    else:
        pass
    r = n % 10
    print(r, end='')
    n //= 10

