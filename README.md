🛡️ QwenGuard Demo: AI Chat & Image Generator

    Aplikasi Chatbot AI bergaya Brutalis (Monokrom) dengan kemampuan percakapan cerdas dan generasi gambar otomatis.

Proyek ini dibangun dengan fokus utama pada efisiensi biaya (zero-cost infrastructure) dan kecepatan inferensi tinggi. Menggabungkan kekuatan LLM untuk teks dan Stable Diffusion untuk visual dalam antarmuka yang minimalis.

🔗 Live Demo: (https://okitarung-qwenguard-demo-01.hf.space/)

✨ Fitur Utama

    ⚡ Cerdas & Cepat: Menggunakan model Llama-3.3-70b-versatile melalui Groq LPU untuk respons teks dengan latensi super rendah (blazing fast).

    🎨 Image Generation: Mampu membuat gambar secara otomatis berdasarkan konteks percakapan menggunakan integrasi Pollinations.ai.

    s 🖤 UI Brutalis: Antarmuka pengguna (UI) bertema hitam-putih yang simpel, estetis, dan fokus sepenuhnya pada konten.

    💸 Zero-Cost Architecture: Seluruh stack teknologi menggunakan layanan tier gratis (Hugging Face Spaces, Groq Free Tier, & Pollinations).

🏗️ Arsitektur Sistem

Aplikasi ini menggunakan pendekatan Serverless Inference yang memisahkan antarmuka pengguna (Frontend) dari logika pemrosesan AI (Backend Intelligence).

Diagram Alur Data

Cuplikan kode

sequenceDiagram
    participant User as 👤 Pengguna
    participant App as 🖥️ Streamlit (Hugging Face)
    participant Brain as 🧠 Groq API (Llama 3.3)
    participant Painter as 🎨 Pollinations.ai

    Note over User, App: Frontend Layer
    User->>App: Input: "Buatkan gambar kucing cyberpunk"

    Note over App, Brain: Logic Layer
    App->>App: Tambahkan System Prompt (Instruksi Rahasia)
    App->>Brain: Kirim Chat History + Prompt

    Note over Brain: AI Processing
    Brain-->>App: Respon: "IMAGE_GEN: A cyberpunk cat neon..."

    Note over App, Painter: Image Generation Layer
    App->>App: Parsing Respon (Cek prefix 'IMAGE_GEN:')

    alt Jika Terdeteksi Perintah Gambar
        App->>Painter: Request via URL (GET /prompt/...)
        Painter-->>App: Return Image Stream
        App->>User: Render Gambar & Caption
    else Jika Teks Biasa
        App->>User: Tampilkan Teks Chat Biasa
    end

Penjelasan Komponen

    Frontend (Hugging Face Space):

        Dibangun menggunakan Python Streamlit.

        Berfungsi sebagai controller yang mengatur sesi percakapan dan antarmuka pengguna.

        Memiliki logika routing untuk mendeteksi apakah AI mengirimkan teks biasa atau kode perintah gambar (format: IMAGE_GEN:).

    AI Brain (Groq Cloud):

        Menggunakan model Llama-3.3-70b.

        Tidak memproses gambar secara pixel, melainkan menghasilkan Prompt Engineering yang presisi untuk diteruskan ke generator gambar.

    Image Engine (Pollinations.ai):

        Layanan API terbuka untuk Stable Diffusion.

        Menerima prompt via URL dan merender gambar secara real-time tanpa memerlukan API Key otentikasi.

🚀 Cara Menjalankan di Lokal

Ikuti langkah ini jika Anda ingin menjalankan proyek di komputer Anda sendiri:

1. Clone Repository

Bash

git clone https://github.com/okitarung/QwenGuard-Demo.git
cd QwenGuard-Demo

2. Install Dependencies

Pastikan Python sudah terinstall, kemudian jalankan:
Bash

pip install -r requirements.txt

3. Setup API Key

Anda memerlukan API Key dari Groq (Gratis). Dapatkan di console.groq.com.

Cara Aman (Disarankan untuk Streamlit): Buat file bernama .streamlit/secrets.toml di dalam folder proyek:
Ini, TOML

# .streamlit/secrets.toml
GROQ_API_KEY = "gsk_..."

Alternatif (Environment Variable):

    Linux/Mac: export GROQ_API_KEY="gsk_..."

    Windows (PowerShell): $env:GROQ_API_KEY="gsk_..."

4. Jalankan Aplikasi

Bash

streamlit run app.py

Aplikasi akan berjalan di http://localhost:8501.

🛠️ Teknologi yang Digunakan

Komponen	Teknologi	Fungsi
Frontend	Streamlit	Framework UI Python interaktif
Inference	Groq (LPU)	Platform inferensi AI tercepat
Model	Llama 3.3 70B	Large Language Model (LLM)
Image Gen	Pollinations.ai	Generator gambar Open Source
Hosting	Hugging Face	Hosting aplikasi gratis

📝 Lisensi

Proyek ini didistribusikan di bawah lisensi Apache 2.0. Bebas untuk dimodifikasi, didistribusikan ulang, dan digunakan untuk keperluan pribadi maupun komersial.
