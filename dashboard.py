
import streamlit as st
from PIL import Image
import pandas as pd
import os

# ---------- CONFIG ---------- #
st.set_page_config(page_title="Dashboard - CV. GRIYA DJINGGA MANDIRI", layout="wide")

# Dummy login data (bisa diganti ke database atau st.secrets untuk produksi)
USERS = {"admin": "1234", "marketing": "rumah"}

# ---------- LOGIN ---------- #
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login_form"):
        st.title("🔐 Login Dashboard")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            if USERS.get(username) == password:
                st.session_state.logged_in = True
                st.success("Login berhasil!")
                st.experimental_rerun()
            else:
                st.error("Username atau password salah.")
    st.stop()

# ---------- HEADER ---------- #
logo = Image.open("Logo CV. Griya Djingga Mandiri (1).png")
st.sidebar.image(logo, width=120)
st.sidebar.title("📂 Menu Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Dashboard", "Upload Foto", "Katalog Rumah", "Tentang Kami"])

# ---------- DASHBOARD ---------- #
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

# ---------- UPLOAD FOTO ---------- #
elif menu == "Upload Foto":
    st.markdown("## 📸 Upload Foto Proyek")
    uploaded_file = st.file_uploader("Pilih gambar proyek", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Preview Gambar", use_column_width=True)
        st.success("Foto berhasil diunggah! (simulasi)")

# ---------- KATALOG RUMAH ---------- #
elif menu == "Katalog Rumah":
    st.markdown("## 🏡 Katalog Rumah Dijual")

    # Dummy data katalog rumah
    data = [
        {
            "Nama": "Tipe 45 PT. Zamzam",
            "Harga": "Rp 350.000.000",
            "Lokasi": "Bengawan Solo",
            "Status": "Tersedia",
            "Foto": "https://via.placeholder.com/300x200.png?text=Rumah+1"
        },
        {
            "Nama": "Tipe 60 Hook Premium",
            "Harga": "Rp 520.000.000",
            "Lokasi": "Dorogowok",
            "Status": "Sold Out",
            "Foto": "https://via.placeholder.com/300x200.png?text=Rumah+2"
        }
    ]

    for rumah in data:
        st.markdown(f"### {rumah['Nama']}")
        st.image(rumah["Foto"], width=400)
        st.write(f"**Harga:** {rumah['Harga']}")
        st.write(f"**Lokasi:** {rumah['Lokasi']}")
        st.write(f"**Status:** `{rumah['Status']}`")
        st.markdown("---")

# ---------- TENTANG KAMI ---------- #
elif menu == "Tentang Kami":
    st.markdown("<h2 style='color:#1f77b4;'>🏢 Tentang CV. GRIYA DJINGGA MANDIRI</h2>", unsafe_allow_html=True)
    st.write("""
    CV. Griya Djingga Mandiri adalah perusahaan yang bergerak di bidang jasa konstruksi, renovasi, dan interior.
    Kami berkomitmen memberikan hasil kerja terbaik kepada setiap klien dengan mengedepankan kualitas, ketepatan waktu, dan kepuasan pelanggan.
    """)

st.markdown("---")
st.markdown("<center>© 2025 CV. Griya Djingga Mandiri</center>", unsafe_allow_html=True)
