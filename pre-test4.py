from abc import ABC,abstractmethod

class FoodOrder(ABC):
    def __init__(self,order_id,food_name,base_price):
        self.__order_id = order_id
        self.__food_name = food_name
        self.__base_price = base_price
    
    @property
    def base_price(self):
        return self.__base_price
    
    @property
    def food_name(self):
        return self.__food_name
    
    @property
    def order_id(self):
        return self.__order_id
    
    @abstractmethod
    def calculate_total(self):
        pass

class DineInOrder(FoodOrder):
    def __init__(self,order_id,food_name,base_price):
        super().__init__(order_id,food_name,base_price)

    def calculate_total(self):
        return self.base_price + (0.1*self.base_price)

class DeliveryOrder(FoodOrder):
    def __init__(self,order_id,food_name,base_price):
        super().__init__(order_id,food_name,base_price)

    def calculate_total(self):
        return self.base_price + 40

class PickupOrder(FoodOrder):
    def __init__(self,order_id,food_name,base_price):
        super().__init__(order_id,food_name,base_price)

    def calculate_total(self):
        return self.base_price - (0.05*self.base_price)

class Customer:
    def __init__(self,name,wallet):
        self.__name = name
        self.__wallet = wallet
        self.__order_history = []
        self.__transaction = []

    @property
    def name(self):
        return self.__name
    
    @property
    def order_history(self):
        return self.__order_history
    
    @property
    def transaction(self):
        return self.__transaction
    
    @property
    def wallet(self):
        return self.__wallet
    
    @wallet.setter
    def wallet(self,new_wallet):
        self.__wallet = new_wallet

    def add_order_history(self,order_history):
        self.__order_history.append(order_history)
    
    def add_transaction(self,transaction):
        self.__transaction.append(transaction)

class DeliveryApp:
    def __init__(self):
        self.__customer_list = []
        self.__food_order_list = []
    
    def place_order(self, customer_name, order_object):
        target_user = None
        for user in self.__customer_list:
            if user.name == customer_name:
                target_user = user
                break

        if not target_user:
            raise Exception("Customer not found")

        total_price = order_object.calculate_total() 
        if target_user.wallet < total_price:
            raise Exception("Insufficient Balance")
        
        if len(target_user.order_history) >= 3:
            raise Exception("Order Limit Exceeded")
        
        target_user.wallet -= total_price
        target_user.add_order_history(order_object)

        new_log = Transaction(
            order_object.__class__.__name__, 
            order_object.food_name, 
            total_price, 
            target_user.wallet
        )
        target_user.add_transaction(new_log)
class Transaction:
    def __init__(self, t_type, food_name, amount, balance):
        self.__t_type = t_type       # ประเภทรายการ: "D" (Dine-In), "DL" (Delivery), "P" (Pickup)
        self.__food_name = food_name # ชื่ออาหารที่สั่ง
        self.__amount = amount       # ราคาสุทธิที่จ่ายจริง (ที่คำนวณผ่าน Polymorphism แล้ว)
        self.__balance = balance     # ยอดเงินคงเหลือใน Wallet หลังจากตัดเงินแล้ว
        # (Option) self.__timestamp = datetime.now() # ถ้าอยากเก็บเวลาด้วย

    def __repr__(self):
        # ออกแบบรูปแบบการพิมพ์ให้เหมือน Lab #4
        # รูปแบบ: [Type]-Food:[Name]-Pay:[Amount]-Balance:[Balance]
        return f"[{self.__t_type}]-Food:{self.__food_name}-Pay:{self.__amount:.2f}-Bal:{self.__balance:.2f}"
    

if __name__ == "__main__":
    # 1. สร้างแอปและเพิ่มลูกค้า
    app = DeliveryApp()
    
    # เพิ่มลูกค้าเข้าระบบ (ต้องเพิ่ม method add_customer ใน DeliveryApp ด้วยนะ)
    c1 = Customer("Somchai", 500)
    c2 = Customer("Somsak", 50) # เงินน้อย
    
    # สมมติว่ามี method add_customer
    app._DeliveryApp__customer_list.append(c1)
    app._DeliveryApp__customer_list.append(c2)

    print("--- เริ่มการทดสอบ Food Delivery ---")

    # Test Case 1: สั่ง DineIn (ราคา + 10%)
    # ส้มตำ 100 บาท + 10% = 110 บาท
    try:
        order1 = DineInOrder("ORD001", "Somtum", 100)
        print("\nTest 1: Somchai สั่งส้มตำ (Dine-In 110.-)")
        app.place_order("Somchai", order1)
        print(f"ผลลัพธ์: สำเร็จ! เงินเหลือ {c1.wallet}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Case 2: สั่ง Delivery (ราคา + 40 บาท)
    # พิซซ่า 300 บาท + 40 = 340 บาท
    try:
        order2 = DeliveryOrder("ORD002", "Pizza", 300)
        print("\nTest 2: Somchai สั่งพิซซ่า (Delivery 340.-)")
        app.place_order("Somchai", order2)
        print(f"ผลลัพธ์: สำเร็จ! เงินเหลือ {c1.wallet}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Case 3: เงินไม่พอ (Insufficent Balance)
    try:
        order3 = PickupOrder("ORD003", "Burger", 100)
        print("\nTest 3: Somsak (เงินมี 50) สั่งเบอร์เกอร์")
        app.place_order("Somsak", order3)
    except Exception as e:
        print(f"ผลลัพธ์ Error (Expected): {e}")

    # Test Case 4: สั่งเกินโควตา (Limit 3 ออเดอร์)
    try:
        print("\nTest 4: Somchai พยายามสั่งออเดอร์ที่ 3 และ 4")
        # ออเดอร์ที่ 3 (สำเร็จ)
        app.place_order("Somchai", PickupOrder("ORD004", "Water", 20))
        # ออเดอร์ที่ 4 (ต้อง Error)
        app.place_order("Somchai", PickupOrder("ORD005", "Coke", 20))
    except Exception as e:
        print(f"ผลลัพธ์ Error (Expected): {e}")

    # Test Case 5: ตรวจสอบประวัติ Transaction
    print("\n--- ประวัติธุรกรรมของ Somchai ---")
    for t in c1.transaction:
        print(t)