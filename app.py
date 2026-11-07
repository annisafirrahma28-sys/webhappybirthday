import streamlit as st
import random

# 1. SETTING HALAMAN PREMIUM
st.set_page_config(
    page_title="Happy Birthday BSF! 🎂🎉", 
    page_icon="👑", 
    layout="centered"
)

# Ambil jumlah klik "Nggak" saat ini
hitung_klik = st.session_state.get('hitung', 0)

# Tombol "Iya" bakal terus membesar TANPA BATAS secara smooth
font_size_iya = 16 + (hitung_klik * 5)
padding_iya = 12 + (hitung_klik * 6)

# Hitung level emosi/kemarahan web dari 0% sampai 100%
level_emosi = min(hitung_klik * 10, 100)

# 2. MENYUNTIKKAN ANIMATE.CSS DAN CSS TOMBOL SMOOTH BERWARNA
st.markdown(f"""
    <!-- Load Animate.css untuk efek teks bergerak -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    
    <style>
    /* Background gradasi mewah */
    .stApp {{
        background: linear-gradient(35deg, #fbcfe8 0%, #e0e7ff 50%, #fde68a 100%);
    }}
    
    /* Wadah utama bergaya kaca transparan mewah (Glassmorphism) */
    .glass-card {{
        background: rgba(255, 255, 255, 0.45);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(8.5px);
        -webkit-backdrop-filter: blur(8.5px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
    }}
    
    /* Judul Megah Animasi */
    .mega-title {{ 
        font-family: 'Poppins', sans-serif;
        font-size: 32px !important; 
        font-weight: 900; 
        color: #ff3366; 
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
        margin-top: 10px;
        margin-bottom: 10px;
    }}

    /* Subtitle Badge Rame */
    .badge-info {{
        display: inline-block;
        background: #ff3366;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(255,51,102,0.3);
    }}
    
    /* Teks Narasi */
    .mega-text {{ 
        font-family: 'Inter', sans-serif;
        font-size: 20px !important; 
        color: #333333;
        font-weight: 500;
        text-align: center; 
        line-height: 1.8;
    }}

    /* KOTAK METERAN EMOSI KUSTOM */
    .emotion-box {{
        background: rgba(255, 255, 255, 0.6);
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 20px;
        border: 2px solid #ff3366;
        box-shadow: 0 4px 15px rgba(255, 51, 102, 0.2);
    }}
    
    .emotion-bar-container {{
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 20px;
        height: 22px;
        overflow: hidden;
        margin-top: 8px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
    }}
    
    .emotion-bar-fill {{
        width: {level_emosi}%;
        height: 100%;
        background: linear-gradient(90deg, #ff9a9e 0%, #ff3366 100%);
        border-radius: 20px;
        transition: width 0.4s ease-in-out;
    }}
    
    /* STYLING KHUSUS TOMBOL IYA DI HALAMAN UTAMA (BERWARNA & SMOOTH) */
    div[data-testid="stColumn"]:nth-of-type(1) button {{
        background: linear-gradient(135deg, #ff3366 0%, #ff6b81 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        font-weight: 800 !important;
        font-size: {font_size_iya}px !important;
        padding: {padding_iya}px 20px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 6px 20px rgba(255, 51, 102, 0.4) !important;
        width: 100% !important;
    }}
    
    div[data-testid="stColumn"]:nth-of-type(1) button:hover {{
        transform: scale(1.02) !important;
        background: linear-gradient(135deg, #e62e5c 0%, #ff526d 100%) !important;
    }}
    
    /* STYLING KHUSUS TOMBOL NGGAK DI HALAMAN UTAMA */
    div[data-testid="stColumn"]:nth-of-type(2) button {{
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%) !important;
        color: #475569 !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 20px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        width: 100% !important;
    }}
    
    div[data-testid="stColumn"]:nth-of-type(2) button:hover {{
        background: #e2e8f0 !important;
        color: #1e293b !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALIZE STATE (Memori Klik)
if 'hitung' not in st.session_state:
    st.session_state.hitung = 0
if 'selesai' not in st.session_state:
    st.session_state.selesai = False
if 'kado_pilih' not in st.session_state:
    st.session_state.kado_pilih = None
if 'posisi_acak' not in st.session_state:
    st.session_state.posisi_acak = False

# 4. LOGIKA HALAMAN UTAMA
if not st.session_state.selesai:
    st.markdown("""
        <marquee behavior="scroll" direction="left" style="background: #ff3366; color: white; font-weight: bold; padding: 6px; border-radius: 10px; margin-bottom: 15px;">
            🚨 PERHATIAN: ADA YANG ULANG TAHUN HARI INI! DILARANG KERAS MENGELAK ATAU MEMENCET TOMBOL NGGAK! 🚨 WAKTUNYA HURU-HARA SWEET SEVENTEEN 👑✨
        </marquee>
    """, unsafe_allow_html=True)

    st.markdown('<div class="animate__animated animate__fadeInDown mega-title">👑 SWEET SEVENTEEN PARTY 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><span class="badge-info">🎂 SPESIAL 7 DESEMBER • WARNING: BIKIN EMOSI 🎂</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animate__animated animate__fadeIn">', unsafe_allow_html=True)

    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExy4nk5bgwpWL6T5Ax9y/giphy.gif", use_container_width=True)
    with col_g2:
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3M3FkanJyeGYyOXR2cWdrYXd1ZWs1NXR3N2lhNjRpbGwwc3VwazdhYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1nymcq1Nzg1OzE5PyW/giphy.gif", use_container_width=True)
                 
    st.markdown('<div class="glass-card" style="margin-top: 15px;">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnU1dTRneTI5ZHRkZXFlbGV5czZxY25sZ2p4MmNobnF4aGR0eDFmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QsomqbDcRm9xMFxJMu/giphy.gif", use_container_width=True)
    st.markdown('<p class="mega-text"> Denger-denger hari ini ada yang jatah umurnya berkurang kan? 👀</b></p>', unsafe_allow_html=True)
