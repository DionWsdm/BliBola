Pertanyaan:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
   Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Jawaban:
1. Sebuah platform tidak akan berguna tanpa data delivery. Data delivery berfungsi sebagai mekanisme untuk memastikan data yang disimpan di backend (database)
   dapat diakses, dikirim, dan diterima oleh pengguna maupun sistem lain secara cepat, aman, dan lengkap. Tanpa data delivery yang baik, informasi mungkin tidak bisa terkirim ataupun informasi yang dikirimkan tidak mencukupi kebutuhan user atau sistem yang meminta data tersebut. Bisa dibayangkan jika platform-platform e-commerce seperti tokoepedia atau shopee tidak mengimplementasikan data delivery, maka pengguna tidak bisa melihat katalog produk, detail produk, dan membuat order.

2. Menurut saya, JSON lebih baik dibandingkan XML, dan saya sendiri lebih menyukai format json. JSON lebih populer karena beberapa hal seperti:
   1) Kemudahan & Kesederhanaan
      Format json lebih mudah untuk dilihat dan dipahami oleh pengembang karena formatnya sendiri mirip seperti struktur data dictionary atau map dan cara pengaambilan datanya juga mirip.
   2) Performa dan Efisiensi yang Lebih Baik
      Format JSON biasanya lebih cepat untuk di-parse dan diproses dibandingkan XML. Ukurannya yang cenderung lebih kecil dibandingkan format XML membuat proses transfer data. Ini menjadi keunggulan yang penting untuk aplikasi-aplikasi yang membutuhkan performa real-time.
   3) Kemudahan Integrasi dengan JavaScript
      Struktur JSON dapat diarahkan secara langsung menjadi objek JavaScript, salah satu bahasa pemrograman yang paling banyak digunakan untuk pengembangan website. Hal ini mensimplifikasi manipulasi data dan kebutuhan untuk mem-parse data.

3. Fungsi is_valid() adalah method bawaa Django Form yang digunakan untuk menvalidasi data yang dikirim dari form. Fungsi is_valid mengecek apakah semua
   field di form sudah diisi sesuai aturan (tipe data, panjang teks, format email, dsb). Fungsi ini juga menangani error. Jika ada field yang tidak valid, is_valid() akan mengembalikan False, dan error tersebut bisa diakses melalui atribut form.errors.

4. csrf_token digunakan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Saat membuat form dengan {% csrf_token %}, Django menyisipkan token 
   unik, acak, dan terikat pada sesi user. Token ini harus dikirim kembali bersama setiap POST request (atau method lain yang memodifikasi data, seperti PUT/DELETE). Django kemudian memverifikasi token, jika cocok, request dianggap sah berasal dari user, kalau tidak cocok atau csrf_token tidak ada, request ditolak. jika kita tidak menambahkan csrf_token, form tidak akan diproses karena Django otomatis menolak request tanpa token valid. Kalau proteksi CSRF dimatikan, aplikasi menjadi rentan terhadap serangan CSRF.

   Jika CSRF protection tidak ada atau dimatikan, penyerang bisa membuat halaman berbahaya (misalnya HTML form tersembunyi atau JavaScript otomatis submit). Jika user sedang login ke aplikasi target, browser akan mengirimkan cookie session user secara otomatis saat mengakses halaman jahat tersebut. Dengan cookie user yang sah, penyerang dapat melakukan berbagai aksi berbahaya seperti menghapus data penting atau mengganti password atau email seolah-olah itu dilakukan oleh user sendiri.

5. Cara saya mengimplementasikan checklist secara step-by-step:
   1) Saya membuat folder templates pada root folder dan di dalamnya saya buat file HTML baru bernama base.html. File html ini nantinya akan menjadi kerangka
      untuk halaman-halaman web lain di proyek.
   2) Mendaftarkan folder templates tersebut sebagai template di proyek dengan cara memodifikasi file settings.py di folder BliBola. Pada file tersebut saya
      menambahkan BASE DIR / 'templates' (path ke folder templates di root) di dictionary pertama di variabel TEMPLATES agar file base.html terdeteksi sebagai file template.
   3) Membuat templates-templates lain yang ada di direktori main untuk meng-extend template base.html.
   4) Saya membuat sebuah form, yakni ProductForm yang berfungsi untuk menambahkan data produk baru di sebuah file baru bernama forms.py di direktori main.
      Dalam ProductForm tersebut saya buat modelnya merujuk ke model Product yang ada di models.py dan menambahkan atribut-atribut yang bisa dikirim oleh user
      ketika menambahkan sebuah produk.
   5) Saya memodifikasi berkas views.py untuk mendukung beberapa fitur proyek. Pertama, pada fungsi show_main, saya menambahkan product_list kedalam 
      context yang dirender, sehingga nanti bisa ditampilkan di template show_main.html. Kedua, saya membuat fungsi create_product yang berfungsi ketika user
      ingin menambahkan data produk baru. Fungsi ini berfungsi untuk menampilkan tampilan form di template create_product.html (akan dibuat nanti) sebagai tempat user menginput data dan menyimpan data produk baru ketika user mensubmitnya. Ketiga, saya membuat fungsi show_product dengan tambahan parameter id. Fungsi ini bertujuan untuk merender detail suatu produk dengan id tertentu ke ke template product_detail.html (akan dibuat nanti).
   6) Mendaftar 2 fungsi baru di views.py ke urls.py. Fungsi create_product didaftarkan untuk url create-product/ dan show_product untuk url product/<str:id>/ 
      (terdapat 1 parameter, yakni id produk).
   7) Membuat 2 template baru di direktori main pada folder templates, yakni create_product.html sebagai tampilan ketika user ingin menambahkan produk baru
      dan product_detail.html sebagai tampilan ketika user mengunjungi suatu detail produk tertentu. Selain itu, saya juga memodifikasi template main.html untuk menampilkan daftar produk yang tersedia.
   8) Membuat 4 fungsi views baru di file views.py, yakni show_xml dan show_json yang berfungsi untuk mengembalikan data dari seluruh product yang ada (list)
      dalam format xml dan json, juga show_xml_by_id dan show_json_by_id yang berfungsi untuk mengembalikan data dari sebuah product dengan id tertentu dalam format xml dan json.
   9) Untuk setiap 4 fungsi views baru tersebut, ditambahkan path ke urls.py, yakni path 'xml/' untuk show_xml, 'json/' untuk show_json, 'xml/<str:product_id>'
      untuk show_xml_by_id, 'json/<str:product_id>' untuk show_json_by_id.
   Screenshot dari hasil akses URL pada Postman:
   https://drive.google.com/drive/folders/1HT4XRj9gwzEo-VqwibKbJpJde4bHd5gQ?usp=sharing
6. Tidak ada.