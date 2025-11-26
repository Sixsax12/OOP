try:
    num  = input("Enter your input : ")
    content = num[1:-1].strip()
    part = [int(e) for e in content.split(",")]
    part.sort()
    num3 = part[0]
    num4 = part[1]
    num1 = part[-2]
    num2 = part[-1]
    min = num3*num4
    max =num1*num2
    if(len(part)>=2):
        if(abs(min)>abs(max)):
            print(abs(min))
        else:
            print(abs(max))

    else:
        print("Invalid Input")
except:
    print("Invalid Input")