Pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py,    models.py, dan berkas html.
3. Jelaskan peran settings.py dalam proyek Django!
4. Bagaimana cara kerja migrasi database di Django?
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Jawaban:
1. Cara saya mengimplementasikan checklist secara step-by-step:
    1) Mengaktifkan virtual environment
    2) Menginstal django dan package-package lain yang dibutuhkan terlebih dahulu. 
    3) Men-setup project, seperti membuat folder dan file-file yang dibutuhkan, seperti .env, .env.prod, folder BliBola, folder main, mengedit file setttings.py agar project bisa dihost di lokal ataupun pws, dan lainnya.
    4) Pada file "models.py" di dalam folder main, saya membuat sebuah class bernama Product yang merupakan sebuah subclass dari models.Model (berarti Product adalah sebuah Model).
    5) Pada model Product, saya menambahkan beberapa field, yakni "id" (AutoField) sebagai primary_key, "name" (CharField) sebagai nama dari produk, "price" (IntegerField) sebagai harga dari produk, "description" (TextField) sebagai deskripsinya, "thumbnail" (URLField) sebagai foto produk, "category" (CharField) sebagai kategori produk, is_featured (BooleanField) sebagai status apakah produk diunggulkan, dan rating (FloatField) sebagai nilai kepuasan pembeli produk.
    6) Membuat folder "templates" pada folder "main" dan membuat file "main.html" sebagai template dari project.
    7) Membuat fungsi show_main pada views.py yang berfungsi untuk merender informasi-informasi yang ingin ditampilkan pada template.
    7) Menambahkan elemen-elemen yang dibutuhkan pada file main.html sebagai template untuk menampilkan nama aplikasi, nama saya, dan kelas saya.
    8) Membuat file urls.py pada folder main. Pada file tersbut, saya membuat dua variabel yakni app_name sebagai namespace unik dari proyek dan urlpatterns sebagai tempat menyimpan endpoint-endpoint yang ada pada proyek nantinya.
    9) Memodifikasi file urls.py pada folder BliBola dan menambahkan sebuah path di variabel urlpatterns untuk menyambungkan dengan file urls.py pada folder main dengan menggunakan fungsi include.
    10) Mencoba untuk menjalankan server di lokal dan melihat bahwa tampilan sudah sesuai dengan yang diinginkan.
    11) Membuat repository git baru dan menginisialiasi git pada proyek ini.
    12) Melakukan push ke github dan deployment ke pws.
2. Gambar bagan: https://drive.google.com/file/d/176C6_cgHF_CaqgjoJ0wQZesNhr4aXy9M/view?usp=sharing
   Penjelasan:
   Ketika cliet mengirimkan request ke aplikasi, maka server akan meneruskan request ke file urls. File urls.py akan mengecek endpoint mana yang ingin diakses oleh client dan menjalankan fungsi view yang ada pada file views.py yang sesuai untuk endpoint tersebut. Fungsi view tersebut dapat melakukan pembacaan / penulisan data yang akan diteruskan ke file models.py sesuai dengan model yang berkaitan. Models.py akan mengembalikan data-data yang diinginkan ke views.py untuk selanjutnya dioper ke template html. Template akan dirender bersama data tersebut, lalu menghasilkan response dalam bentuk halaman web yang ditampilkan kembali ke layar client.
3. Dalam proyek django, file settings.py berisikan konfigurasi-konfigurasi dari instalasi django. Dokumen ini mengatur bagaimana pengaturan-pengaturan
   tersebut bekerja dan apa yang boleh diubah. Variabel-variabel yang ada pada file tersebut boleh diubah sesuai keperluan proyek. Contohnya, pada proyek ini saya merubah variabel ALLOWED_HOST dengan menambahkan string localhost dan link pws. Variabel ALLOWED_HOST sendiri mengatur domain-domain yang berhak / diperbolehkan untuk mengakses server. Saya juga mengubah variabel DATABASES agar proyek mengakses database yang berbeda pada localhost dan pws dan menambahkan string main di variabel INSTALLED_APPS.
4. Migrasi database pada django membaca perubahan model-model yang ada pada models.py dan menerapkannya pada database. Setelah merubah / menambahkan model 
   pada models.py, kita bisa menjalankan perintah 'python manage.py makemigrations' pada terminal untuk django membaca perubahan, membuat file migrasi di direktori 'migrations/', dan mengisi file tersebut dengan intsruksi python untuk merubah struktur database nantinya. Setelah itu kita jalankan 'python manage.py migrate' dimana django akan menerjermahkan instruksi-instruksi yang ada pada file migrasi ke perintah-perintah SQL untuk mengeksekusi perubahan struktur database. Setelah semua perubahan dieksekusi, django akan membuat catatan di tabel khusus bernama django_migrations sehingga django tahu perubahan mana yang sudah pernah dijalankan.
5. Menurut saya, django cocok untuk dijadikan permulaan pembelajaran pengembangan perangkat lunak karena beberapa hal berikut:
   1) Proses instalasi yang relatif lebih singkat dibanding framework-framework pada bahasa pemrograman lain.
   2) Interaksi dengan database yang mudah sehingga pemula tidak perlu mempelajari dan membuat perintah-perintah SQL.
   3) Menggunakan arsitektur MVT yang melatih pengembang untuk berpikir secara struktural dalam membangun dan menentukan model-model yang ada, 
      endpoints, fungsi-fungsi view, dan tampilannya pada pengguna.
   4) Bahasa pemrograman python sendiri yang relatif lebih mudah dipelajari dan dipahami dibanding bahasa-bahasa pemrograman lain sehingga pengembang 
      bisa mengetahui fungsi / kegunaan dari suatu nama file, fungsi bawaan, atribut dan keyword-keyword lain hanya dengan mengetahui arti dari kosakatanya.
   5) Terdapat fitur bawaan seperti admin panel dimana pengembang dapat melihat isi dari model-model pada database dan fitur autentikasi usernya yang sudah
      dibuat langsung oleh django.
6. Tidak ada, sudah cukup baik.