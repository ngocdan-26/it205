from datetime import datetime

def parse_and_inspect_date(date_str):
    try:
        upload_date = datetime.strptime(date_str, "%Y-%m-%d")
        return upload_date
    except ValueError:
        print(f"[WARNING] Định dạng ngày upload '{date_str}' không tồn tại")
        return None