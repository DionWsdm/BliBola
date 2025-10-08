Tugas 3
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

Tugas 6
Pertanyaan:
1. Apa perbedaan antara synchronous request dan asynchronous request?
2. Bagaimana AJAX bekerja di Django (alur request–response)?
3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

Jawaban:
1. Synchronous request adalah jenis permintaan di mana browser harus menunggu respons dari server sebelum bisa melanjutkan proses
   lainnya. Selama menunggu, halaman akan “terhenti” — pengguna tidak dapat berinteraksi secara lancar, dan jika responsnya lama, halaman bisa terasa lambat. Sebaliknya, asynchronous request memungkinkan browser mengirim permintaan ke server di belakang layar tanpa harus me-reload atau menghentikan interaksi pengguna. Dengan asynchronous, halaman dapat tetap responsif, dan data baru dapat dimuat secara dinamis tanpa transisi penuh.
2. AJAX bekerja dengan cara JavaScript mengirimkan permintaan ke URL Django (biasanya ke sebuah view) tanpa melakukan reload halaman.
   Django kemudian memproses permintaan tersebut, misalnya dengan mengambil data dari database, dan mengembalikan respons dalam bentuk JSON. Setelah itu, JavaScript menerima data JSON tersebut dan memperbarui tampilan halaman secara dinamis, misalnya menambahkan elemen baru atau mengubah isi konten tertentu. Alur sederhananya yakni: JavaScript --> View Django --> JSON Response --> Update Halaman.
3. Penggunaan AJAX memberikan pengalaman yang lebih cepat dan interaktif karena halaman tidak perlu dimuat ulang secara penuh setiap kali
   ada perubahan. AJAX juga memungkinkan pembaruan hanya pada bagian tertentu dari halaman, sehingga tampilan menjadi lebih dinamis dan efisien. Selain itu, pengelolaan data dan tampilan dapat dipisahkan dengan lebih jelas, sehingga pengembangan fitur menjadi lebih fleksibel dan terstruktur.
4. Keamanan tetap menjadi hal utama saat menggunakan AJAX, terutama untuk fitur login dan register. Pastikan setiap permintaan POST 
   menyertakan CSRF token agar terhindar dari serangan CSRF. Semua data yang dikirim melalui AJAX harus tetap divalidasi di sisi server, bukan hanya di sisi klien. Selain itu, gunakan HTTPS untuk melindungi data sensitif seperti kata sandi. Jangan pernah mengirimkan informasi sensitif atau pesan error internal secara langsung melalui respons AJAX.
5. AJAX dapat meningkatkan pengalaman pengguna karena membuat interaksi dengan website menjadi lebih cepat, responsif, dan tidak terganggu 
   oleh proses reload halaman. Misalnya, ketika pengguna menambahkan produk ke keranjang atau memfilter data, perubahan dapat muncul secara langsung tanpa berpindah halaman. Hal ini membuat website terasa lebih modern, interaktif, dan nyaman digunakan.