Program ini terdiri dari beberapa fungsi yang masing-masing memiliki peran khusus. Berikut adalah penjelasan detailnya:

1. **List Awal**:
   ```python
   list_angka = []
   ```
   `list_angka` adalah sebuah list kosong yang akan digunakan untuk menyimpan angka-angka yang dimasukkan oleh pengguna.

2. **Fungsi insert_angka()**:
   ```python
   def insert_angka():
       angka = ""
       for x in range(1, 4, 1):
           angka = input("Masukkan Angka ke-{} kedalam List : ".format(x))
           list_angka.append(int(angka))
           x += 1
   ```
   Fungsi ini digunakan untuk memasukkan tiga angka ke dalam `list_angka`. Berikut adalah langkah-langkahnya:
   - Menggunakan loop `for` untuk mengulangi proses input sebanyak 3 kali (dari 1 hingga 3).
   - Meminta pengguna untuk memasukkan angka, yang kemudian diubah menjadi tipe `int` dan ditambahkan ke `list_angka`.

3. **Fungsi sorting_list()**:
   ```python
   def sorting_list():
       list_angka.sort()
       print(list_angka)
   ```
   Fungsi ini digunakan untuk mengurutkan `list_angka` secara ascending (dari kecil ke besar) dan kemudian mencetak hasil urutannya.

4. **Fungsi searching_list_item()**:
   ```python
   def searching_list_item():
       angka = input("Masukkan data yang ingin dicari : ")
       if int(angka) in list_angka:
           print("Angka {} ada di dalam List Angka".format(int(angka)))
       else:
           print("Maaf Angka {} tidak ada pada List Angka".format(int(angka)))
   ```
   Fungsi ini digunakan untuk mencari angka tertentu dalam `list_angka`. Langkah-langkahnya adalah:
   - Meminta pengguna memasukkan angka yang ingin dicari.
   - Mengecek apakah angka tersebut ada dalam `list_angka`.
   - Menampilkan pesan yang sesuai berdasarkan hasil pengecekan.

5. **Fungsi list_menu()**:
   ```python
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
   ```
   Fungsi ini menampilkan menu utama yang digunakan untuk menjalankan fungsi-fungsi di atas. Berikut adalah cara kerjanya:
   - Menampilkan pilihan menu kepada pengguna.
   - Menggunakan loop `while` agar menu terus muncul sampai pengguna memilih opsi untuk selesai (4).
   - Berdasarkan pilihan pengguna, fungsi yang sesuai akan dijalankan (`insert_angka`, `sorting_list`, `searching_list_item`, atau keluar dari loop dan mengakhiri program).

6. **Memulai Program**:
   ```python
   list_menu()
   ```
   Bagian ini memanggil fungsi `list_menu()` untuk memulai program.

Program ini merupakan contoh sederhana dari penggunaan fungsi untuk melakukan operasi dasar pada list angka, yaitu memasukkan data, mengurutkan data, dan mencari data. Semoga penjelasan ini membantu.
