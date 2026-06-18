import logging

logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

# Hiển thị danh sách trận đấu
def display_matches(match_list):
    logging.info("User viewed the match list.")
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return
    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    for match in match_list:
        try:
            print(
                f"{match['match_id']} | "
                f"{match['team_a']} vs "
                f"{match['team_b']} | "
                f"{match['score_a']}-{match['score_b']} | "
                f"{match['status']}"
            )
        except KeyError:
            print("Dữ liệu trận đấu bị thiếu.")

# Thêm trận đấu mới
def add_match(match_list):
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    match_id = input("Nhập mã trận đấu: ").strip()
    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return
    for match in match_list:
        if match["match_id"] == match_id:
            print("Mã trận đấu đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return
    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()
    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return
    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    match_list.append(new_match)
    print("Thêm trận đấu thành công.")
    logging.info(f"Match {match_id} added successfully")

# Nhập điểm hợp lệ
def input_score(message):
    while True:
        try:
            score = int(input(message))
            if score < 0:
                print("Điểm phải >= 0")
                logging.error(f"Negative score input detected: {score}")
                continue
            return score
        except ValueError as error:
            print("Điểm phải là số nguyên.")
            logging.error(f"Invalid score input. Error: {error}")

# Cập nhật tỷ số
def update_score(match_list):
    print("\n--- CẬP NHẬT TỶ SỐ ---")
    match_id = input("Nhập mã trận đấu: ").strip()
    match_found = None
    for match in match_list:
        if match["match_id"] == match_id:
            match_found = match
            break
    if match_found is None:
        print("Không tìm thấy trận đấu.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return
    score_a = input_score("Điểm đội A: ")
    score_b = input_score("Điểm đội B: ")
    match_found["score_a"] = score_a
    match_found["score_b"] = score_b
    if score_a == 0 and score_b == 0:
        confirm = input("Xác nhận hoàn thành? (y/n): ")
        if confirm.lower() == "y":
            match_found["status"] = "Completed"
        else:
            match_found["status"] = "Pending"
    else:
        match_found["status"] = "Completed"
    print("Cập nhật thành công.")
    logging.info(f"Match {match_id} score updated successfully")

#Xác định đội thắng
def determine_winner(match):
    if match["status"] == "Pending":
        return "Not Started"
    if match["score_a"] > match["score_b"]:
        return match["team_a"]
    if match["score_b"] > match["score_a"]:
        return match["team_b"]
    return "Draw"
# In báo cáo
def generate_report(match_list):
    print("\n--- BÁO CÁO ---")
    total = 0
    for match in match_list:
        if match["status"] == "Completed":
            winner = determine_winner(match)
            print(f"{match['match_id']} | Kết quả: {winner}")
            total += 1
    print(f"Tổng số trận hoàn thành: {total}")
    logging.info("User generated tournament report.")
while True:

    print("\n===== MENU =====")
    print("1. Hiển thị trận đấu")
    print("2. Thêm trận đấu")
    print("3. Cập nhật tỷ số")
    print("4. Báo cáo")
    print("5. Thoát")

    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        display_matches(matches)
    elif choice == "2":
        add_match(matches)
    elif choice == "3":
        update_score(matches)
    elif choice == "4":
        generate_report(matches)
    elif choice == "5":
        logging.info("Tournament system closed.")
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
        logging.warning("Invalid menu choice selected")