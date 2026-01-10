def __init__(self, account_no, user, amount, term_months=12):
        
        """TODO:
        1. เรียก super().__init__()
        2. เก็บ term_months
        3. เก็บ start_date = datetime.now()
        4. คำนวณ maturity_date = start_date + timedelta(days=term_months*30)
        """
        super().__init__(account_no,user,amount)
        self.__term_months = term_months
        self.__start_date = datetime.now()
        self.__maturity_date = self.__start_date + timedelta(days=term_months * 30)
    @property
    def term_months(self):
        return self.__term_months
    @property
    def maturity_date(self):
        return self.__maturity_date
    def get_account_type(self):
        """TODO: Return f"Fixed Account ({self.term_months} months)" """
        return f"Fixed Account ({self.term_months} months)"

        
    
    def calculate_interest(self, early_withdrawal=False):
        """คำนวณดอกเบี้ย 2.5% (หรือ 1.25% ถ้าถอนก่อนกำหนด)
        
        TODO:
        1. เริ่มจาก rate = INTEREST_RATE
        2. ถ้า early_withdrawal → rate *= EARLY_WITHDRAWAL_PENALTY
        3. คำนวณ interest = amount * rate * (term_months / 12)
        4. เพิ่ม interest เข้า __amount
        5. บันทึก transaction
        6. แสดงข้อความและ return interest
        
        """
        rate = FixedAccount.INTEREST_RATE

        if (early_withdrawal):
            rate *= FixedAccount.EARLY_WITHDRAWAL_PENALTY

        interest = self.amount * rate * (self.__term_months / 12)

        self._Account__amount += interest
        self._create_transaction("I",'SYSTEM', 'AUTO', interest, self.amount)
        print(f"Interest added: {interest:.2f}")
        return interest
            
    
    def _check_withdraw_limit(self, amount):
        """ฝากประจำสามารถถอนได้ แต่แสดง warning
        
        TODO:
        - ถ้า datetime.now() < maturity_date
        - แสดง warning message
        """
        if datetime.now() < self.__maturity_date:
            Warning("Beware!!")