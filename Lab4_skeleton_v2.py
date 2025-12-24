from typing import List, Union, Optional

##################################################################################
# Instruction for Students:
# 1. จงเขียน Class Diagram เพื่อออกแบบ Class ต่างๆ ให้รองรับการทำงานของ Code ส่วนล่าง
# 2. จงเขียน Class Definition (Bank, User, Account, ATM_Card, ATM_machine, Transaction)
#    เพื่อให้สามารถรัน Function run_test() ได้โดยไม่เกิด Error
# 3. ห้ามแก้ไข Code ในส่วนของ create_bank_system() และ run_test() โดยเด็ดขาด
# 4. ต้องมีการ Validate ข้อมูลตามเงื่อนไขที่กำหนดในเอกสาร Lab (เช่น เงินไม่พอ, PIN ผิด)
#    และทำการ Raise Exception เมื่อเกิดข้อผิดพลาด
##################################################################################

# --- พื้นที่สำหรับเขียน Class ของนักศึกษา (เขียนต่อจากตรงนี้) ---

class Bank:
    def __init__(self,name):
        self.__name_bank = name
        self.__users = []
        self.__Atm_machine = []
    def add_user(self,user_instance):
        self.__users.append(user_instance)
    def add_atm_machine(self,atm_machine) :
        self.__Atm_machine.append(atm_machine)
    def get_atm_by_id(self,id):
        for atm in self.__Atm_machine :
            if atm.atm_id == id :
                return atm
    def search_account_from_atm(self,atm_card_id):
        for user in self.__users:
            for account in user.Account:
                if account.atm_card and account.atm_card.atmID == atm_card_id:
                    return account
class User:
    def __init__(self,citizen_id,name):
        self.__Citizen_ID = citizen_id
        self.__Username = name
        self.__Account = []
    def add_account(self,user_account):
        if isinstance(user_account,Account):
            self.__Account.append(user_account)
    @property
    def Account(self) :
        return self.__Account
    @property
    def name(self):
        return self.__Username
class Account:
    def __init__(self,id,user_instance,amount):
        self.__Account_no = id
        self.__User_Instance = user_instance
        self.__Balance = amount
        self.__atm_card = None
        self.__transection = []
        self.__limit = 0
    def add_atm_card(self,atm_card):
        self.__atm_card= atm_card
    @property
    def user(self):
        return self.__User_Instance
    
    @property
    def atm_card(self):
        return self.__atm_card
    @property
    def amount(self):
        return self.__Balance

    @property
    def account_no(self):
        return self.__Account_no
    def deposit(self,atm_machine,cash):
        if atm_machine.cardIn and atm_machine.cardIn != self.__atm_card:
            raise ValueError("Not match card")
        if cash >0:
            self.__Balance += cash
            atm_machine.remain_cash += cash
            self.__transection.append(Transaction("D",atm_machine.atm_id,cash,self.__Balance))
        else:
            raise ValueError()
    def withdraw(self,atm_machine,cash):
        if atm_machine.cardIn and atm_machine.cardIn != self.__atm_card:
            raise ValueError("Not match card")
        if cash >0 and cash <= self.__Balance and self.__limit+cash <= Rule.limit and cash<=atm_machine.remain_cash:
            self.__Balance -= cash
            atm_machine.remain_cash -= cash
            self.__limit += cash
            self.__transection.append(Transaction("W",atm_machine.atm_id,cash,self.__Balance))
        else:
            raise ValueError()
    def tranfer_deposit(self,atm,money,one_self):
        self.__Balance += money
        transection =Transaction("TD",atm.atm_id,money,self.__Balance)
        transection.add_target(one_self)
        self.__transection.append(transection)
    def transfer(self, atm, money, second_account):
        if atm.cardIn and atm.cardIn != self.__atm_card:
            raise ValueError("Not match card")

        if money <= 0:
            raise ValueError("Invalid amount")

        if money > self.__Balance:
            raise ValueError("Insufficient balance")

        if self.__limit + money > Rule.limit:
            raise ValueError("Exceed daily limit")

        if money > atm.remain_cash:
            raise ValueError("ATM insufficient cash")

        self.__Balance -= money
        atm.remain_cash -= money
        self.__limit += money

        second_account.tranfer_deposit(atm, money, self)

        transaction = Transaction("TW", atm.atm_id, money, self.__Balance)
        transaction.add_target(second_account)
        self.__transection.append(transaction)

    def print_transactions(self):
        for transaction in self.__transection:
            if transaction.target != None:
                print(f"{transaction.Type}-ATM:[{transaction.atm_id}]-{transaction.amount}-{transaction.balance}-{transaction.target.user.name}")
            else :
                print(f"{transaction.Type}-ATM:[{transaction.atm_id}]-{transaction.amount}-{transaction.balance}")
class ATM_Card:
    def __init__(self,id,account_no,password):
        self.__atmcard_id = id
        self.__account_no = account_no
        self.__Password = password
    @property
    def atmID(self):
        return self.__atmcard_id
    @property
    def password_card(self):
        return self.__Password

class ATM_machine:
    def __init__(self,id,cash):
        self.__atm_id = id
        self.__remain_cash_atm = cash
        self.__card_in = None
    def insert_card(self,atm_card, password):
        if atm_card.password_card != password:
            return False
        self.__card_in = atm_card
        return True
    @property
    def cardIn(self):
        return self.__card_in
    @property
    def remain_cash(self):
        return self.__remain_cash_atm
    @property
    def atm_id(self):
        return self.__atm_id
    @remain_cash.setter
    def remain_cash(self, value):
        self.__remain_cash_atm = value
class Transaction:
    def __init__(self,type,atm_id,amount,balance):
        self.__Type = type
        self.__atm_id = atm_id
        self.__amount = amount
        self.__balance = balance
        self.__target = None
    def add_target(self,target) :
        self.__target = target
    @property
    def Type(self):
        return self.__Type
    @property
    def atm_id(self):
        return self.__atm_id
    @property
    def amount(self):
        return self.__amount
    @property
    def balance(self):
        return self.__balance
    @property
    def target(self):
        return self.__target
class Rule :
    fee = 150
    limit = 40000


##################################################################################
# Test Case & Setup : ห้ามแก้ไข Code ส่วนนี้
# ใช้สำหรับตรวจสอบว่า Class ที่ออกแบบมาถูกต้องตาม Requirement หรือไม่
##################################################################################

def create_bank_system() -> Bank:
    print("--- Setting up Bank System ---")
    
    # 1. กำหนดชื่อธนาคาร
    scb = Bank("SCB")
    
    # 2. สร้าง User, Account, ATM_Card
    # Data format: CitizenID: [Name, AccountNo, ATM Card No, Balance]
    user_data = {
       '1-1101-12345-12-0': ['Harry Potter', '1000000001', '12345', 20000],
       '1-1101-12345-13-0': ['Hermione Jean Granger', '1000000002', '12346', 1000]
    }
    
    for citizen_id, detail in user_data.items():
        name, account_no, atm_no, amount = detail
        
        user_instance = User(citizen_id, name)
        user_account = Account(account_no, user_instance, amount)
        atm_card = ATM_Card(atm_no, account_no, '1234')
        
        user_account.add_atm_card(atm_card)
        user_instance.add_account(user_account)
        scb.add_user(user_instance)

    # 3. สร้างตู้ ATM
    scb.add_atm_machine(ATM_machine('1001', 1000000))
    scb.add_atm_machine(ATM_machine('1002', 200000))

    return scb

def run_test():
    scb = create_bank_system()
    
    atm_machine1 = scb.get_atm_by_id('1001')
    atm_machine2 = scb.get_atm_by_id('1002')
    
    harry_account = scb.search_account_from_atm('12345')
    hermione_account = scb.search_account_from_atm('12346')
    
    # ตรวจสอบว่าหา Account เจอหรือไม่
    if not harry_account or not hermione_account:
        print("Error: Could not find accounts. Check your search_account_from_atm method.")
        return

    harry_card = harry_account.atm_card
    
    print("\n--- Test Case #1 : Insert Card (Harry) ---")
    print(f"Harry's Account No : {harry_account.account_no}")

    if atm_machine1.insert_card(harry_card, "1234"):
        print("Success: ATM accepted valid card and PIN")
    else:
        print("Error: ATM rejected valid card")

    print("\n--- Test Case #2 : Deposit 1000 to Hermione ---")
    print(f"Before: {hermione_account.amount}")

    try:
        hermione_account.deposit(atm_machine2, 1000)
        print(f"After: {hermione_account.amount}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Test Case #3 : Deposit -1 (Expect Error) ---")
    try:
        hermione_account.deposit(atm_machine2, -1)
        print("Error: Failed to catch negative deposit")
    except ValueError as e: # คาดหวัง ValueError หรือ Exception ที่เหมาะสม
        print(f"Pass: System correctly raised error -> {e}")
    except Exception as e:
        print(f"Pass: System raised error -> {e}")

    print("\n--- Test Case #4 : Withdraw 500 from Hermione ---")
    print(f"Before: {hermione_account.amount}")

    try:
        hermione_account.withdraw(atm_machine2, 500)
        print(f"After: {hermione_account.amount}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Test Case #5 : Withdraw Excess Balance (Expect Error) ---")
    try:
        hermione_account.withdraw(atm_machine2, 30000)
        print("Error: Failed to catch overdraft")
    except Exception as e:
        print(f"Pass: System correctly raised error -> {e}")

    print("\n--- Test Case #6 : Transfer 10000 from Harry to Hermione ---")
    print(f"Harry Before: {harry_account.amount}")
    print(f"Hermione Before: {hermione_account.amount}")

    try:
        harry_account.transfer(atm_machine2, 10000, hermione_account)
        print(f"Harry After: {harry_account.amount}")
        print(f"Hermione After: {hermione_account.amount}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Test Case #7 : Transaction History ---")

    print("Harry Transactions:")
    harry_account.print_transactions()
    print("Hermione Transactions:")
    hermione_account.print_transactions()

    print("\n--- Test Case #8 : Wrong PIN (Expect Error) ---")
    if not atm_machine1.insert_card(harry_card, "9999"):
        print("Pass: ATM correctly rejected wrong PIN")
    else:
        print("Error: ATM accepted wrong PIN")
        
    print("\n--- Test Case #9 : Exceed Daily Limit (Expect Error) ---")
    # Harry ถอนไปแล้ว 0, โอน 10000 (นับรวม) = ใช้ไป 10000
    # Limit = 40000. ลองถอนอีก 35000 (รวมเป็น 45000) ต้อง Error
    try:
        print("Attempting to withdraw 35,000 (Total daily: 45,000)...")
        harry_account.withdraw(atm_machine1, 35000)
        print("Error: Daily limit exceeded but not caught")
    except Exception as e:
        print(f"Pass: System correctly raised error -> {e}")

    print("\n--- Test Case #10 : ATM Insufficient Cash (Expect Error) ---")
 
    poor_atm = ATM_machine('9999', 100) 
    scb.add_atm_machine(poor_atm)
    try:
        print("Attempting to withdraw 500 from ATM with 100 THB...")
        harry_account.withdraw(poor_atm, 500)
        print("Error: ATM insufficient cash but not caught")
    except Exception as e:
        print(f"Pass: System correctly raised error -> {e}")

if __name__ == "__main__":
    run_test()