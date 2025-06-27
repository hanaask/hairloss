import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.graph_objects as go
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="🌸 Hair Loss Predictor", layout="wide")

# Inisialisasi halaman pertama kali
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# Fungsi ganti halaman
def change_page(pilihan):
    st.session_state.page = pilihan
    st.query_params.update({"page": pilihan})

# Tangkap dari URL jika ada
params = st.query_params
if "page" in params:
    st.session_state.page = params["page"]

# Load model
with open('model_kerontokan.pkl', 'rb') as file:
    model = pickle.load(file)

# Sidebar styling
st.markdown("""
    <style>
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        padding: 10px 20px;
        color: white;
        background-color: #111827;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .nav-btn {
        padding: 12px 20px;
        margin: 5px 10px;
        border-radius: 8px;
        font-size: 16px;
        background-color: #1f2937;
        color: white;
        border: none;
        width: 100%;
        text-align: left;
    }
    .nav-btn:hover {
        background-color: #4c1d95;
        cursor: pointer;
    }
    .nav-selected {
        background-color: #a855f7 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Navigasi Sidebar
nav_options = {
    "Beranda": "🏠",
    "Info Kerontokan Rambut": "💡",
    "Prediksi": "🧪",
    "Pencegahan": "🛡️"
}

with st.sidebar:
    logo = Image.open("logo1.png")
    st.image(logo, use_container_width=True)
    st.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)
    for label, icon in nav_options.items():
        btn_class = "nav-btn nav-selected" if st.session_state.page == label else "nav-btn"
        if st.button(f"{icon} {label}", key=label):
            change_page(label)

selected = st.session_state.page

# ================== HALAMAN KONTEN ==================

if selected == "Beranda":
    st.markdown("""
    <div style="padding:10px;border-radius:10px;">
    <marquee style='color:deeppink;font-size:35px;font-weight:bold;'>
        🌟Selamat Datang Di Aplikasi Prediksi Kerontokan Rambut By HanaSK🌟
    </marquee>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("beranda.png", use_container_width=True)
    st.markdown("""
    <div style='text-align: center; font-size:18px; color: #f0f0f0; line-height: 1.7;'>
    🔍 <b>Ingin tahu seberapa sehat rambutmu?</b><br>
    Saatnya prediksi dari sekarang <span style='color:#ff66cc;font-weight:bold;'>risiko kerontokan rambut</span> sebelum terlambat! 🌿<br><br>
    Aplikasi ini akan membantu Anda <b>memprediksi risiko kerontokan rambut</b> sejak dini<br>
    melalui analisis <i>data kesehatan dan gaya hidup</i> menggunakan <span style='color:#00FF99;font-weight:bold;'>XGBoost</span> — mesin cerdas yang siap bantu kamu tampil percaya diri lagi! ✨
    </div>
    """, unsafe_allow_html=True)
    
elif selected == "Info Kerontokan Rambut":
    st.title("💡 Info Lengkap Tentang Kerontokan Rambut")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("info1.png", width=500)

    st.markdown("### 📌 Apa itu Kerontokan Rambut?")
    st.markdown("""
    Kerontokan rambut adalah kondisi yang sangat umum dialami oleh pria maupun wanita.  
    Normalnya, seseorang dapat kehilangan **50–100 helai rambut per hari** sebagai bagian dari siklus alami pertumbuhan rambut.  
    Namun, jika jumlahnya melebihi angka tersebut dan terjadi secara terus-menerus, itu bisa menjadi tanda adanya masalah kesehatan.
    """)

    with st.expander("💾 Jenis-Jenis Kerontokan Rambut"):
        st.markdown("""
        - **Androgenetic Alopecia**: Kerontokan genetik, umum pada pria & wanita.
        - **Telogen Effluvium**: Kerontokan akibat stres berat, demam, atau perubahan hormonal.
        - **Alopecia Areata**: Rambut rontok berbentuk bulat akibat gangguan autoimun.
        - **Traction Alopecia**: Kerontokan karena menarik rambut terlalu kencang (kuncir, kepang).
        """)

    
    with st.expander("🧠 Penyebab Umum Kerontokan Rambut"):
        st.markdown("""
        <table style='width:100%; font-size: 14px; line-height: 1.5; border-collapse: collapse;'>
          <tr><td><b>Stres Berlebih</b></td><td>Dapat mengganggu siklus pertumbuhan rambut dan mempercepat kerontokan.</td></tr>
          <tr><td><b>Anemia</b></td><td>Kekurangan zat besi dan darah menyebabkan folikel rambut kekurangan oksigen.</td></tr>
          <tr><td><b>Gangguan Tidur / Insomnia</b></td><td>Mengganggu regenerasi sel rambut dan metabolisme tubuh.</td></tr>
          <tr><td><b>Penyakit Kronis</b></td><td>Seperti lupus, tiroid, atau alopecia menyebabkan kerontokan sistemik.</td></tr>
          <tr><td><b>Penggunaan Produk Rambut Tertentu</b></td><td>Bahan seperti sulfat dan paraben dapat merusak folikel rambut.</td></tr>
          <tr><td><b>Pola Makan Tidak Seimbang</b></td><td>Kurangnya asupan protein, vitamin, dan mineral penting untuk pertumbuhan rambut.</td></tr>
          <tr><td><b>Faktor Genetik</b></td><td>Riwayat keluarga dengan kebotakan meningkatkan risiko kerontokan.</td></tr>
          <tr><td><b>Kebiasaan Begadang</b></td><td>Jam tidur kurang dari 6–7 jam dapat mengganggu produksi hormon pertumbuhan rambut.</td></tr>
          <tr><td><b>Kualitas Air</b></td><td>Air berkapur atau berkeruh dapat merusak kulit kepala dan folikel rambut.</td></tr>
        </table>
        """, unsafe_allow_html=True)

    with st.expander("🔍 Tanda-Tanda Kerontokan Tidak Normal"):
        st.markdown("""
        - Rambut rontok dalam jumlah banyak saat disisir/keramas
        - Penipisan rambut terlihat jelas di area tertentu
        - Muncul kebotakan berbentuk bulat
        - Rambut sulit tumbuh kembali setelah rontok
        """)

elif selected == "Pencegahan":
    st.markdown("""
    <h2 style='text-align: center; color: deeppink;'>💡 Tips Pencegahan Kerontokan Rambut 💡</h2>
    <table style='width:100%; font-size: 18px; line-height: 1.7; border-collapse: collapse;'>
      <tr><td style='padding: 10px;'>🥗 <b>Konsumsi Makanan Bergizi</b></td><td style='padding: 10px;'>Protein, zat besi, vitamin: <span style='color:mediumseagreen'><b>bayam, telur, ikan</b></span>.</td></tr>
      <tr><td style='padding: 10px;'>🔥 <b>Hindari Styling Panas</b></td><td style='padding: 10px;'>Batasi penggunaan catokan, hair dryer, dll. <span style='color:red'><b>Merusak batang rambut!</b></span></td></tr>
      <tr><td style='padding: 10px;'>🧴 <b>Gunakan Produk Tepat</b></td><td style='padding: 10px;'>Hindari sulfat & paraben. Gunakan sampo sesuai jenis rambut.</td></tr>
      <tr><td style='padding: 10px;'>🧘‍♀️ <b>Kelola Stres</b></td><td style='padding: 10px;'>Relaksasi, journaling, olahraga untuk menyeimbangkan hormon.</td></tr>
      <tr><td style='padding: 10px;'>🛌 <b>Tidur Cukup</b></td><td style='padding: 10px;'>Minimal 7 jam/hari untuk regenerasi sel & pertumbuhan rambut.</td></tr>
    </table>
    """, unsafe_allow_html=True)

elif selected == "Prediksi":
    st.title("💇‍♀️✨ Prediksi Rambut Rontok ✨💇‍♀️")
    st.markdown("Isi data kamu untuk cek risiko kerontokan rambut 🎀🧴")

    usia = st.number_input("🎂 Berapa Usia Anda?", value=25, step=1)
    
    jenis_kelamin = st.selectbox("🚻 Apa Jenis Kelamin Anda?", ["Laki-laki", "Perempuan"])
    jenis_kelamin_val = 1 if jenis_kelamin == "Laki-laki" else 0

    genetik = st.selectbox("🧬Apakah Anda Memiliki Genetik Rambut Rontok?", ["iya", "tidak"])
    genetik_val = 1 if genetik == "iya" else 0

    penyakit = st.selectbox("💊 Apakah Anda Memiliki Penyakit Kronis?", ["iya (Alopecia, Tyroid, Lupus, dll)", "tidak"])
    penyakit_val = 1 if "iya" in penyakit else 0

    begadang = st.selectbox("🌙 Seberapa Sering Anda Begadang?", [
        "Sangat Sering Begadang",
        "Sering Begadang",
        "Kadang-kadang Begadang",
        "Tidak Begadang"
    ])
    begadang_val = {
        "Sangat Sering Begadang": 1,
        "Sering Begadang": 2,
        "Kadang-kadang Begadang": 0,
        "Tidak Begadang": 3
    }[begadang]

    st.caption("""
    📌 **Keterangan Seberapa Sering Begadang:**  
    - **Sangat Sering Begadang** → jam tidur kurang dari 2 jam  
    - **Sering Begadang** → jam tidur 3–5 jam  
    - **Kadang-kadang Begadang** → jam tidur 5–6 jam  
    - **Tidak Begadang** → jam tidur ≥ 7 jam
    """)

    gangguan_tidur = st.selectbox("😴 Apakah Anda Memiliki Gangguan Tidur?", ["Insomnia", "Tidak Ada Gangguan Tidur"])
    gangguan_tidur_val = 0 if gangguan_tidur == "Insomnia" else 1
    
    air = st.selectbox("🚿 Bagimana Kualitas Air Di Lingkungan Anda?", [
        "Air Berkapur",
        "Air Bersih"
    ])
    air_val = {
        "Air Berkapur": 0,
        "Air Bersih": 1
    }[air]

    produk_rambut = st.selectbox("🧴 Apa Kandungan Produk Rambut Anda?", [
        "Mengandung Sulfat",
        "Tidak menggunakan produk rambut"
    ])
    produk_rambut_val = {
        "Mengandung Sulfat": 0,
        "Tidak menggunakan produk rambut": 1
    }[produk_rambut]


    anemia = st.selectbox("🩸Apakah Anda Memiliki Riwayat Anemia?", [
        "Anemia berat", "Anemia sedang", "Anemia Ringan", "Tidak ada anemia"
    ])
    anemia_val = {
        "Anemia berat": 0,
        "Anemia Ringan": 1,
        "Anemia sedang": 2,
        "Tidak ada anemia": 3
    }[anemia]

    st.caption("""
    📌 **Keterangan Anemia (g/dL):**  
    - **Ringan**: 10 g/dL hingga batas normal terendah  
    - **Sedang**: 8 – 10 g/dL  
    - **Berat**: 6.5 – 7.9 g/dL
    """)

    stres = st.selectbox("😣 Seberapa Tingkat Stres Anda?", ["High", "Low", "Moderate"])
    stres_val = {"High": 0, "Low": 1, "Moderate": 2}[stres]

    makan = st.selectbox("🍔 Bagaimana Kebiasaan Makan Anda Sehari-hari?", [
        "Bernutrisi", "Ketergantungan Makanan Cepat Saji", "Seimbang atau Keduanya"
    ])
    makan_val = {
        "Bernutrisi": 1,
        "Ketergantungan Makanan Cepat Saji": 0,
        "Seimbang atau Keduanya": 2
    }[makan]

    st.markdown("</div>", unsafe_allow_html=True)

    # ✅ Gabungkan input jadi DataFrame
    input_data = pd.DataFrame([{
    "Usia": usia,
    "Jenis_Kelamin": jenis_kelamin_val,
    "Genetik": genetik_val,
    "Penyakit_Kronis": penyakit_val,
    "Sering_Begadang": begadang_val,
    "Gangguan_Tidur": gangguan_tidur_val,
    "Masalah_Air": air_val,
    "Penggunaan_Produk_Rambut": produk_rambut_val,
    "Anemia": anemia_val,
    "Stres": stres_val,
    "Kebiasaan_Makan": makan_val,
    }])



    # ✅ Tombol prediksi
    if st.button("💖 Prediksi Sekarang! 💖"):
        # Load scaler yang benar
        with open('scaler.pkl', 'rb') as s:
            scaler = pickle.load(s)

        # Standarisasi input sebelum prediksi
        input_scaled = scaler.transform(input_data)

        # Prediksi
        pred = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0][1] * 100

        st.subheader("💡 Hasil Prediksi:")
        if pred == 1:
            st.error("😱 Risiko Mengalami Rambut Rontok.\nSegera rawat rambutmu! 💆‍♀️")
        else:
            st.success("✨ Risiko Tidak Mengalami Rambut Rontok.\nPertahankan gaya hidup sehat ya! 💖")
   
