# Scrape-Glints
![image](https://github.com/rizkialifah/Scrape-Glints/assets/50816275/e56b5628-21c7-4872-bb1b-9ad228f27eb7)

# Scraping web data automation (glints)
Github pada halaman ini berisi tugas akhir praktikum Mata Kuliah Manajemen Data Statistika, Program Studi Pascasarjana Statistika dan Sains Data dengan topik Web Scraping & Crawling pada situs https://glints.com/id/opportunities/jobs/explore?keyword=statistika&country=ID&locationName=Indonesia . Program scraping dilakukan menggunakan bantuan software Python dan hasilnya disimpan pada MongoDB Atlas setiap 2 jam sekali menggunakan github action dan hasil tabel scraping dapat di ekstrak melalui program python setiap selesai ter-scraping. 

Dikarenakan penyimpanan menggunakan mongoDB Atlas yang bersifat free dan ada batasan memory penyimpanan pada cluster yang dibuat maka program automasi scraping menggunakan python dan mongoDB pada github ini hanya menampilkan 2 informasi  yaitu nama lowongan pekerjaan dan perusahaan nya. Namun, program ini dapat dikembangkan dengan menambahkan informasi lain yang ada pada laman https://glints.com sesuai dengan kebutuhan informasi yang ingin didapatkan dan tentunya harus disesuaikan dengan element ataupun class pada website tersebut pada saat men-scrapping.

# Scraping Flow
Seluruh proses scraping dilakukan oleh main.py. Untuk lebih detailnya bagaimana program ini berjalan, berikut alurnya :

1. Panggil seluruh paket yang dibutuhkan untuk program scraping.
2. Siapkan kontainer pada program (tujuan nya untuk menaruh list data hasil scrap sebelum di ubah kedalam bentuk tabel).
3. Program akan masuk ke halaman glints.
4. Lalu, akan masuk ke spesifik URL. Pada studi kasus ini ingin melihat lowongan pekerjaan jurusan statistik di website glints, sehingga ini akan mengarahkan ke halaman pencarian https://glints.com/id/opportunities/jobs/explore?keyword=statistika&country=ID&locationName=Indonesia.
5. Sebelum mendapatkan data pekerjaan, akan dilakukan pengecekan halaman terlebih dahulu apakah hanya 1 halaman atau lebih. Pada proses ini, webdriver akan terus men-scroll ke bawah hingga mendapatkan halaman maksimum yang ada pada website.
6. Program akan mengambil informasi sesuai dengan apa yang telah di program hingga halaman terakhir (pada kasus ini hanya mengambil informasi nama lowongan dan perusahaan).
7. Jika semua halaman sudah dikunjungi, maka proses scraping selesai.
8. Hasil scrape kemudian akan dibentuk menjadi table dengan bantuan pandas dataframe pada python.
9. Hasil dapat di save dan akan otomatis tersimpan pada file yang sama pada saat program berjalan dalam format CSV dan dapat dilakukan analisis lebih lanjut.
10. Untuk mencegah terjadinya data yang hilang pada file lokal, hasil scrape dapat di simpan pada MongoDB Atlas dengan mengubah terlebih dahulu struktur file menjadi bentuk dictionary.
11. File dapat otomatis ter-upload ke mongoDB pada database cluster yang telah dibuat.

# Struktur Dokumen
Berikut ini merupakan contoh struktur dokumen hasil scraping yang ter-upload pada MongoDB Atlas :
<img width="909" alt="image" src="https://github.com/rizkialifah/Scrape-Glints/assets/50816275/cf806bf0-6e02-4eb8-9991-f46c78522dea">

# Scrapping Output
Program ini secara otomatis akan menghasilkan output berupa tabel file csv yang akan disimpan di dalam direktori yang sama dengan program yang berjalan dengan nama LokerData.csv. Jika ingin memeriksa isi file dapat dilihat pada bagian github yang bertuliskan LokerData.csv.

# Penulis
Nama  : Rizki Alifah Putri

NIM   : G1501221005


