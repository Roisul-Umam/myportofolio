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
- [ ] Menambahkan animasi pada web
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

## AI Disclosure Tugas 1&2

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