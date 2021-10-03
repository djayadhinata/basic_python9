def menu():
    print("Selamat Datang")
    print("---MENU---")
    print("1.Daftar Kontak")
    print("2.Tambah Kontak")
    print("3.Keluar")
DaftarKontakNama = []
DaftarKontakTelepon = []
menu()
option = int(input("enter Number: "))

while option != 3:
    if option == 1:
        print(DaftarKontakNama)
        print(DaftarKontakTelepon)

    elif option == 2:

        inputKontak = input("nama yang ingin ditambahkan: ")
        DaftarKontakNama.append(inputKontak)


        inputKontak = input("No telepon yang ingin ditambahkan: ")
        DaftarKontakTelepon.append(inputKontak)

        print(DaftarKontakNama)
        print(DaftarKontakTelepon)

    else :
        print("Menu Tidak tersedia")

    print()
    menu()
    option = int(input("enter number"))

print("program exit")




