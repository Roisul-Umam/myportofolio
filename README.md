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

## Struktur Folder
mypoirtofolio/
├── portofolio/                 
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── rois.jpg
├── templates/
│   └── index.html
├── venv/
├── .env
├── .env.prod
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt

## Fitur
- **Profile Section** — Menampilkan foto, biodata singkat, NPM, program studi, dan link sosial media (GitHub, LinkedIn, Email).
- **Skills & Projects Section** — Menampilkan daftar skill teknis dalam bentuk tag, serta project-project yang pernah dikerjakan dalam bentuk card.
- **Responsive Design** — Layout menyesuaikan otomatis untuk mobile dan desktop menggunakan CSS Grid dan media query.

## Rencana Pengembangan (Roadmap)
- [ ] Menambahkan section "Experience" atau "Education"
- [ ] Menambahkan animasi pada web
- [ ] Menghubungkan form kontak yang langsung terkirim ke hp lewat aplikasi buatan

## Author
**Rois (Roisul Umam)**
NPM: 2506620210
S1 Ilmu Komputer, Fakultas Ilmu Komputer, Universitas Indonesia
- GitHub: [@Roisul-Umam](https://github.com/Roisul-Umam)
- LinkedIn: [Roisul Umam](https://www.linkedin.com/in/roisul-umam-83577b302/?locale=en)
- Email: umamr545@gmail.com

### Tugas 1

1. Yap saya menggunakan elemen semantik seperti artikel, header dll dalam merancang website portofolio ini, karena ini membuat kode saya itu lebih terstruktur dan mudah dibaca oleh kita sebagai manusia.
2. Selama saya membangun website ini, saya tidak menemukan tantangan tata letak ukuran ketika berpindah ke mobile, tetapi jika hal itu terjadi, saya akan segera menggunakan CSS grid/flexbox agar elemennya bisa menumpuk kebawah ketika dibuka di layar yg vertical.
3. Batasan yang paling saya alami pada website static ini adalah tidak adanya backend. Feedback system adalah fitur yang saya sangat ingin tambahkan pada website ini, namun ketidak adaannya datebase membuat hal ini tidak bisa terjadi karena tidak adannya sistem penyimpanan data secara real time.

## AI Disclosure

Bagian *"Skills & Projects"* pada portofolio ini dikembangkan dengan bantuan AI assistant (Claude, Anthropic) untuk mempercepat proses penulisan HTML dan CSS awal.

### Cakupan Bantuan AI
- AI digunakan untuk menghasilkan struktur HTML section baru (skills tags dan project cards).
- AI digunakan untuk menghasilkan styling CSS yang konsisten dengan desain hero section yang sudah ada sebelumnya (warna, radius, font, spacing).

### Keterbatasan AI yang Diidentifikasi
Beberapa keterbatasan yang disadari dari hasil AI dan perlu ditinjau ulang secara manual:

1. Konten placeholder, bukan konten nyata. AI tidak memiliki akses ke daftar project atau skill saya yang sebenarnya, sehingga nama project, deskripsi, dan tag teknologi yang dihasilkan masih berupa contoh generik (misalnya "Nama Project 1", deskripsi template). Ini wajib diganti manual dengan data project asli.
2. AI melakukan hardcoding, bukan solusi dinamis. Pada iterasi pertama, AI menghasilkan setiap item skill dan project card secara statis langsung di HTML/template (`<li>Python</li>`, `<article class="project-card">...</article>` ditulis berulang satu per satu).
3. Tidak memahami konteks personal/preferensi desain secara utuh. AI meniru pola desain yang sudah ada (warna aksen, border tipis, radius kecil) berdasarkan analisis kode CSS yang diberikan, tapi tidak punya "selera" — keputusan akhir soal apakah gaya visual ini cocok tetap ada di tangan saya.

### Penyesuaian Manual yang Dilakukan
- Mengganti seluruh konten placeholder project dengan data project asli (nama, deskripsi, tech stack, link repo).
- Menyesuaikan jumlah dan urutan skill sesuai kemampuan yang benar-benar saya kuasai.
- Melakukan pengecekan tampilan di beberapa ukuran layar (mobile, tablet, desktop) dan memperbaiki [sebutkan bagian yang diperbaiki, misal: spacing pada mobile / warna kontras tag].
- Me-refactor konten yang sebelumnya di-hardcode di HTML (bio, skills, projects) menjadi data yang dikirim dari `views.py` sebagai context, lalu ditampilkan di template menggunakan Django template tag (`{{ }}` dan `{% for %}`).
- Menyesuaikan struktur dict di `views.py` dengan data project dan skill saya yang sebenarnya.

### Kesimpulan
AI digunakan sebagai alat bantu untuk mempercepat proses coding (*scaffolding* HTML/CSS) dan mengimplementasikan algoritma yang telah saya buat sebelumnya, bukan sebagai pengganti proses berpikir dan pengambilan keputusan desain maupun konten. Verifikasi akhir, pengisian konten yang akurat, dan pengujian fungsional/aksesibilitas tetap dilakukan secara manual oleh saya.

Nama : Roisul Umam

NPM : 2506620210

Kelas : PBP F