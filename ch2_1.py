try:
    n = int(input("Input : "))
    if n < 0:
        exit()

    for i in range(1, n + 1):
        print(" " * (n - i+1) + "#" * i)

except:
    print("Invalid Input")
