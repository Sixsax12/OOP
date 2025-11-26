try :
    num = [int(e) for e in input("Input : ").split()]
    num.sort()
    for n in num:
        if n < 0 or n > 9:
            exit()
    if(len(num) >10):
        exit()
    if(num[0] == 0 and len(num) > 1):
        for i in range(1,len(num)):
            if(num[i] != 0):
                temp = num[0]
                num[0] = num[i]
                num[i] = temp
                break
    if all(n == 0 for n in num):
        print("Invalid Input")
    else :
        print("".join(map(str,num)))


except:
    print("Invalid Input")