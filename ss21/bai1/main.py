import logging

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class Wallet:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            logging.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError

        self.balance += amount

        logging.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {self.balance}"
        )

    def transfer(self, phone, amount):
        if amount <= 0:
            logging.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError

        if amount > self.balance:
            logging.error(
                f"InsufficientBalanceError: Attempted to transfer "
                f"{amount} VND with balance {self.balance} VND."
            )
            raise InsufficientBalanceError

        if amount >= 10000000:
            logging.warning(
                f"High value transaction detected: "
                f"{amount} VND to {phone}"
            )

        self.balance -= amount

        logging.info(
            f"Transfer successful: -{amount} VND to {phone}. "
            f"Current Balance: {self.balance}"
        )


wallet = Wallet()

while True:
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        print("\n--- NẠP TIỀN VÀO VÍ ---")

        try:
            amount = int(input("Nhập số tiền cần nạp: "))

            wallet.deposit(amount)

            print(f"Nạp tiền thành công: +{amount:,} VND")
            print(f"Số dư hiện tại: {wallet.balance:,} VND")

        except ValueError:
            logging.error(
                "ValueError: Invalid numeric input for deposit."
            )
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")

        except InvalidAmountError:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")

    elif choice == "2":
        print("\n--- CHUYỂN TIỀN ---")

        phone = input("Nhập số điện thoại người nhận: ")

        if not (phone.isdigit() and len(phone) == 10):
            print("Số điện thoại không hợp lệ.")
            continue

        try:
            amount = int(input("Nhập số tiền cần chuyển: "))

            wallet.transfer(phone, amount)

            print(f"Chuyển tiền thành công tới {phone}")
            print(f"Số tiền đã chuyển: {amount:,} VND")
            print(f"Số dư còn lại: {wallet.balance:,} VND")

        except ValueError:
            logging.error(
                "ValueError: Invalid numeric input for transfer."
            )
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")

        except InvalidAmountError:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")

        except InsufficientBalanceError:
            print("Giao dịch thất bại: Số dư của bạn không đủ.")
            print(f"Số dư hiện tại: {wallet.balance:,} VND")

    elif choice == "3":
        print("\n--- SỐ DƯ VÍ MOMO ---")
        print(f"Số dư hiện tại: {wallet.balance:,} VND")

        logging.info(
            f"Balance checked. Current Balance: {wallet.balance}"
        )

    elif choice == "4":
        logging.info("System shutdown")
        print("Cảm ơn bạn đã sử dụng dịch vụ.")
        break

    else:
        print("Lựa chọn không hợp lệ.")