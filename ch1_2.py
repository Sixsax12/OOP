def is_palindrome(num):
    return str(num) == str(num)[::-1]

try:
    n = int(input("Enter digits : "))

    if n <= 1:
        exit()
    if n > 7:
        exit()

    start = 10**(n-1)
    end = 10**n - 1

    max_palindrome = 0

    for i in range(end, start - 1, -1):
        if i * i <= max_palindrome:
            break
        for j in range(i, start - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
                break

    print(max_palindrome)

except:
    print("Invalid Input")
