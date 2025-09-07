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