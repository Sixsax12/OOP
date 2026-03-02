from abc import ABC,abstractmethod
class Cinema:
    def __init__(self):
        self.__user_list = []
        self.__movie_list = []

    def add_user(self,user):
        self.__user_list.append(user)

    def add_theater(self,theater):
        self.__movie_list.append(theater)

    def book_seat(self, citizen_id,theater_number,seat_id):
        target_user = None
        for user in self.__user_list:
            if user.citizen == citizen_id:
                target_user = user
                break
        if not target_user: 
            raise Exception("User not found") 
        
        target_seat = None
        for theater in self.__movie_list:
            if theater.room_number == theater_number: 
                for seat in theater.seat_list:
                    if seat.seat_id == seat_id:
                        target_seat = seat
                        break
        if not target_seat: 
            raise Exception("Seat not found")


        if target_seat.status != "available":  
            raise Exception("Seat already booked")

        total_price = target_seat.calculate_price() 
        if target_user.wallet < total_price:# 
            raise Exception("Insufficient funds")

        if len(target_user.booking_list) >= 5: 
            raise Exception("Daily limit exceeded")


        target_seat.status = "not available"
        target_user.wallet -= total_price 
        target_user.add_seat(target_seat)
        
       
        new_log = Transaction("B", seat_id, total_price, target_user.wallet)
        target_user.add_transaction(new_log)
class Seat(ABC):
    def __init__(self,seat_id, base_price):
        self.__seat_id = seat_id
        self.__status = "available"
        self.__base_price = base_price
    @property
    def seat_id(self):
        return self.__seat_id

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,new_status):
        self.__status = new_status

    @property
    def base_price(self):
        return self.__base_price

    @abstractmethod
    def calculate_price(self):
        pass

class NormalSeat(Seat):
    def __init__(self, seat_id, base_price):
        super().__init__(seat_id, base_price)

    def calculate_price(self):
        return self.base_price
    
class PremiumSeat(Seat):
    def __init__(self, seat_id, base_price):
        super().__init__(seat_id, base_price)

    def calculate_price(self):
        return self.base_price + 100

class SofaBed(Seat):
    def __init__(self, seat_id, base_price):
        super().__init__(seat_id, base_price)

    def calculate_price(self):
        return (self.base_price*2)+300
    
class User:
    def __init__(self, citizen, name, wallet):
        self.__citizen = citizen
        self.__name = name
        self.__wallet = wallet
        self.__booking_list = []
        self.__transactions = []

    def add_seat(self, seat):
        self.__booking_list.append(seat)

    def add_transaction(self, transaction):
        self.__transactions.append(transaction)

    @property
    def citizen(self):
        return self.__citizen
    
    @property
    def wallet(self):
        return self.__wallet

    @wallet.setter
    def wallet(self,new_wallet):
        self.__wallet = new_wallet

    @property
    def booking_list(self):          
        return self.__booking_list
    
    @property
    def transactions(self):      
        return self.__transactions
    
class Movie:
    def __init__(self,movie_name,time_show):
        self.__movie_name = movie_name
        self.__time_show = time_show

class Theater:
    def __init__(self,room_number):
        self.__seat_list = []
        self.__room_number = room_number

    def add_seat(self,seat):
        self.__seat_list.append(seat)

    @property
    def seat_list(self):
        return self.__seat_list
    @property
    def room_number(self):
        return self.__room_number


class Transaction:
    def __init__(self, t_type, seat_id, amount, balance):
        self.__t_type = t_type   
        self.__seat_id = seat_id
        self.__amount = amount
        self.__balance = balance   
    def __repr__(self): 
        return f"[{self.__t_type}]-Seat:{self.__seat_id}-{self.__amount}-{self.__balance}"  
 

if __name__ == "__main__":
    # 1. เตรียมระบบ Cinema
    major = Cinema()

    # 2. สร้างข้อมูล User (อิงตามตัวอย่าง Lab: citizen_id, name, wallet)
    user1 = User("1-1101-12345-12-0", "Harry Potter", 1000)
    user2 = User("1-1101-12345-13-0", "Ron Weasley", 100) # เงินน้อย
    major.add_user(user1)
    major.add_user(user2)

    # 3. สร้างโรงภาพยนตร์และที่นั่ง (Theater & Seats)
    room1 = Theater(101)
    # เพิ่มที่นั่งประเภทต่าง ๆ (Polymorphism)
    room1.add_seat(NormalSeat("A1", 200))   # ราคา 200
    room1.add_seat(PremiumSeat("B1", 200))  # ราคา 200 + 100 = 300
    room1.add_seat(SofaBed("C1", 200))      # ราคา (200*2) + 300 = 700
    major.add_theater(room1)

    print("--- เริ่มการทดสอบระบบ ---")

    # Test Case #1: จองที่นั่งสำเร็จ (Normal Seat)
    try:
        print("\nTest #1: Harry จอง A1 (Normal)")
        major.book_seat("1-1101-12345-12-0", 101, "A1")
        print("ผลลัพธ์: จองสำเร็จ!")
    except Exception as e:
        print(f"ผลลัพธ์ Error: {e}")

    # Test Case #2: จองที่นั่งซ้ำ (ต้องเกิด Exception)
    try:
        print("\nTest #2: จอง A1 ซ้ำอีกครั้ง")
        major.book_seat("1-1101-12345-12-0", 101, "A1")
    except Exception as e:
        print(f"ผลลัพธ์ Error (Expected): {e}")

    # Test Case #3: เงินไม่พอ (Ron จอง SofaBed 700 บาท แต่มีแค่ 100)
    try:
        print("\nTest #3: Ron จอง C1 (SofaBed) ราคา 700 แต่มีเงิน 100")
        major.book_seat("1-1101-12345-13-0", 101, "C1")
    except Exception as e:
        print(f"ผลลัพธ์ Error (Expected): {e}")

    # Test Case #4: จองจนเกินโควตาต่อวัน (Limit 5 ที่นั่ง)
    try:
        print("\nTest #4: Harry พยายามจองเพิ่มให้ครบ 6 ที่นั่ง")
        # เตรียมที่นั่งเพิ่ม
        for i in range(2, 7):
            room1.add_seat(NormalSeat(f"A{i}", 100))
        
        # จองเพิ่ม (ครั้งที่ 2, 3, 4, 5)
        major.book_seat("1-1101-12345-12-0", 101, "A2")
        major.book_seat("1-1101-12345-12-0", 101, "A3")
        major.book_seat("1-1101-12345-12-0", 101, "A4")
        major.book_seat("1-1101-12345-12-0", 101, "A5")
        
        # ครั้งที่ 6 (ต้อง Error)
        major.book_seat("1-1101-12345-12-0", 101, "A6")
    except Exception as e:
        print(f"ผลลัพธ์ Error (Expected): {e}")

    # Test Case #5: แสดงประวัติธุรกรรม (Transaction History)
    print("\n--- ตรวจสอบประวัติธุรกรรมของ Harry ---")
    for log in user1.transactions:
        print(log)
    