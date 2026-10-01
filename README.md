Nama : Roisul Umam

NPM : 2506620210

Kelas : PBP F

# Rois - Personal Portfolio

Website portofolio pribadi untuk menampilkan profil, skills, dan project sebagai mahasiswa S1 Ilmu Komputer, Fakultas Ilmu Komputer, Universitas Indonesia.

## Live Demo
[https://roisul-umam-myportofolio.pws.cs.ui.ac.id/]

## Deskripsi
Portofolio ini dibangun menggunakan HTML dan CSS dengan framework Django. Terdiri dari beberapa section utama: Profile, Skills, dan Projects.

## Tech Stack
- Python (Django)
- HTML5 (Django Template)
- CSS3 (Grid, Flexbox, CSS Variables)
- Google Fonts (Space Grotesk)

## Fitur
- **Profile Section** — Menampilkan foto, biodata singkat, NPM, program studi, dan link sosial media (GitHub, LinkedIn, Email).
- **Skills Section** — Menampilkan daftar skill teknis dalam bentuk tag.
- **Experience & Projects Page** — Menampilkan daftar project-project yang pernah dikerjakan dalam bentuk card dan juga menampilkan penglaman-pengalaman aku sendiri.
- **Responsive Design** — Layout menyesuaikan otomatis untuk mobile dan desktop menggunakan CSS Grid dan media query.

## Rencana Pengembangan (Roadmap)
- [ ] Menambahkan page "Education"
- [ ] Menambahkan animasi pada web menggunakan JavaScript
- [ ] Membuat button switch mode
- [ ] Menghubungkan form kontak yang langsung terkirim ke hp lewat aplikasi buatan

## Author
**Rois (Roisul Umam)**
NPM: 2506620210
S1 Ilmu Komputer, Fakultas Ilmu Komputer, Universitas Indonesia
- GitHub: [@Roisul-Umam](https://github.com/Roisul-Umam)
- LinkedIn: [Roisul Umam](https://www.linkedin.com/in/roisul-umam-83577b302/?locale=en)
- Email: umamr545@gmail.com

# Tugas
## Tugas 1

1. Yap aku menggunakan elemen semantik seperti artikel, header dll dalam merancang website portofolio ini, karena ini membuat kode aku itu lebih terstruktur dan mudah dibaca oleh kita sebagai manusia.
2. Selama aku membangun website ini, aku tidak menemukan tantangan tata letak ukuran ketika berpindah ke mobile, tetapi jika hal itu terjadi, aku akan segera menggunakan CSS grid/flexbox agar elemennya bisa menumpuk kebawah ketika dibuka di layar yg vertical.
3. Batasan yang paling aku alami pada website static ini adalah tidak adanya backend. Feedback system adalah fitur yang aku sangat ingin tambahkan pada website ini, namun ketidak adaannya datebase membuat hal ini gabisa terjadi karena tidak adannya sistem penyimpanan data secara real time.

## Tugas 2

1. Pengguna mengetik URL website aku lalu konfigurasi url projek mengfordward requestnya ke konfigurasi url versi aplikasi lalu konfigurasi url versi aplikasi ini menentukan view mana yg harus menangani request url yg diketikan pengguna tadi lalu views menerima perintah tsb dan meminta data porto ke models lalu models ambil data ke DB dan menyerahkannya ke views, views ini nyimpen datanya ke ke file template html lalu template html ini ngerakit data dari views supaya jadi halaman web yang siap ditampilin.
2. Akan lebih mudah untuk maintenance nya, karna data di portofolio itu akan bertambah maka dari itu sebaiknya tidak di hardcode pada template untuk memudahkan kita pada saat mau menambah datanya, lalu juga mengantisipasi redundansi, jika data ingin ditampilkan pada beberapa halaman, kita cukup call dari database saja tidak perlu mempaste teks yg sama. 
3. makemigrations ituu untuk mendeteksi file yang berubah dan membuat perintah sql untuk migrasi, sedangkan migrate itu untuk mengeksekusi perintah sql yg dibuat oleh makemigrations. Implementasi makemigrations dan migrate dalam projek aku ada pada bagian Projects, aku menambahkan class baru di models.py dan ketika aku makemigrations, django akan otomatis membuat file migrations yang ada pada main dan itu isinya perintah sql yang akan dieksekusi ketika aku mengetik migrate.

## Tugas 3

1. Biar kita sebagai developer itu garibet validasi tiap field, nulis logic buat nyimpen inputan ke model, trus juga ga ribet nampilin errornya kalo ada validasi gagal, jd kalo kita pake modelform (kalo di program ini contohnya kayak projectform) kita cuma taro 1 kayak `fields` yang ada di projectform, ntar django otomatis tau kalo project_url itu harus mereka validasi sebagai URL dan seterusnya, jadi si form ini ngikutin struktur model, jd kita tinggal ngurusin aja di model nya. Alasan `{% csrf_token %}` wajib itu biar kalo aku lagi login ke web ini dan ternyata aku gasengaja buka web jahat lain dan si web jahat ini ternyata punya `<form action="http://localhost:8000/projects/5/delete/" method="post">` nanti di web aku bakal kehapus otomatis gara gara aku ga nerapin token csrf, jd yg hapus si web jahat itu, jadi ibarat token tersembunyi kalo tokennya ga sama nanti web ini bakal nolak request delete dari web jahat tsb.
2. JSON lebih ringkas, gakaya XML sebagai perbandingan, contoh XML = `<project><title>Rainfall data model</title><tech_stack>Python, Kaggle</tech_stack></project>` dan kalo JSON = `projects_json = serializers.serialize("json", projects)` trus yang kedua adalah native ke JS jd kalo nanti aku bikin fitur di FE yg fetch data dari API projects, tinggal pake JS fetch() aja nah nanti result JSON nya bisa langsung dipake sebagai object JS.
3. Alur di view nya adalah kita ngetik misal `api/projects` trus nanti views nge return data dari database pake ORM trus nanti datanya di serialize dari py ke JSON nah nanti view nge return balik barupa response kayak `HttpResponse(data, content_type="application/json")`. Nah alasan kenapa harus pake serialize simplenya buat nge penerjemah yg ngubah objek python jadi format teks JSON supaya bisa dikirim lewat HTTP dan browser bisa ngerti itu.

## Tugas 5
1. Debouncing itu kayak ngasih jeda pas kita ngetik di fitur pencarian, nah kalo kita gapake debouncing, misal kita baru ketik satu huruf aja, browser bakal ngirim HTTP request ke server, nah ini yang bikin server jebol, jadi kalo kita kasih aja debouncing 300ms (0.3 detik), pas kita beres ngetik, si browser baru ngirim request, nah ini yang bikin aman, jadinya server gabakal jebol.
2. Fungsi `await` pada `fetch()` adalah buat nunda eksekusi baris kode selanjutnya sampe proses pengambilan data dari server selesai, sehingga data tersebut siap dipakaii.
3. Misal ada yg nambahin project, trus nama projectnya `<script>alert('Akun kamu di-hack!');</script>`, kalo django, dia otomatis bakal ngubah kodenya jadi teks mentah (`&lt;script&gt;`) nah jadinya si script itu gabakal dijalanin, jatohnya kaya teks biasa. Beda nih kalo di AJAX/JS, browser bakal ngira itu instruksi resmi, jadinya dia bakal ngejalanin kode tersebut saat itu juga.

## AI Disclosure Tugas 1 & 2

Bagian *"Skills & Projects"* pada portofolio ini dikembangkan dengan bantuan AI assistant (Claude, Anthropic) untuk mempercepat proses penulisan HTML dan CSS awal.

### Cakupan Bantuan AI
- AI digunakan untuk menghasilkan struktur HTML section baru (skills tags dan project cards).
- AI digunakan untuk menghasilkan styling CSS yang konsisten dengan desain hero section yang sudah ada sebelumnya (warna, radius, font, spacing).

### Keterbatasan AI yang Diidentifikasi
Beberapa keterbatasan yang disadari dari hasil AI dan perlu ditinjau ulang secara manual:

1. Konten placeholder, bukan konten nyata. AI tidak memiliki akses ke daftar project atau skill aku yang sebenarnya, sehingga nama project, deskripsi, dan tag teknologi yang dihasilkan masih berupa contoh generik (misalnya "Nama Project 1", deskripsi template). Ini wajib diganti manual dengan data project asli.
2. AI melakukan hardcoding, bukan solusi dinamis. Pada iterasi pertama, AI menghasilkan setiap item skill dan project card secara statis langsung di HTML/template (`<li>Python</li>`, `<article class="project-card">...</article>` ditulis berulang satu per satu).
3. Tidak memahami konteks personal/preferensi desain secara utuh. AI meniru pola desain yang sudah ada (warna aksen, border tipis, radius kecil) berdasarkan analisis kode CSS yang diberikan, tapi tidak punya "selera" — keputusan akhir soal apakah gaya visual ini cocok tetap ada di tangan aku.

### Penyesuaian Manual yang Dilakukan
- Mengganti seluruh konten placeholder project dengan data project asli (nama, deskripsi, tech stack, link repo).
- Menyesuaikan jumlah dan urutan skill sesuai kemampuan yang benar-benar aku kuasai.
- Melakukan pengecekan tampilan di beberapa ukuran layar (mobile, tablet, desktop).
- Me-refactor konten yang sebelumnya di-hardcode di HTML (bio, skills, projects) menjadi data yang dikirim dari `views.py` sebagai context, lalu ditampilkan di template menggunakan Django template tag (`{{ }}` dan `{% for %}`).
- Menyesuaikan struktur dict di `views.py` dengan data project dan skill aku yang sebenarnya.

### Kesimpulan
AI digunakan sebagai alat bantu untuk mempercepat proses coding (*scaffolding* HTML/CSS) dan mengimplementasikan algoritma yang telah aku buat sebelumnya, bukan sebagai pengganti proses berpikir dan pengambilan keputusan desain maupun konten. Verifikasi akhir, pengisian konten yang akurat, dan pengujian fungsional/aksesibilitas tetap dilakukan secara manual oleh aku.

## AI Disclosure Tugas 3

AI membantu aku untuk memastikan fitur Create, Update, Delete, dan JSON serialization/deserialization pada model `Project` di aplikasi portofolio Django ini layak dan berfungsi dengan aman.

### Cakupan Bantuan AI

- AI membantu menyusun boilerplate kode awal: `ProjectForm` (ModelForm), fungsi `create_project`, `edit_project`, `delete_project`, `get_projects_json`, dan `show_projects` di `views.py`.
- AI membantu proses debugging berulang kali sepanjang pengerjaan: menganalisis pesan error Django (`OperationalError`, `NoReverseMatch`, `NameError: auth_views`, `NameError: login_required`) berdasarkan traceback yang aku laporkan, dan menunjukkan baris kode spesifik yang jadi penyebabnya.
- AI membantu merancang tampilan (glassmorphism) berdasarkan referensi visual yang aku berikan, dan menyesuaikan ulang beberapa kali sesuai revisi yang aku minta (warna, radius, alignment tombol).
- AI membantu menyusun struktur proteksi akses (`@login_required`, mengimplementasikan untuk sembunyiin tombol Add/Edit/Delete dari pengunjung yang belum login) sebagaimana yang aku bilang dan setelah itu aku sadar sendiri bahwa fitur create/delete awalnya bisa diakses siapa saja tanpa autentikasi.

### Keterbatasan AI yang Diidentifikasi

- **AI gabisa menjalankan atau melihat aplikasi aku secara langsung.** Semua debugging bergantung sepenuhnya pada informasi yang aku berikan — screenshot error page, isi file kode yang aku paste/upload, dan hasil pengamatan aku sendiri di browser. Ketika aku tidak memberikan detail yang cukup (misalnya struktur folder atau isi `urls.py`), AI gabisa menebak dengan akurat dan aku perlu menyediakan konteks tersebut secara aktif.
- **AI beberapa kali memberikan solusi yang ternyata tidak langsung cocok dengan struktur project aku**, misalnya penamaan context variable (`projects` vs `project_list`) dan penamaan field model (`tags`/`link` vs `tech_stack`/`project_url`) yang sempat tidak konsisten antar file. Ini baru ketahuan setelah aku membandingkan sendiri kode yang aku punya dengan target yang diberikan asdos.
- **AI tidak tahu kapan cache browser atau proses server menyebabkan perubahan tidak muncul.** Saat CSS/HTML yang sudah benar tetap terlihat sama di browser aku, AI hanya bisa memberikan kemungkinan penyebab (cache, `collectstatic`, session login yang masih aktif), aku sendirilah yang harus ngelakuin hard refresh, buka Incognito, dan ngecek DevTools untuk mastiin penyebab sebenarnya.

### Penyesuaian Manual yang Dilakukan

- aku ngejalanin `makemigrations` dan `migrate` sendiri, termasuk secara sadar memilih opsi "rename field" (bukan "hapus dan buat baru") saat Django menanyakan perubahan nama field `tags`→`tech_stack` dan `link`→`project_url`, supaya data yang sudah ada tidak hilang.
- aku menguji ulang setiap fitur secara manual di local server: mencoba alur create → edit → delete project, membuka `/api/projects/` untuk ngeverif format JSON, trus nguji proteksi login dengan membuka aplikasi lewat Incognito window untuk memastikan tombol Add/Edit/Delete benar-benar tersembunyi dari user yang belum login.
- aku yang mengidentifikasi sendiri celah keamanan bahwa fitur tambah/hapus project awalnya bisa diakses oleh siapa saja tanpa login, dan memikirkan untuk menambahkan proteksi akses.
- aku ngebaca dan ngelaporin traceback error Django secara spesifik di setiap error, yang menjadi dasar diagnosis perbaikan.
- aku mutusin sendiri pilihan desain visual (warna biru gelap-terang, gaya glassmorphism, radius tombol, penempatan foto) berdasarkan referensi visual yang aku cari sendiri.
- aku bikin akun `superuser` sendiri melalui `createsuperuser`, trus ngeverifikasi bahwa perilaku login/logout bekerja sesuai harapan di lokal.

### Kesimpulan

AI digunakan sebagai alat bantu untuk mempercepat penulisan boilerplate kode dan menjelaskan konsep teknis di balik implementasi Create, Update, Delete, dan JSON. Namun, seluruh proses pengujian, debugging berdasarkan observasi langsung di lingkungan saya sendiri, identifikasi celah keamanan, verifikasi kesesuaian dengan requirement tugas, dan pengambilan keputusan desain akhir tetap saya lakukan secara aktif dan mandiri. AI tidak memiliki akses langsung ke aplikasi saya, sehingga peran saya dalam menjalankan, menguji, dan memverifikasi setiap perubahan menjadi bagian yang tidak tergantikan dari keseluruhan proses pengerjaan tugas ini.

## AI Disclosure Tugas 4

AI membantu aku untuk mengimplementasikan sistem autentikasi, session/cookie (`last_login`), dan permission berbasis peran (anonymous, pengguna biasa, editor, superuser)

### Cakupan Bantuan AI

- AI membantu nyusun fungsi `register`, `login_user`, `logout_user` yang menggantikan `LoginView`/`LogoutView` bawaan Django, termasuk logic `set_cookie`/`delete_cookie` untuk `last_login`.
- AI membantu merancang mekanisme peran Editor lewat Django Group (`user.groups.filter(name="Editor").exists()`), termasuk membedakan `can_manage` (khusus superuser) dan `can_edit` (superuser + editor) di context view dan template.
- AI membantu menyusun CSS tombol Star.

### Keterbatasan AI yang Diidentifikasi

- **AI sempat salah nebak tipe data primary key `Project`.** AI mengasumsikan `Project.id` sudah UUID dan nulis `<uuid:project_id>` di `urls.py`, padahal di database aku ternyata masih integer biasa. Ini baru ketahuan setelah aku menjalankan aplikasinya sendiri dan mendapat error `NoReverseMatch`, lalu aku coba ubah yang dari `uuid` ke `int`.
- **AI melewatkan satu celah keamanan penting saat menambahkan peran Editor.** Saat nambahin pengecekan `is_superuser` untuk `edit_project`, AI gak sekaligus meriksa ulang `delete_project`, sehingga fungsi itu tetap cuma ngandelin `@login_required` tanpa cek `is_superuser`. Akibatnya, akun editor yang aku buat (`roisganteng`) ternyata masih bisa menghapus project nah bug ini aku temuin sendiri lewat pengujian manual langsung, bukan dikasih tau AI.
- **AI tidak tahu isi database aku secara langsung** (misalnya status `is_superuser` akun tertentu, atau apakah Group "Editor" sudah benar-benar dibuat) — semua verifikasi itu aku lakukan sendiri lewat Django Admin dan aku laporkan hasilnya ke AI.

### Penyesuaian Manual yang Dilakukan

- aku bikin Group "Editor" secara manual lewat Django Admin, dan nge-assign akun `roisganteng` ke group itu untuk keperluan testing.
- aku yang nemuin sendiri bug bahwa akun editor bisa menghapus project, lewat pengujian manual langsung (login sebagai editor, coba klik Delete), bukan dari analisis AI.
- aku ngejalanin `makemigrations` dan `migrate` sendiri untuk field `starred_by` yang baru ditambahkan.
- aku nguji tiap peran satu per satu secara manual: anonymous (redirect ke login), pengguna biasa (bisa star, tidak bisa edit/delete), editor (bisa edit, tidak bisa delete), dan superuser (bisa semua) lalu ngeverif tombol yang muncul/hilang sesuai peran di browser.
- aku ngelaporin traceback error secara spesifik dan lengkap di tiap kegagalan (`TemplateDoesNotExist`, `NoReverseMatch`, `ImportError`), yang jadi dasar AI mendiagnosis lokasi bug-nya.
- aku mutusin sendiri kapan pake pendekatan Group dibanding Permission Django untuk peran Editor, dan memutuskan tombol Delete disembunyikan total dari editor di UI (bukan cuma dibiarin menghasilkan 403).

### Kesimpulan

AI digunakan sebagai alat bantu untuk mempercepat penulisan kode autentikasi, dan permission berbasis peran, sekaligus membantu menjelaskan konsep di baliknya (session, cookie, CSRF, Group vs Permission). Namun, verifikasi tiap peran, pengujian manual di browser, identifikasi bug keamanan penting (celah delete pada editor), serta pengambilan keputusan akhir soal desain otorisasi tetap aku lakukan sendiri secara aktif. AI juga terbukti gak selalu benar di awal seperti contohnya ada celah keamanan yg dimana editor bisa menghapus projek, sehingga peran aku dalam menguji dan memvalidasi setiap perubahan menjadi bagian penting yang tidak bisa digantikan oleh AI.

## AI Disclosure Tugas 5

AI membantu aku untuk menyelesaikan Tugas 5, khususnya pada bagian memastikan perlindungan XSS pada aplikasi portofolio Django ini. Struktur dasar halaman Projects (fetch, search debounce, modal popover, toast.js) aku bangun sendiri mengikuti tutorial PBP, lalu AI membantu menjelaskan flow web portofolio aku yang sekarang.

### Cakupan Bantuan AI

- AI membantu menemukan penyebab error `OperationalError: no such table: main_project_starred_by` dan mengarahkan aku untuk menjalankan `migrate` di database lokal.
- AI membantu menambahkan lapisan perlindungan XSS tambahan (`isSafeUrl()` untuk memvalidasi skema URL sebelum dirender sebagai `href`/`src`), serta memverifikasi bahwa `escapeHtml()` sudah dipasang di semua field dinamis.
- AI membantu mengganti `confirm()` bawaan browser pada tombol Delete dengan modal glassmorphism yang sudah ada di tema, supaya UX-nya konsisten.

### Keterbatasan AI yang Diidentifikasi

- **AI mengulangi kesalahan yang sama soal asumsi nama field.** Setelah sebelumnya salah asumsi `Project.id` berupa UUID, AI lagi-lagi salah asumsi field model bernama `tech_stack`/`project_url`, padahal nama aslinya `tags`/`link`. Ini baru ketahuan pas aku buka `/api/projects/` sendiri dan ngebandingin field JSON yang sebenarnya dengan kode JavaScript-nya.
- **AI tidak bisa menjalankan aplikasi atau membuka DevTools sendiri.** Semua diagnosis (traceback, isi `innerHTML` kartu project, hasil `/api/projects/`) bergantung sepenuhnya pada aku yang harus mencari tahu sendiri error pada link dan tags yang tidak muncul di card project.
- **AI sempat tidak menyadari ada kode mati (dead code) dan duplikasi fungsi `escapeHtml`** di `projects.html` aku baru sadar bahwa ada dua fungsi escapeHtml dan itu bikin aku keinget bahwa fungsi escapeHtml yang satunya adalah bekas kode lama.

### Penyesuaian Manual yang Dilakukan

- aku nulis sendiri `create_project_ajax`, termasuk validasi `ModelForm`, response JSON dengan status 201/400/403, dan pengecekan `is_superuser` di server bukan hasil generate AI.
- aku ngejalanin `migrate` sendiri untuk memperbaiki tabel `starred_by` yang belum ada di database lokal.
- aku ngelakuin debugging manual lewat DevTools: membuka tab Console untuk mengecek `innerHTML` kartu project, membuka tab Network untuk memverifikasi debouncing search benar-benar mengirim satu request setelah berhenti mengetik, dan membuka `/api/projects/` langsung untuk membandingkan nama field JSON dengan kode JavaScript.
- aku ngelakuin pengujian XSS manual: nyobain payload kaya `<img src=x onerror=alert('XSS')>` dan `javascript:alert('XSS')` di field title dan link, termasuk menggunakan Django shell untuk lewatin validasi form pas pengen nguji proteksi `isSafeUrl()` secara spesifik.
- aku uji ulang halaman Projects di jendela Incognito untuk memastikan bug yang dilaporkan bukan karena cache browser, sebelum lanjutin debugging lebih dalam.

### Kesimpulan

AI kebanyakan ngebantuin aku dalam proses debugging di Tugas 5 ini, terutama buat error yang traceback-nya rumit. Tapi, implementasi inti seperti `create_project_ajax` aku tulis sendiri, dan hampir semua bug yang ditemukan baru bisa didiagnosis setelah aku ngelakuin investigasi manual dulu (buka DevTools, ngecek `/api/projects/`, jalanin migrasi, uji di Incognito). AI sendiri terbukti beberapa kali salah asumsi soal struktur data di proyekku, sehingga peran aku dalam ngeverifikasi setiap klaim AI dengan bukti nyata dari browser dan terminal menjadi bagian yang tidak tergantikan dari proses pengerjaan tugas ini.