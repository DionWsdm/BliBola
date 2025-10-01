Tugas 4
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

Tugas 5
Pertanyaan:
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
2.  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Jawaban:
1. Urutan prioritas CSS (cascade & specificity):
   1) !important.
   2) Inline style (style="...")
   3) ID selector (#id)
   4) Class, attribute, pseudo-class (.class, [attr], :hover)
   5) Tag / element / pseudo-element (div, p, ::after)
   6) Source order. Kalau sama kuat, aturan yang ditulis terakhir yang menang.
2. Responsive design penting karena pengguna mengakses web dari berbagai perangkat dengan ukuran layar berbeda, mulai dari ponsel,
   tablet, hingga desktop. Tanpa desain responsif, tampilan web bisa berantakan, sulit dibaca, atau tombolnya terlalu kecil untuk disentuh, sehingga pengalaman pengguna (UX) menurun. Selain itu, Google juga memprioritaskan situs yang mobile-friendly dalam hasil pencarian, jadi desain responsif berpengaruh pada SEO. Contoh aplikasi yang sudah menerapkan responsive design adalah Airbnb atau Medium, di mana tata letak, ukuran font, dan gambar menyesuaikan secara mulus pada layar kecil maupun besar. Sebaliknya, banyak aplikasi lama seperti portal akademik universitas atau situs pemerintahan yang belum responsif, biasanya karena dibangun dengan teknologi lama berbasis tabel dan hanya dioptimalkan untuk desktop, sehingga sulit digunakan di perangkat mobile.
3. Perbedaan padding, border, dan margin:
   1) Padding
      Menambahkan space kosong di dalam elemen antara konten dan border. Digunakan dengna menambahkna atribut css seperti **padding: 16px;** atau padding
   2) Border
      Garis yang mengelilingi suatu elemen sesuai dengan width dan height elemen tersebut. Digunakan dengan menambahkan atribut seperti 
      **border: 2px solid #333;**
   3) Margin
      Menambahkan space kosong di luar elemen antara border suatu elemen dengan elemen lain. Digunakan dengan menambahkan atribut seperti 
      **margin: 12px 0;**
   Contoh penggunaan ketiganya di suatu elemen dengan nama class "card":
   .card {
      margin: 16px;               /* ruang luar */
      padding: 20px;              /* ruang dalam */
      border: 1px solid #ddd;     /* garis */
      border-radius: 8px;
      background: white;
   }
4. Flexbox adalah sistem layout 1 dimensi di CSS yang digunakan untuk mengatur elemen dalam satu arah, baik secara horizontal (row) 
   maupun vertikal (column). Flexbox sangat berguna untuk mengatur posisi, jarak antar item, dan alignment tanpa perlu banyak perhitungan manual. Dengan properti seperti justify-content, align-items, dan flex-wrap, kita bisa membuat elemen lebih fleksibel mengikuti ruang yang tersedia. Flexbox biasanya dipakai untuk hal-hal seperti navbar, tombol berderet, atau untuk melakukan centering elemen dengan mudah.
   Contoh penggunaan flexbox:
   .navbar {
      display: flex;
      justify-content: center;
      gap: 20px;
   }

   CSS Grid adalah sistem layout 2 dimensi yang memungkinkan kita mengatur baris dan kolom sekaligus, sehingga lebih cocok untuk struktur halaman yang kompleks. Dengan grid-template-rows, grid-template-columns, dan grid-template-areas, kita bisa membuat layout seperti header, sidebar, content, dan footer dengan lebih rapi dan terkontrol. Grid juga mendukung fungsi-fungsi seperti repeat() dan minmax() sehingga layout bisa lebih responsif sesuai ukuran layar.
   Contoh penggunaan grid:
   .layout {
      display: grid;
      grid-template-columns: 250px 1fr;
      gap: 16px;
   }
5. Cara saya mengimplementasikan checklist secara step-by-step:
   1) Mengubah theme default aplikasi menjadi dark theme.
   2) Mengubah page register dan login menjadi 1 card di center.
   3) Membuat komponen card_product.html yang akan digunakan untuk menampilkna produk pada home page.
   4) Membuat komponen navbar.html untuk ditampilkan pada homepage.
   5) Mengubah page main.html agar sesuai dengan theme dan menambahkan navbar serta menampilkan produk dengan card.
   6) Mengubah page create_product.html menjadi 1 card besar dengan warna yang disesuaikan agar lebih sesuai dengan theme.
   7) Mengubah page detail_product.html agar lebih sesuai dengan theme.
   8) Membuat fungsi edit_product dan delete_product pada views.py dan menambahkna path dengan fungsi tersebut di urls.py
   9) Membuat page edit_product.html dengan tampilan mirip seperti create_product.html yang bertujuan sebagai page ketika user ingin mengedit   produk mereka.