Kode ini merupakan implementasi sistem pengelolaan data nilai siswa menggunakan pendekatan Object-Oriented Programming (OOP) dengan 3 kelas utama:
1. Class Student Data
   - Berfungsi sebagai pengelola data siswa
   - Memiliki atribut students berupa list untuk menyimpan data siswa
   - Memiliki method add_student untuk menambah data siswa baru (nama dan nilai)
   - Method get_students untuk mengambil semua data siswa yang tersimpan
2. Class Student View
   - Bertugas untuk menampilkan data siswa ke layar
   - Memiliki method display_students yang menampilkan daftar siswa dalam format tabel
   - Menggunakan string formatting untuk merapikan tampilan output
3. Class Student Process
   - Berfungsi sebagai pengontrol utama program
   - Menghubungkan StudentData dan StudentView
   - Memiliki method get_student_input untuk:
     - Menerima input nama dan nilai siswa
     - Melakukan validasi nilai (harus 0-100)
     - Menangani error jika input tidak valid
   - Method run untuk:
     - Menjalankan proses input data berulang
     - Memberi opsi untuk menambah data siswa lain
     - Menampilkan hasil akhir

Program ini menggunakan beberapa konsep penting:
- Exception handling (try-except) untuk menangani error input
- Validasi data untuk memastikan nilai dalam rentang 0-100
- Pemisahan tanggung jawab antar kelas (separation of concerns)
- Penggunaan if __name__ == "__main__" untuk menjalankan program
Cara kerja program:
1. User diminta memasukkan nama dan nilai siswa
2. Program memvalidasi input
3. User diberi pilihan untuk menambah data siswa lain
4. Setelah selesai, program menampilkan daftar semua siswa dan nilai mereka
# uas-pemograman
