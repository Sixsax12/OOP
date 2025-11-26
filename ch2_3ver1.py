"""
เขียนโปรแกรมรับ input เป็นประเภท string ในรูปแบบ List ของ Integer เช่น Enter your input : [1, 3, 5, 2, 6]
ให้หาคู่ของตัวเลข 2 ตัวใน List ที่คูณกัน ได้ค่ามากที่สุด
กรณี Input ไม่ต้องกับที่ต้องการให้แสดงผลคำว่า "Invalid Input"
ตัวอย่าง Input-Output
Input            |    Output
[0,0,0,0]       |    0
[1, 3]            |    3
[1, 3, 2, 2]    |    6     
"""
try:
    num  = input("Enter your input : ")
    content = num[1:-1].strip()
    part = [int(e) for e in content.split(",")]
    part.sort(key=lambda x: abs(int(x)))
    if(len(part)>=2):
        num1 = part[-2]
        num2 = part[-1]
        print(num1*num2)

    else:
        print("Invalid Input")
except:
    print("Invalid Input")