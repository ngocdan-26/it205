from abc import ABC, abstractmethod


class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._BaseAccount__balance = balance

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, name):
        self._owner_name = " ".join(name.strip().upper().split())

    @property
    def balance(self):
        return self._BaseAccount__balance

    def _update_balance(self, value):
        self._BaseAccount__balance = value

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name


class SavingsAccount(BaseAccount):
    def __init__(self, account_number, owner_name, interest_rate):
        super().__init__(account_number, owner_name)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._update_balance(self.balance + amount)

    def withdraw(self, amount):
        fee = amount * 0.02
        total = amount + fee

        if total > self.balance:
            print("Không đủ số dư!")
            return

        self._update_balance(self.balance - total)
        print("Rút tiền thành công!")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Lãi: {interest:,.0f} VND")


class CreditAccount(BaseAccount):
    def __init__(self, account_number, owner_name, credit_limit):
        super().__init__(account_number, owner_name)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        self._update_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount < -self.credit_limit:
            print("Vượt hạn mức tín dụng!")
            return

        self._update_balance(self.balance - amount)
        print("Rút tiền thành công!")


class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5000000:
            reward = amount * 0.01
            self.deposit(reward)
            print(f"Hoàn tiền: {reward:,.0f} VND")


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass


class VNPayGateway:
    def execute_pay(self, account, amount):
        account.withdraw(amount)
        print("Thanh toán VNPay thành công!")


class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        account.withdraw(amount)
        print("Thanh toán Viettel Money thành công!")


def process_payment(gateway, account, amount):
    try:
        gateway.execute_pay(account, amount)
    except AttributeError:
        print("Cổng thanh toán không hợp lệ!")


accounts = []
current_account = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK =====")
    print("1. Mở tài khoản")
    print("2. Xem thông tin")
    print("3. Nạp / Rút")
    print("4. Tính lãi")
    print("5. So sánh & Gộp")
    print("6. Thanh toán")
    print("7. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        print("1. Savings")
        print("2. Credit")
        print("3. Hybrid")

        acc_type = input("Loại: ")

        acc_num = input("Số tài khoản: ")

        if not BaseAccount.validate_account_number(acc_num):
            print("Số tài khoản không hợp lệ!")
            continue

        name = input("Tên: ")

        if acc_type == "1":
            rate = float(input("Lãi suất: "))
            acc = SavingsAccount(acc_num, name, rate)

        elif acc_type == "2":
            limit = float(input("Hạn mức: "))
            acc = CreditAccount(acc_num, name, limit)

        elif acc_type == "3":
            rate = float(input("Lãi suất: "))
            acc = HybridAccount(acc_num, name, rate)

        else:
            print("Không hợp lệ!")
            continue

        accounts.append(acc)
        current_account = acc
        print("Mở tài khoản thành công!")

    elif choice == "2":
        if current_account is None:
            print("Chưa có tài khoản!")
            continue

        print("Loại:", type(current_account).__name__)
        print("Ngân hàng:", current_account.bank_name)
        print("Số TK:", current_account.account_number)
        print("Tên:", current_account.owner_name)
        print(f"Số dư: {current_account.balance:,.0f} VND")

        print("MRO:")
        for cls in type(current_account).mro():
            print(cls.__name__)

    elif choice == "3":
        if current_account is None:
            print("Chưa có tài khoản!")
            continue

        print("1. Nạp")
        print("2. Rút")

        t = input("Chọn: ")
        amount = float(input("Số tiền: "))

        if t == "1":
            current_account.deposit(amount)

            if isinstance(current_account, HybridAccount):
                current_account.cashback_reward(amount)

            print("Nạp tiền thành công!")

        elif t == "2":
            current_account.withdraw(amount)

        print(f"Số dư: {current_account.balance:,.0f} VND")

    elif choice == "4":
        if current_account is None:
            print("Chưa có tài khoản!")
            continue

        if isinstance(current_account, (SavingsAccount, HybridAccount)):
            current_account.apply_interest()
            print(f"Số dư: {current_account.balance:,.0f} VND")
        else:
            print("Không hỗ trợ tính lãi!")

    elif choice == "5":
        if len(accounts) < 2:
            print("Cần ít nhất 2 tài khoản!")
            continue

        for i, acc in enumerate(accounts):
            print(i, acc.owner_name)

        try:
            idx = int(input("Chọn tài khoản: "))
            other = accounts[idx]

            if current_account < other:
                print("Tài khoản hiện tại nhỏ hơn")
            else:
                print("Tài khoản hiện tại lớn hơn hoặc bằng")

            print(f"Tổng số dư: {current_account + other:,.0f} VND")

        except:
            print("Lỗi so sánh!")

    elif choice == "6":
        if current_account is None:
            print("Chưa có tài khoản!")
            continue

        print("1. VNPay")
        print("2. Viettel Money")

        g = input("Chọn: ")
        amount = float(input("Số tiền: "))

        if g == "1":
            gateway = VNPayGateway()
        else:
            gateway = ViettelMoneyGateway()

        process_payment(gateway, current_account, amount)

        print(f"Số dư: {current_account.balance:,.0f} VND")

    elif choice == "7":
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ!")