# NadaAI

**NadaAI** adalah sebuah platform AI yang dikembangkan sebagai proyek mata kuliah **Deep Learning** pada semester 7. Proyek ini bertujuan untuk melestarikan budaya Indonesia dengan memanfaatkan kecerdasan buatan.

NadaAI mampu **memprediksi alat musik tradisional Indonesia** (seperti Angklung, Gamelan, Sape, dan Seruling) melalui analisis suara. Sistem ini dilatih menggunakan dataset audio yang komprehensif untuk mengidentifikasi karakteristik unik dari setiap alat musik.

## Fitur Utama

-   **Prediksi Nada:** Unggah file audio dan dapatkan prediksi alat musik tradisional secara instan.
-   **Jelajah Musik:** Bagian yang mungkin menampilkan informasi detail atau koleksi audio dari alat musik yang didukung.
-   **Nada Quiz:** Fitur interaktif untuk menguji pengetahuan pengguna tentang alat musik tradisional.
-   **Informasi dan Dataset:** Menyediakan informasi lebih lanjut mengenai proyek serta dataset yang digunakan untuk pelatihan model.

## Teknologi yang Digunakan

-   **Flask:** Framework web Python untuk membangun server aplikasi.
-   **TensorFlow:** Digunakan untuk melatih dan menjalankan model Deep Learning.
-   **Librosa:** Pustaka Python untuk analisis audio dan pemrosesan sinyal.
-   **NumPy & Scikit-image:** Pustaka pendukung untuk komputasi numerik dan pemrosesan gambar (untuk mengubah spectrogram menjadi format yang sesuai untuk model).
-   **Python:** Bahasa pemrograman utama yang digunakan.

## Cara Instalasi

Untuk menjalankan proyek ini, pastikan Anda memiliki **Python versi 3.11** atau yang lebih tinggi terinstal.

1.  **Instalasi Pustaka:**
    Buka terminal dan instal semua pustaka yang dibutuhkan dengan perintah berikut:

    ```bash
    pip install Flask tensorflow librosa numpy scikit-image
    ```

    Jika Anda memiliki beberapa versi Python, gunakan perintah yang lebih spesifik:

    ```bash
    py -3.11 -m pip install Flask tensorflow librosa numpy scikit-image
    ```

2.  **Jalankan Aplikasi:**
    Setelah semua pustaka terinstal, jalankan aplikasi Flask:

    ```bash
    python app.py
    ```

    Atau, jika Anda ingin memastikan menggunakan versi Python 3.11:

    ```bash
    py -3.11 app.py
    ```

3.  **Akses Platform:**
    Buka browser Anda dan kunjungi alamat yang ditampilkan di terminal, biasanya `http://127.0.0.1:5000/`.


## Kontributor
- Zulkarnain - Front End
- Devina - Back End
    
