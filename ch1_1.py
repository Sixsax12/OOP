"""
จงเขียนโปรแกรมที่คํานวณค่าของ a+aa+aaa+aaaa เมื่อรับข้อมูลเป็นตัวเลข 1 หลัก
Input : 9
Output : 11106 (=9+99+999+9999)

ในกรณีที่รูปแบบ Input ไม่ถูกต้อง ให้ output ของโปรแกรมเป็น Invalid Input
"""
try:
    num = str(input("Input : "))
    if(int(num) >=0 and int(num)<=9):
        num1 = num
        num2 = num*2
        num3 = num*3
        num4 = num*4
        cal = int(num1)+int(num2)+int(num3)+int(num4)
        print("Output : "+str(cal))
    else:
        print("Output : Invalid Input")
except:
    print("Output : Invalid Input")

