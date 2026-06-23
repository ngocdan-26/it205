from datetime import datetime
from colorama import Fore, Style
from utils.score_utils import (calculate_average,classify_student)

def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records,start=1):
        average = calculate_average(student["scores"])
        level = classify_student(average )
        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average:.2f} - {level}"
        )
    print("---------------------------------")

def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total_students = len(records)
    passed_students = 0
    for student in records:
        average = calculate_average(student["scores"])
        if average >= 5:
            passed_students += 1
    failed_students = (total_students - passed_students)
    report_time = datetime.now()
    with open("learning_report.txt", "w",encoding="utf-8") as file:
        file.write("BÁO CÁO HỌC TẬP")
        file.write(f"Thời gian tạo: {report_time}")
        file.write(f"Tổng số sinh viên: {total_students}")
        file.write(f"Số sinh viên đạt yêu cầu: {passed_students}")
        file.write(f"Số sinh viên cần cải thiện: {failed_students}")
    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed_students}")
    print(f"Số sinh viên cần cải thiện: {failed_students}")
    print(Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt" +Style.RESET_ALL)