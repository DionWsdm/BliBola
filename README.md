Pertanyaan:
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus 
   diwaspadai? Bagaimana Django menangani hal tersebut?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawaban:
1. AuthenticationForm adalah form bawaan Django yang dipakai untuk menangani proses login user. Form ini secara otomatis 
   sudah menyediakan field untuk username dan password, serta melakukan validasi terhadap keduanya dengan memeriksa data ke model User.
   Kelebihan:
   1) Sudah terintegrasi penuh dengan sistem autentikasi Django.
   2) Meng-handle validasi secara otomatis (misalnya: username atau password salah).
   3) Bisa langsung dipakai tanpa banyak konfigurasi atau modifikasi tambahan.
   Kekurangan:
   1) Hanya mendukung login berbasis username + password secara default (kalau mau login pakai email atau custom field perlu extend).
   2) Validasi terbatas sesuai rule Django, jadi untuk kasus spesifik perlu subclassing.

2. Autentikasi adalah proses verifikasi identitas pengguna (Apakah seorang pengguna terdaftar). Sedangkan, otorisasi merupakan
   proses verifikasi apakah seorang pengguna yang telah terautentikasi berhak terhadap suatu aksi atau fitur yang ingin diakses. Django mengimplementasikan autentikasi melalui framework bawaan django.contrib.auth, yang menyediakan fungsi seperti authenticate(), login(), serta middleware AuthenticationMiddleware untuk menambahkan informasi user ke dalam objek request. Sedangkan otorisasi di Django diatur menggunakan sistem permission, group, serta decorator seperti @login_required atau @permission_required. Dengan cara ini, Django menyediakan mekanisme untuk memastikan hanya pengguna yang benar dan berhak yang bisa mengakses fitur atau informasi tertentu.

3. Session dan cookies adalah dua cara utama untuk menyimpan state pengguna, masing-masing memiliki kelebihan dan kekurangan.
   Session menyimpan data di sisi server, sehingga lebih aman karena pengguna tidak bisa langsung mengubah isinya, serta mampu menampung data yang lebih kompleks. Namun, session membutuhkan penyimpanan tambahan seperti database atau cache, dan dapat membebani server terutama jika jumlah pengguna sangat banyak. Di sisi lain, cookies menyimpan data di sisi client, sehingga lebih ringan bagi server dan cocok untuk menyimpan informasi kecil seperti mode tampilan (dark atau light mode) atau bahasa. Kekurangannya, cookies rentan dimanipulasi atau disadap karena berada di sisi client, kapasitas penyimpanannya juga terbatas, serta lebih berisiko terhadap serangan keamanan seperti XSS atau CSRF jika tidak diamankan dengan benar.

4. Cookies tidak sepenuhnya aman secara default. Berikut adalah beberapa risiko dari penggunaan cookies:
   1) XSS (Cross-Site Scripting): attacker bisa mencuri cookie jika script berbahaya dijalankan.
   2) Session Hijacking: kalau cookie session dicuri, attacker bisa menyamar jadi user.
   3) Man-in-the-Middle Attack: jika tidak pakai HTTPS, cookie bisa disadap.

   Django menyediakan berbagai mekanisme dalam menghadapi risiko keamanan dalam penggunaan cookies. Secara default, Django memungkinkan pengaturan parameter 'httponly' saat mengirim cookie melalui method set_cookie() agar cookies tidak dapat diakses melalui JavaScript, sehingga lebih terlindungi dari serangan XSS. Selain itu, parameter 'secure' juga dapat diaktifkan agar cookies hanya dikirim melalui koneksi HTTPS, sehingga mencegah pencurian data lewat serangan man-in-the-middle. Django juga mendukung pengaturan umur cookies melalui parameter max_age pada method set_cookie() atau variabel SESSION_COOKIE_AGE di settings.py untuk membatasi waktu hidup sesi pengguna. Dari sisi penyimpanan, session dapat dikelola menggunakan SESSION_ENGINE di settings.py, sehingga data penting tidak harus disimpan langsung di cookies, melainkan di server (misalnya database atau cache). Untuk melindungi dari serangan CSRF, Django otomatis menyertakan CSRF token pada form. Terakhir, dengan pengaturan SESSION_COOKIE_SAMESITE di settings.py, Django membantu membatasi pengiriman cookies lintas domain agar tidak digunakan secara ilegal melalui aplikasi lain.

5. Cara saya mengimplementasikan checklist secara step-by-step:
   1) Membuat fungsi register() di views.py yang menggunakan form dari UserCreationForm() yang diimport dari django.contrib.auth.forms. Fungsi ini akan
      merender tampilan untuk registrasi atau menyimpan user baru jika pengguna mengirimkan request dengan metode POST.
   2) Membuat template register.html pada direktori main/templates sebgai template yang akan dirender oleh fungsi register() dari views.py.
   3) Menambahkan sebuah path (endpoint) di urls.py pada direktori main yakni 'register/' untuk mengakses fungsi dan tampilan register tadi.
   4) Membuat fungsi login_user() di views.py yang menggunakan form dari AuthenticationForm() yang diimport dari django.contrib.auth.forms.
      Fungsi ini akan merender tampilan untuk registrasi atau melogginkan user jika user mengirim request dengan http method POST dan mengirim cookie 'last_login' yang mencatat kapan terakhir kali user tersebut login.
   5) Membuat template login.html pada direktori main/templates sebgai template yang akan dirender oleh fungsi login_user() dari views.py.
   6) Menambahkan sebuah path (endpoint) di urls.py pada direktori main yakni 'login/' untuk mengakses fungsi dan tampilan login tadi.
   7) Membuat fungsi logout_user() di views.py pada direktori main yang berfungsi untuk melakukan mekanisme logout. Ketika logout, 
      cookie 'last_login' akan dihapus.
   8) Menambahkan decorator @login_required untuk fungsi show_main() dan show_product() di views.py sehingga yang bisa mengakses halaman
      tersebut adalah user yang sudah terautentikasi saja. Dalam decorator tersebut, ditambahkan parameter login_url='login/' sehingga ketika user yang belum terautentikasi mencoba mengakses path '' atau 'product/<str:id>/', maka user akan diredirect ke path 'login/' untuk login terlebih dahulu.
   9) Memodifikasi berkas main.html di direktori main/templates untuk menampilkan informasi last login user yang sudah disimpan di cookie user.
   10) Menghubungkan model Product dengan User dari django.contrib.auth.models sehingga setiap product memiliki field user (siapa yang
       menambahkan product) dengan menambahkan atribut user yang berupa ForeignKey menuju model User.
   11) Membuat fitur filter pada fungsi show_main() di views.py sehingga user bisa memilih untuk melihat semua produk yang ada atau hanya
       produk yang ia tambahkan saja dan menambahkan dua tombol ("my" dan "all") pada template main.html untuk bisa menggunakan fitur filtering tersebut.