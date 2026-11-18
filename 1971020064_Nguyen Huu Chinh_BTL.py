import os
DATA_FILE = "employees.txt"
SO_NGAY_CONG_CHUAN = 26


# ============ TIỆN ÍCH ============
def tinh_luong_thuc_nhan(luong_co_ban, so_ngay_cong, phu_cap):
    """Lương thực nhận = (Lương CB / 26) * Số ngày công + Phụ cấp"""
    return (luong_co_ban / SO_NGAY_CONG_CHUAN) * so_ngay_cong + phu_cap


def nhap_chuoi_bat_buoc(prompt):
    """Nhập chuỗi, không cho phép rỗng"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  ⚠ Thông tin bắt buộc không được bỏ trống!")


def nhap_so_thuc_duong(prompt):
    """Nhập số thực >= 0"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  ⚠ Giá trị không được âm!")
                continue
            return value
        except ValueError:
            print("  ⚠ Vui lòng nhập số hợp lệ!")


def nhap_so_ngay_cong(prompt):
    """Nhập số ngày công trong khoảng 0..31"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 31:
                print("  ⚠ Số ngày công phải nằm trong khoảng 0-31!")
                continue
            return value
        except ValueError:
            print("  ⚠ Vui lòng nhập số hợp lệ!")


def kiem_tra_ma_trung(danh_sach, ma):
    return any(nv["ma_nv"].lower() == ma.lower() for nv in danh_sach)


def tim_theo_ma(danh_sach, ma):
    for nv in danh_sach:
        if nv["ma_nv"].lower() == ma.lower():
            return nv
    return None


def format_tien(so_tien):
    return f"{so_tien:,.0f} VNĐ"


# ============ 1. THÊM NHÂN VIÊN ============
def them_nhan_vien(danh_sach):
    print("\n--- THÊM NHÂN VIÊN ---")
    ma_nv = nhap_chuoi_bat_buoc("  Mã nhân viên: ")
    if kiem_tra_ma_trung(danh_sach, ma_nv):
        print("  ⚠ Lỗi: Mã nhân viên đã tồn tại!")
        return

    ho_ten    = nhap_chuoi_bat_buoc("  Họ và tên: ")
    ngay_sinh = nhap_chuoi_bat_buoc("  Ngày sinh : ")
    gioi_tinh = nhap_chuoi_bat_buoc("  Giới tính: ")
    phong_ban = nhap_chuoi_bat_buoc("  Phòng ban: ")
    chuc_vu   = nhap_chuoi_bat_buoc("  Chức vụ: ")
    luong_cb  = nhap_so_thuc_duong("  Lương cơ bản (VNĐ): ")
    so_ngay   = nhap_so_ngay_cong("  Số ngày công (0-31): ")
    phu_cap   = nhap_so_thuc_duong("  Phụ cấp (VNĐ): ")

    luong_tn = tinh_luong_thuc_nhan(luong_cb, so_ngay, phu_cap)

    danh_sach.append({
        "ma_nv": ma_nv,
        "ho_ten": ho_ten,
        "ngay_sinh": ngay_sinh,
        "gioi_tinh": gioi_tinh,
        "phong_ban": phong_ban,
        "chuc_vu": chuc_vu,
        "luong_co_ban": luong_cb,
        "so_ngay_cong": so_ngay,
        "phu_cap": phu_cap,
        "luong_thuc_nhan": luong_tn
    })
    print(f"  Thêm thành công! Lương thực nhận: {format_tien(luong_tn)}")


# ============ 2. HIỂN THỊ DANH SÁCH ============
def hien_thi_danh_sach(danh_sach):
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    if not danh_sach:
        print("  (Danh sách trống)")
        return
    print(f"{'Mã NV':<8}{'Họ và tên':<22}{'Phòng ban':<15}{'Chức vụ':<15}"
          f"{'Lương CB':>12}{'Ngày công':>11}{'Phụ cấp':>12}{'Thực nhận':>15}")
    print("-" * 110)
    for nv in danh_sach:
        print(f"{nv['ma_nv']:<8}{nv['ho_ten']:<22}{nv['phong_ban']:<15}"
              f"{nv['chuc_vu']:<15}{nv['luong_co_ban']:>12,.0f}"
              f"{nv['so_ngay_cong']:>11.1f}{nv['phu_cap']:>12,.0f}"
              f"{nv['luong_thuc_nhan']:>15,.0f}")
    print("-" * 110)
    print(f"  Tổng số nhân viên: {len(danh_sach)}")


# ============ 3. CẬP NHẬT ============
def cap_nhat_nhan_vien(danh_sach):
    print("\n--- CẬP NHẬT NHÂN VIÊN ---")
    ma = nhap_chuoi_bat_buoc("  Nhập mã NV cần cập nhật: ")
    nv = tim_theo_ma(danh_sach, ma)
    if not nv:
        print("   Không tìm thấy nhân viên có mã này!")
        return

    print(f"  Đang cập nhật: {nv['ho_ten']} ({nv['ma_nv']})")
    print("  (Nhấn Enter để giữ nguyên giá trị cũ)")

    ho_ten = input(f"  Họ tên [{nv['ho_ten']}]: ").strip()
    if ho_ten:
        nv["ho_ten"] = ho_ten

    ngay_sinh = input(f"  Ngày sinh [{nv['ngay_sinh']}]: ").strip()
    if ngay_sinh:
        nv["ngay_sinh"] = ngay_sinh

    gioi_tinh = input(f"  Giới tính [{nv['gioi_tinh']}]: ").strip()
    if gioi_tinh:
        nv["gioi_tinh"] = gioi_tinh

    phong_ban = input(f"  Phòng ban [{nv['phong_ban']}]: ").strip()
    if phong_ban:
        nv["phong_ban"] = phong_ban

    chuc_vu = input(f"  Chức vụ [{nv['chuc_vu']}]: ").strip()
    if chuc_vu:
        nv["chuc_vu"] = chuc_vu

    luong_cb = input(f"  Lương cơ bản [{nv['luong_co_ban']:,.0f}]: ").strip()
    if luong_cb:
        try:
            val = float(luong_cb)
            if val < 0:
                print("   Lương không được âm, giữ nguyên.")
            else:
                nv["luong_co_ban"] = val
        except ValueError:
            print("   Giá trị không hợp lệ, giữ nguyên.")

    so_ngay = input(f"  Số ngày công [{nv['so_ngay_cong']}]: ").strip()
    if so_ngay:
        try:
            sn = float(so_ngay)
            if 0 <= sn <= 31:
                nv["so_ngay_cong"] = sn
            else:
                print("   Số ngày công phải 0-31, giữ nguyên.")
        except ValueError:
            print("   Giá trị không hợp lệ, giữ nguyên.")

    phu_cap = input(f"  Phụ cấp [{nv['phu_cap']:,.0f}]: ").strip()
    if phu_cap:
        try:
            pc = float(phu_cap)
            if pc < 0:
                print("   Phụ cấp không được âm, giữ nguyên.")
            else:
                nv["phu_cap"] = pc
        except ValueError:
            print("   Giá trị không hợp lệ, giữ nguyên.")

    nv["luong_thuc_nhan"] = tinh_luong_thuc_nhan(
        nv["luong_co_ban"], nv["so_ngay_cong"], nv["phu_cap"])
    print(f"  Cập nhật thành công! Lương thực nhận mới: {format_tien(nv['luong_thuc_nhan'])}")


# ============ 4. XÓA ============
def xoa_nhan_vien(danh_sach):
    print("\n--- XÓA NHÂN VIÊN ---")
    ma = nhap_chuoi_bat_buoc("  Nhập mã NV cần xóa: ")
    nv = tim_theo_ma(danh_sach, ma)
    if not nv:
        print("   Không tìm thấy nhân viên có mã này!")
        return
    xac_nhan = input(f"  Xác nhận xóa {nv['ho_ten']} ({nv['ma_nv']})? (y/n): ").strip().lower()
    if xac_nhan == "y":
        danh_sach.remove(nv)
        print("   Đã xóa nhân viên thành công!")
    else:
        print("   Hủy thao tác xóa.")


# ============ 5. TÌM KIẾM ============
def tim_kiem_nhan_vien(danh_sach):
    print("\n--- TÌM KIẾM NHÂN VIÊN ---")
    print("  1. Theo mã NV")
    print("  2. Theo họ tên")
    print("  3. Theo phòng ban")
    print("  4. Theo chức vụ")
    lua_chon = input("  Chọn tiêu chí (1-4): ").strip()

    if lua_chon not in ("1", "2", "3", "4"):
        print("   Lựa chọn không hợp lệ!")
        return

    tu_khoa = nhap_chuoi_bat_buoc("  Nhập từ khóa: ").lower()
    ket_qua = []

    for nv in danh_sach:
        if lua_chon == "1" and tu_khoa in nv["ma_nv"].lower():
            ket_qua.append(nv)
        elif lua_chon == "2" and tu_khoa in nv["ho_ten"].lower():
            ket_qua.append(nv)
        elif lua_chon == "3" and tu_khoa in nv["phong_ban"].lower():
            ket_qua.append(nv)
        elif lua_chon == "4" and tu_khoa in nv["chuc_vu"].lower():
            ket_qua.append(nv)

    if ket_qua:
        print(f"\n   Tìm thấy {len(ket_qua)} kết quả:")
        hien_thi_danh_sach(ket_qua)
    else:
        print("   Không tìm thấy nhân viên phù hợp.")


# ============ 6. SẮP XẾP ============
def sap_xep_nhan_vien(danh_sach):
    print("\n--- SẮP XẾP DANH SÁCH ---")
    if not danh_sach:
        print("  (Danh sách trống)")
        return
    print("  1. Theo họ tên (A→Z)")
    print("  2. Theo lương thực nhận (giảm dần)")
    print("  3. Theo số ngày công (giảm dần)")
    lua_chon = input("  Chọn tiêu chí (1-3): ").strip()

    if lua_chon == "1":
        danh_sach.sort(key=lambda x: x["ho_ten"].split()[-1])
        print("   Đã sắp xếp theo họ tên.")
    elif lua_chon == "2":
        danh_sach.sort(key=lambda x: x["luong_thuc_nhan"], reverse=True)
        print("   Đã sắp xếp theo lương thực nhận giảm dần.")
    elif lua_chon == "3":
        danh_sach.sort(key=lambda x: x["so_ngay_cong"], reverse=True)
        print("   Đã sắp xếp theo số ngày công giảm dần.")
    else:
        print("   Lựa chọn không hợp lệ!")
        return
    hien_thi_danh_sach(danh_sach)


# ============ 7. TÍNH LƯƠNG CHI TIẾT ============
def tinh_luong_chi_tiet(danh_sach):
    print("\n--- TÍNH LƯƠNG NHÂN VIÊN ---")
    if not danh_sach:
        print("  (Danh sách trống)")
        return
    ma = nhap_chuoi_bat_buoc("  Nhập mã NV cần tính lương: ")
    nv = tim_theo_ma(danh_sach, ma)
    if not nv:
        print("   Không tìm thấy nhân viên!")
        return
    print(f"\n  Nhân viên: {nv['ho_ten']} ({nv['ma_nv']})")
    print(f"  Lương cơ bản     : {format_tien(nv['luong_co_ban'])}")
    print(f"  Số ngày công     : {nv['so_ngay_cong']}")
    print(f"  Phụ cấp          : {format_tien(nv['phu_cap'])}")
    print(f"  Công thức        : ({nv['luong_co_ban']:,.0f} / 26) × {nv['so_ngay_cong']} + {nv['phu_cap']:,.0f}")
    print(f"  → Lương thực nhận: {format_tien(nv['luong_thuc_nhan'])}")


# ============ 8. THỐNG KÊ ============
def thong_ke(danh_sach):
    print("\n--- THỐNG KÊ NHÂN VIÊN ---")
    if not danh_sach:
        print("  (Danh sách trống)")
        return

    tong = len(danh_sach)
    luong_tb = sum(nv["luong_thuc_nhan"] for nv in danh_sach) / tong
    max_nv = max(danh_sach, key=lambda x: x["luong_thuc_nhan"])
    min_nv = min(danh_sach, key=lambda x: x["luong_thuc_nhan"])

    print(f"  • Tổng số nhân viên  : {tong}")
    print(f"  • Lương trung bình   : {format_tien(luong_tb)}")
    print(f"  • NV lương cao nhất  : {max_nv['ho_ten']} ({max_nv['ma_nv']}) - {format_tien(max_nv['luong_thuc_nhan'])}")
    print(f"  • NV lương thấp nhất : {min_nv['ho_ten']} ({min_nv['ma_nv']}) - {format_tien(min_nv['luong_thuc_nhan'])}")

    dem_phong_ban = {}
    for nv in danh_sach:
        pb = nv["phong_ban"]
        dem_phong_ban[pb] = dem_phong_ban.get(pb, 0) + 1

    print("\n  • Số lượng nhân viên theo phòng ban:")
    for pb, so_luong in dem_phong_ban.items():
        print(f"      - {pb}: {so_luong} nhân viên")


# ============ 9. LƯU FILE ============
def luu_du_lieu(danh_sach, ten_file=DATA_FILE):
    try:
        with open(ten_file, "w", encoding="utf-8") as f:
            for nv in danh_sach:
                f.write("|".join([
                    nv["ma_nv"], nv["ho_ten"], nv["ngay_sinh"],
                    nv["gioi_tinh"], nv["phong_ban"], nv["chuc_vu"],
                    str(nv["luong_co_ban"]), str(nv["so_ngay_cong"]),
                    str(nv["phu_cap"]), str(nv["luong_thuc_nhan"])
                ]) + "\n")
        print(f"  Đã lưu {len(danh_sach)} nhân viên vào file '{ten_file}'.")
    except IOError as e:
        print(f"  Lỗi ghi file: {e}")


# ============ 10. ĐỌC FILE ============
def doc_du_lieu(ten_file=DATA_FILE):
    danh_sach = []
    if not os.path.exists(ten_file):
        print(f"   File '{ten_file}' không tồn tại. Bắt đầu với danh sách trống.")
        return danh_sach
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if not dong:
                    continue
                parts = dong.split("|")
                if len(parts) != 10:
                    continue
                danh_sach.append({
                    "ma_nv": parts[0],
                    "ho_ten": parts[1],
                    "ngay_sinh": parts[2],
                    "gioi_tinh": parts[3],
                    "phong_ban": parts[4],
                    "chuc_vu": parts[5],
                    "luong_co_ban": float(parts[6]),
                    "so_ngay_cong": float(parts[7]),
                    "phu_cap": float(parts[8]),
                    "luong_thuc_nhan": float(parts[9])
                })
        print(f"  Đã đọc {len(danh_sach)} nhân viên từ file '{ten_file}'.")
    except (IOError, ValueError) as e:
        print(f"  Lỗi đọc file: {e}")
    return danh_sach


# ============ MENU ============
def hien_thi_menu():
    print("\n" + "=" * 42)
    print("        QUẢN LÝ NHÂN VIÊN")
    print("=" * 42)
    print("  1. Thêm nhân viên")
    print("  2. Hiển thị danh sách")
    print("  3. Cập nhật nhân viên")
    print("  4. Xóa nhân viên")
    print("  5. Tìm kiếm")
    print("  6. Sắp xếp")
    print("  7. Tính lương")
    print("  8. Thống kê")
    print("  9. Lưu dữ liệu")
    print(" 10. Đọc dữ liệu")
    print("  0. Thoát")
    print("=" * 42)


# ============ MAIN ============
def main():
    print("Đang tải dữ liệu...")
    danh_sach = doc_du_lieu()

    while True:
        hien_thi_menu()
        lua_chon = input("Lựa chọn: ").strip()

        if lua_chon == "1":
            them_nhan_vien(danh_sach)
        elif lua_chon == "2":
            hien_thi_danh_sach(danh_sach)
        elif lua_chon == "3":
            cap_nhat_nhan_vien(danh_sach)
        elif lua_chon == "4":
            xoa_nhan_vien(danh_sach)
        elif lua_chon == "5":
            tim_kiem_nhan_vien(danh_sach)
        elif lua_chon == "6":
            sap_xep_nhan_vien(danh_sach)
        elif lua_chon == "7":
            tinh_luong_chi_tiet(danh_sach)
        elif lua_chon == "8":
            thong_ke(danh_sach)
        elif lua_chon == "9":
            luu_du_lieu(danh_sach)
        elif lua_chon == "10":
            danh_sach = doc_du_lieu()
        elif lua_chon == "0":
            print("Tạm biệt! Chương trình kết thúc.")
            break
        else:
            print("   Lựa chọn không hợp lệ. Vui lòng chọn lại!")


if __name__ == "__main__":
    main()