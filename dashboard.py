
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard - CV. GRIYA DJINGGA MANDIRI", page_icon="🏢", layout="wide")

# Memuat logo
logo_path = "Logo CV. Griya Djingga Mandiri (1).png"
logo = Image.open(logo_path)

# Sidebar Navigasi
st.sidebar.image(logo, width=120)
st.sidebar.title("📂 Menu Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Dashboard", "Data Proyek", "Tentang Kami"])

# Halaman Dashboard
if menu == "Dashboard":
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(logo, width=120)
    with col2:
        st.markdown("<h1 style='color:#1f77b4;'>CV. GRIYA DJINGGA MANDIRI</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#1f77b4;'>Dashboard Utama</h4>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 Ringkasan Proyek")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Proyek", "24", "+3 bulan ini")
    with col2:
        st.metric("Klien Aktif", "12", "+1 minggu ini")
    with col3:
        st.metric("Pendapatan", "Rp 120.000.000", "+15%")

    # Grafik Proyek per Bulan
    st.markdown("### 📈 Grafik Jumlah Proyek per Bulan")

    # Contoh data dummy
    data = {
        "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul"],
        "Jumlah Proyek": [2, 3, 4, 5, 3, 4, 3]
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["Bulan"], df["Jumlah Proyek"], color="#1f77b4")
    ax.set_ylabel("Jumlah Proyek")
    ax.set_title("Proyek per Bulan")

    st.pyplot(fig)

# Halaman Data Proyek
elif menu == "Data Proyek":
    st.markdown("<h2 style='color:#1f77b4;'>📋 Data Proyek</h2>", unsafe_allow_html=True)

    # Data dummy
    data_proyek = {
        "Nama Proyek": ["Renovasi Ruko", "Pembangunan Rumah", "Interior Kantor"],
        "Klien": ["Bpk. A", "Ibu B", "CV XYZ"],
        "Status": ["Selesai", "Dalam Proses", "Perencanaan"],
        "Nilai Kontrak": ["Rp 50jt", "Rp 200jt", "Rp 150jt"]
    }
    df_proyek = pd.DataFrame(data_proyek)
    st.table(df_proyek)

# Halaman Tentang Kami
elif menu == "Tentang Kami":
    st.markdown("<h2 style='color:#1f77b4;'>🏢 Tentang CV. GRIYA DJINGGA MANDIRI</h2>", unsafe_allow_html=True)
    st.write("""
    CV. Griya Djingga Mandiri adalah perusahaan yang bergerak di bidang jasa konstruksi, renovasi, dan interior.

    Kami berkomitmen memberikan hasil kerja terbaik kepada setiap klien dengan mengedepankan kualitas, ketepatan waktu, dan kepuasan pelanggan.
    """)

# Footer
st.markdown("---")
st.markdown("<center>© 2025 CV. Griya Djingga Mandiri</center>", unsafe_allow_html=True)
