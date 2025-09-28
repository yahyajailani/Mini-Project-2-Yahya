# Nama : Yahya Jailani
# Tugas: MinproDDP2
# Tema : Sistem Manajemen Aplikasi LUNApos
# Kelas: Sistem Informasi C

menu = []

users = {
    "manager": {"password": "54143", "role": "Manager"},
    "karyawan": {"password": "75864", "role": "Karyawan"}
}


barang = {
    1: {"nama": "Pulpen", "harga": 3000, "stok": 50},
    2: {"nama": "Buku Tulis", "harga": 5000, "stok": 30}
}


def login():
    print("===== LOGIN SISTEM LUNApos =====")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username]["password"] == password:
        print(f"\nLogin berhasil! Selamat datang {username} ({users[username]['role']})\n")
        return users[username]["role"]
    else:
        print("Login gagal! Username atau password salah.\n")
        return None


def tampilkan_barang():
    print("===== DAFTAR BARANG =====")
    print("1. pulpen")
    print("2. buku tulis")
    

def tambah_barang():
    try:
        id_barang = int(input("Masukkan id barang: "))
        nama = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
        barang[id_barang] = {"nama": nama, "harga": harga, "stok": stok}
        print("Barang berhasil ditambahkan!\n")
    except ValueError:
        print("Input tidak valid! Pastikan harga dan stok berupa angka.\n")


def update_barang():
    try:
        tampilkan_barang()
        id_barang = int(input("Masukkan ID barang yang akan diupdate: "))
        if id_barang in barang:
            nama = input("Masukkan nama baru: ")
            harga = int(input("Masukkan harga baru: "))
            stok = int(input("Masukkan stok baru: "))
            barang[id_barang] = {"nama": nama, "harga": harga, "stok": stok}
            print("Barang berhasil diperbarui!\n")
        else:
            print("ID barang tidak ditemukan!\n")
    except ValueError:
        print("Input tidak valid! Pastikan ID, harga, dan stok berupa angka.\n")

        
def hapus_barang():
    try:
        tampilkan_barang()
        id_barang = int(input("Masukkan ID barang yang akan dihapus: "))
        if id_barang in barang:
            del barang[id_barang]
            print("Barang berhasil dihapus!\n")
        else:
            print("ID barang tidak ditemukan!\n")
    except ValueError:
        print("Input tidak valid! Masukkan angka ID yang benar.\n")


def main():
    role = None
    while not role:
        role = login()

    while True:
        if role == "Manager":
            print("\n===== MENU MANAGER =====")
            print("1. Tambah Barang")
            print("2. Tampilkan Barang")
            print("3. Update Barang")
            print("4. Hapus Barang")
            print("5. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tambah_barang()
            elif pilihan == "2":
                tampilkan_barang()
            elif pilihan == "3":
                update_barang()
            elif pilihan == "4":
                hapus_barang()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan LUNApos!\n")
                break
            else:
                print("Pilihan tidak valid!\n")

        elif role == "Karyawan":
            print("\n===== MENU KARYAWAN =====")
            print("1. Tampilkan Barang")
            print("2. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tampilkan_barang()
            elif pilihan == "2":
                print("Terima kasih telah menggunakan LUNApos!\n")
                break
            else:
                print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()