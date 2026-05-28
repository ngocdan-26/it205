# vòng lặp for
# for in list/string/range()/tuple/dict
    # block code 
# range(): tạo ra môitj dãy số nguyên. lưu ý: range(1,5) => 1,2,3,4

# in ra dãy số từ 1 đến 10
# for index in range(1,11):
#     print(index)

# # dùng với tham số là stop :nếu không sd start,thì mặc định là 0
# for value in range(11):
#     print(value)

# #in ra số chẵn từ 1 đến 10
# for value in range(0,11,2):
#     print(value)

# # tinh tong cac so tu 1 den 10
# total = 0
# for value in range(1,11):
#     total += value
# print(total)

# print("---- vòng lặp while ----")
# # while condition:
    #block code
    # tăng giá trị của biến khởi tạo làm đk

#in ra các số từ 1 đến 10 bằng while 
# inittial_value = 1
# while inittial_value <= 10:
#     print(inittial_value)
#     inittial_value += 1

# password = 123456
# isSuccese = False
# i = 0
# while not isSuccese and i < 3:
#     password_input = int(input("nhap MK: "))
#     if password_input == password :
#         print("dang nhap thanh cong")
#         isSuccese = True
#     else:
#         print("dang nhap that bai")
#         i += 1
    
# in ra bng cuu chuong
for first_value in range(2,10):
    print(f"bang cuu chuong {first_value}")
    for second_value in range(1,11):
        print(f"{first_value} x {second_value} = {first_value * second_value}")
step = 1
distance = 0
while step <= 4:
    distance = distance + step * 2
    step = step + 1
print(distance)