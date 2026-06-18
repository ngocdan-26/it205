import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500,
        "status": "Active"
    }
]

def calculate_actual_pay(player):
    if player["status"] == "Active":
        return player["salary"]
    return player["salary"] * 0.5

def display_roster(roster_list):
    logging.info("Coach viewed the team roster.")
    if len(roster_list) == 0:
        print("Đội hình hiện đang trống.")
        return
    print("\n--- ĐỘI HÌNH ---")
    for player in roster_list:
        try:
            status = player.get("status","Unknown")
            name = player["name"]
            if status == "Benched":
                name += " [DỰ BỊ]"

            print(player["player_id"],name,player["role"],player["salary"],status)
        except KeyError:
            print("Dữ liệu bị thiếu.")

def sign_player(roster_list):
    print("\n--- CHIÊU MỘ ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    for player in roster_list:
        if player["player_id"] == player_id:
            print("Mã tuyển thủ đã tồn tại.")
            logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
            return
    name = input("Tên: ").title()
    role = input("Vị trí: ").title()
    while True:
        try:
            salary = float(input("Lương: "))
            if salary <= 0:
                print("Lương phải lớn hơn 0.")
                continue
            break
        except ValueError:
            print("Lương phải là số.")
            logging.warning("Failed to sign player - Invalid salary input")
    roster_list.append(
        {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": "Active"
        }
    )
    logging.info(
        f"Signed new player {name} with salary {salary}")
    print("Thêm thành công.")

def generate_payroll_report(roster_list):
    total = 0
    try:
        for player in roster_list:
            total += calculate_actual_pay(player)
        print(f"Tổng quỹ lương: {total}")
        logging.info(f"Generated monthly payroll report. Total: {total}")
    except KeyError as error:
        print("Lỗi dữ liệu.")
        logging.error(f"Missing key: {error}")

while True:
    print("\n===== MENU =====")
    print("1. Xem đội hình")
    print("2. Chiêu mộ")
    print("3. Báo cáo lương")
    print("4. Thoát")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        display_roster(roster)
    elif choice == "2":
        sign_player(roster)
    elif choice == "3":
        generate_payroll_report(roster)
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")