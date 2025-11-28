import streamlit as st
import os
from groq import Groq

# 1. Konfigurasi Halaman (Simpel & Minimalis)
st.set_page_config(
    page_title="AI Chat",
    page_icon="⚫",
    layout="centered" # Posisi di tengah biar fokus
)

# 2. Custom CSS untuk memaksa tema Hitam-Putih (Monokrom)
st.markdown("""
<style>
    /* Hapus garis dekorasi warna di bagian atas */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
    /* Sembunyikan elemen menu hamburger & footer bawaan */
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    /* Paksa tombol jadi hitam putih */
    .stButton>button {
        color: white;
        background-color: black;
        border: 1px solid white;
    }
    .stButton>button:hover {
        color: black;
        background-color: white;
        border: 1px solid black;
    }
    /* Hapus footer "Made with Streamlit" biar bersih */
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. Judul Simpel
st.title("⚫ AI Chat")
st.write("---") # Garis pembatas simpel

# 4. Setup Client Groq
# Mengambil API Key dari Secrets Hugging Face
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ API Key belum dimasukkan di Settings > Secrets!")
    st.stop()

client = Groq(api_key=api_key)

# 5. Inisialisasi Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 6. Tampilkan Chat Sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. Input Chat User
if prompt := st.chat_input("Ketik pesan..."):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate jawaban dari Groq
    with st.chat_message("assistant"):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                model="llama-3.3-70b-versatile",
                stream=True,
            )

            # Helper function: Mengambil teks murni dari respon Groq yang ribet
            def parse_stream(stream):
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content

            # Tulis stream yang sudah bersih
            response = st.write_stream(parse_stream(chat_completion))
            
            # Simpan jawaban assistant
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error: {e}")
