
list_angka = []

def insert_angka():
    angka = ""
    for x in range(1, 4, 1):
        angka = input("Masukkan Angka ke-{} kedalam List : ".format(x))
        list_angka.append(int(angka))
        x += 1

def sorting_list():
    list_angka.sort()
    print(list_angka)

def searching_list_item():
    angka = input("Masukkan data yang ingin dicari : ")
    if int(angka) in list_angka:
        print("Angka {} ada di dalam List Angka".format(int(angka)))
    else:
        print("Maaf Angka {} tidak ada pada List Angka".format(int(angka)))

def list_menu():
    while True:
        menu = input("""1. Input angka\n2. Sorting\n3. Searching\n4. Selesai\nMasukkan Pilihan 1/2/3/4 : """)
        if int(menu) == 1:
            insert_angka()
        if int(menu) == 2:
            sorting_list()
        if int(menu) == 3:
            searching_list_item() 
        if int(menu) == 4:
            print("Program ini telah selesai")
            break

list_menu()