playlist = []

while True:
    print("======== MENU QUẢN LÝ DANH SÁCH PHÁT ========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")
    print("============================================")
    choice = input("Nhập lựa chọn của bạn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice == 1:
        print("--- THÊM BÀI HÁT ---")
        print("1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí cụ thể")
        sub_choice = input("Nhập lựa chọn: ")

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ")
            continue

        sub_choice = int(sub_choice)
        song_name = input("Nhập tên bài hát: ")

        match sub_choice:
            case 1:
                playlist.append(song_name)
                print(f"Đã thêm thành công. Tổng số bài hát hiện tại: {len(playlist)}")
            case 2:
                index = input("Nhập vị trí muốn chèn: ")
                if not index.isdigit():
                    print("Vị trí không hợp lệ")
                    continue
                index = int(index)
                if index < 1 or index > len(playlist) + 1:
                    print("Vị trí không hợp lệ")
                else:
                    playlist.insert(index - 1, song_name)
                    print("Đã thêm thành công")
                    print(f"Tổng số bài hát hiện tại: {len(playlist)}")
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

    elif choice == 2:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống")
        else:
            print("--- DANH SÁCH PHÁT ---")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")
            print(f"Tổng số bài hát: {len(playlist)}")

    elif choice == 3:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống")
            continue

        print("--- XÓA BÀI HÁT ---")
        print("1. Xóa theo tên bài hát")
        print("2. Xóa theo số thứ tự")
        sub_choice = input("Nhập lựa chọn: ")

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ")
            continue

        sub_choice = int(sub_choice)

        match sub_choice:
            case 1:
                song_name = input("Nhập tên bài hát muốn xóa: ")
                if song_name in playlist:
                    playlist.remove(song_name)
                    print("Đã xóa thành công")
                else:
                    print("Không tìm thấy bài hát trong danh sách phát")
            case 2:
                index = input("Nhập số thứ tự muốn xóa: ")
                if not index.isdigit():
                    print("Vị trí không hợp lệ")
                    continue
                index = int(index)
                if index < 1 or index > len(playlist):
                    print("Vị trí không hợp lệ")
                else:
                    removed_song = playlist.pop(index - 1)
                    print(f"Đã xóa bài hát: {removed_song}")
            case _:
                print("Lựa chọn không hợp lệ")

    elif choice == 4:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống")
            continue

        print("--- SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH ---")
        print("1. Sắp xếp danh sách phát theo bảng chữ cái")
        print("2. Hiển thị 3 bài hát đầu tiên")
        sub_choice = input("Nhập lựa chọn: ")

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ")
            continue

        sub_choice = int(sub_choice)

        match sub_choice:
            case 1:
                playlist.sort()
                print("Đã sắp xếp danh sách phát")
            case 2:
                print("3 bài hát đầu tiên:")
                for i, song in enumerate(playlist[:3], start=1):
                    print(f"{i}. {song}")
                print()
            case _:
                print("Lựa chọn không hợp lệ")

    elif choice == 5:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")