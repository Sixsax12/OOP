"""
ให้รับเวลาเข้าและออกของรถให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้น
คำนวณค่าที่จอดรถที่ต้องจ่าย โดยหลักเกณฑ์การคำนวณมีดังนี้  
     1) จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
     2) จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็น
         หนึ่งชั่วโมง
     3) จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของ
         ชั่วโมงคิดเป็นหนึ่งชั่วโมง
     4) จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท

ข้อมูลนำเข้า    
     มี 1 บรรทัด โดยมีจำนวนเต็ม 4 จำนวนคั่นด้วย Space
     โดยจำนวนเต็มที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และจำนวนเต็มที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก

ข้อมูลส่งออก
มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจำนวนเต็ม
กรณี Input ไม่ตรงกับที่ต้องการให้แสดงผลคำว่า "Invalid Input"

ตัวอย่าง Input - Output
Input            |   Output        
7 0 7 15       |   0
7 0 7 16       |   10
7 30 10 30   |   30
7 30 10 31   |   50
7 30 13 31   |   200
7 0 23 1       |   Invalid Input      
"""
try:
    time_in_H,time_in_M,time_out_H,time_out_M = [int(e) for e in input("Enter your input : ").split()]
    min_time_in_H = time_in_H*60
    min_time_out_H = time_out_H*60
    time_in = min_time_in_H+time_in_M
    time_out = min_time_out_H+time_out_M
    sum = time_out-time_in
    if(time_in>=420  and time_out<= 1380 and sum>0 and time_out_M <60 and time_in_M<60):
        if(sum < 15):
            print("0")
        elif(15<=sum<=180):
            if(sum < 60) :
                print("10")
            else :
                amout = (sum//60)
                print(amout*10)
        elif(181<=sum<=360):
            amout = (sum//60)
            if(181<=sum<240):
                print((amout*10)+20)
            else:
                print(3*10 +(amout-3)*20)
        else:
            print("200")
    else:
        print("Invalid Input")
except:
    print("Invalid Input")