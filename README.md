⚫ QwenGuard Demo: AI Chat & Image Generator

Sebuah aplikasi Chatbot AI bergaya Brutalis (Monokrom) yang mampu melakukan percakapan teks cerdas dan menghasilkan gambar secara otomatis. Proyek ini dibangun dengan fokus pada efisiensi biaya (zero-cost infrastructure) dan kecepatan inferensi tinggi.

🔗 Live Demo:https://okitarung-qwenguard-demo-01.hf.space/

✨ Fitur Utama

Cerdas & Cepat: Menggunakan model Llama-3.3-70b-versatile melalui Groq LPU untuk respon teks super cepat (latency rendah).

Image Generation: Mampu membuat gambar berdasarkan deskripsi teks menggunakan integrasi Pollinations.ai.

UI Brutalis: Antarmuka pengguna (UI) hitam-putih yang simpel, bersih, dan fokus pada konten.

Zero-Cost Architecture: Seluruh stack teknologi menggunakan layanan tier gratis (Hugging Face Spaces, Groq Free Tier, Pollinations).

🏗️ Arsitektur Sistem

Aplikasi ini menggunakan pendekatan Serverless Inference yang memisahkan antarmuka pengguna (Frontend) dari logika pemrosesan AI (Backend Intelligence).

Diagram Alur Data

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

Memiliki logika routing untuk mendeteksi apakah AI mengirimkan teks biasa atau kode perintah gambar (IMAGE_GEN:).

AI Brain (Groq Cloud):

Menggunakan model Llama-3.3-70b.

Tidak memproses gambar secara langsung, melainkan menghasilkan Prompt Engineering yang diteruskan ke generator gambar.

Image Engine (Pollinations.ai):

Layanan API terbuka untuk Stable Diffusion.

Menerima prompt via URL dan merender gambar secara real-time tanpa memerlukan API Key otentikasi.

🚀 Cara Menjalankan di Lokal

Jika Anda ingin menjalankan proyek ini di komputer Anda sendiri:

1. Clone Repository

git clone [https://github.com/okitarung/QwenGuard-Demo.git](https://github.com/okitarung/QwenGuard-Demo.git)
cd QwenGuard-Demo


2. Install Dependencies

Pastikan Anda sudah menginstall Python, lalu jalankan:

pip install -r requirements.txt


3. Setup API Key

Dapatkan API Key gratis di console.groq.com.

Linux/Mac: export GROQ_API_KEY="gsk_..."

Windows (Powershell): $env:GROQ_API_KEY="gsk_..."

Alternatif: Buat file .env (jika menggunakan python-dotenv) atau hardcode sementara untuk testing (tidak disarankan).

4. Jalankan Aplikasi

streamlit run app.py


Aplikasi akan berjalan di http://localhost:8501.

🛠️ Teknologi yang Digunakan

Streamlit - Framework Frontend Python.

Groq - Platform Inferensi AI Tercepat (LPU).

Hugging Face Spaces - Hosting Aplikasi Gratis.

Pollinations.ai - Open Source Image Generation.

📝 Lisensi

Proyek ini didistribusikan di bawah lisensi Apache 2.0. Bebas untuk dimodifikasi dan didistribusikan ulang.
