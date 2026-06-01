# # break dừng vòng lặp ngay lập tức
# # continue dừng vòng lặp hiện tại

# # cách dùng break ,continue
# state = 1
# cost = 0
# while True:
#     state_name = f"State{state}"
#     print(state_name)
#     if state % 2 == 0:
#         state += 1
#         continue
#     cost += 100_00
#     if state == 5:
#         break
#     state += 1
# print(f"state = {cost}")

# in bang cu chuong tu 2 den 9
# print("bang cuu chuong")
# for i in range(2,10):
#     print(f"bang {i}")
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")

col = int(input("nhap chieu rong: "))
row = int(input("nhap chieu dai: "))
for i in range(row):
    for j in range(col):
        if j == 0 or j == col - 1 or i == 0 or i == row - 1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()