if not isinstance(channel,Channel):
            raise PermissionError("Not a right session")
        if isinstance(channel,(ATM_machine,EDC_machine)):
            if not channel.current_card:
                raise PermissionError("No Card")
            if not channel.has_sufficient_cash(amount) :
                raise ValueError("not enough cash")
            if channel.current_card.get_card_type() == "Premium Card":
                if amount + self.__daily_withdrawn > PremiumCard.DAILY_LIMIT:
                    raise ValueError("Over daily limit")
            if amount > Bank.WITHDRAW_LIMIT:
                raise ValueError("More than daily limit")
            if channel.current_card.get_card_type() == "ATM card":
                if self.__amount < ATM_Card.ANNUAL_FEE:
                    raise ValueError("Not enough money")
                if self.__amount - amount - Bank.ATM_FEE > ATM_Card.ANNUAL_FEE:
                    raise ValueError("Not enough money")
        if amount <= 0:
            raise ValueError("money have not more 0")
        self._check_withdraw_limit(amount)
        if self.__amount < amount + Bank.ATM_FEE:
            raise ValueError("Not enough money")
        self.__amount -= amount
        if isinstance(channel,(ATM_machine,EDC_machine)):
            self.__daily_withdrawn += amount
            channel.dispense_cash(amount)