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

# Tombol "Iya" bakal terus membesar TANPA BATAS selama dia terus ngeklik "Nggak"
font_size_iya = 10 + (hitung_klik * 6)
padding_iya = 10 + (hitung_klik * 8)

# Hitung level emosi/kemarahan web dari 0% sampai 100% (nambah 10% tiap klik)
level_emosi = min(hitung_klik * 10, 100)

# 2. MENYUNTIKKAN ANIMATE.CSS DAN CSS DINAMIS UNTUK TOMBOL MEMBESAR
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

    /* KOTAK METERAN EMOSI KUSTOM (GAYA GAME) */
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
    
    /* TOMBOL IYA (OTOMATIS MEMBESAR BERDASARKAN JUMLAH KLIK NGGAK) */
    div[data-testid="stColumn"]:nth-of-type(1) .stButton>button {{
        background-color: #ff3366 !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        font-weight: bold !important;
        font-size: {font_size_iya}px !important;
        padding: {padding_iya}px 25px !important;
        transition: all 0.3s ease !important;
        animation: pulse infinite 2s;
        box-shadow: 0 4px 15px rgba(255, 51, 102, 0.4) !important;
    }}
    
    div[data-testid="stColumn"]:nth-of-type(1) .stButton>button:hover {{
        transform: scale(1.05) !important;
    }}
    
    /* Tombol Nggak (MAKIN LAMA MAKIN MENYUSUT KECIL) */
    div[data-testid="stColumn"]:nth-of-type(2) .stButton>button {{
        background-color: #ffffff !important;
        color: #777777 !important;
        border: 1px solid #cccccc !important;
        border-radius: 50px !important;
        font-weight: bold !important;
        font-size: 16px!important;
        padding: 8px 12px !important;
        animation: pulse infinite 2s;
        box-shadow: 0 4px 15px rgba(255, 51, 102, 0.4) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALIZE STATE (Memori Klik)
if 'hitung' not in st.session_state:
    st.session_state.hitung = 0
if 'selesai' not in st.session_state:
    st.session_state.selesai = False
if 'kado_pilih' not in st.session_state:
    st.session_state.buka_kado = None
if 'posisi_acak' not in st.session_state:
    st.session_state.posisi_acak = False

# 4. LOGIKA HALAMAN UTAMA
if not st.session_state.selesai:
    # Marquee / Teks berjalan darurat di atas
    st.markdown("""
        <marquee behavior="scroll" direction="left" style="background: #ff3366; color: white; font-weight: bold; padding: 6px; border-radius: 10px; margin-bottom: 15px;">
            🚨 PERHATIAN: ADA YANG ULANG TAHUN HARI INI! DILARANG KERAS MENGELAK ATAU MEMENCET TOMBOL NGGAK! 🚨 WAKTUNYA HURU-HARA SWEET SEVENTEEN 👑✨
        </marquee>
    """, unsafe_allow_html=True)

    st.markdown('<div class="animate__animated animate__fadeInDown mega-title">👑 SWEET SEVENTEEN PARTY 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><span class="badge-info">🎂 SPESIAL 7 DESEMBER • WARNING: BIKIN EMOSI 🎂</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animate__animated animate__fadeIn">', unsafe_allow_html=True)

    # Dua GIF berdampingan biar meriah
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjhlOGQ1ZDQ3a3hrZzRtYXh0NTJnZm1qbWs0dHcxeGkydG9jcGo5cSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/y4nk5bgwpWL6T5Ax9y/giphy.gif", use_container_width=True)
    with col_g2:
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3M3FkanJyeGYyOXR2cWdrYXd1ZWs1NXR3N2lhNjRpbGwwc3VwazdhYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1nymcq1Nzg1OzE5PyW/giphy.gif", use_container_width=True)
                 
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnU1dTRneTI5ZHRkZXFlbGV5czZxY25sZ2p4MmNobnF4aGR0eDFmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QsomqbDcRm9xMFxJMu/giphy.gif", use_container_width=True)
    st.markdown('<p class="mega-text">Denger-denger hari ini ada yang jatah umurnya berkurang nih... <br><b>Kamu yang ulang tahun hari ini kan? 👀</b></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- EFEK KOLOM DINAMIS & POSISI ACAK (KABUR) ---
    lebar_iya = 1 + (st.session_state.hitung * 0.6)
    lebar_nggak = max(1 - (st.session_state.hitung * 0.15), 0.15)
    
    # Kalau posisi_acak True, posisi tombol "Iya" dan "Nggak" ditukar (acak posisi)
    if st.session_state.posisi_acak:
        kolom_kiri, kolom_kanan = st.columns([lebar_nggak, lebar_iya])
        btn_kiri = kolom_kiri.button("Nggak", use_container_width=True)

    # Kalau posisi_acak True, posisi tombol "Iya" dan "Nggak" ditukar (acak posisi)
    if st.session_state.posisi_acak:
        kolom_kiri, kolom_kanan = st.columns([lebar_nggak, lebar_iya])
        btn_kiri = kolom_kiri.button("Nggak", use_container_width=True)
        
        teks_iya = "Iya, Aku Ulang Tahun! 🎉"
        if st.session_state.hitung >= 2:
            teks_iya = "Iya, Ngaku deh! 😭"
        if st.session_state.hitung >= 4:
            teks_iya = "IYA KOK, UDAH PENCET AJA! 🫵"
        if st.session_state.hitung >= 6:
            teks_iya = "PENCET INI ATAU GUE NGAMBEK! 🔥"
            
        btn_kanan = kolom_kanan.button(teks_iya, use_container_width=True)
        
        # Logika tombol diklik di posisi acak
        if btn_kiri:
            st.session_state.hitung += 1
            st.session_state.posisi_acak = random.choice([True, False])
            st.rerun()
        if btn_kanan:
            st.session_state.selesai = True
            st.rerun()
            
    else:
        col1, col2 = st.columns([lebar_iya, lebar_nggak])
                                
    with col1:
        # Teks tombol "Iya" makin lama makin memaksa
        teks_iya = "Iya"
        if st.session_state.hitung >= 2:
            teks_iya = "Iya"
        if st.session_state.hitung >= 3:
            teks_iya = "IYA"
        if st.session_state.hitung >= 4:
            teks_iya = "IYAA"
        if st.session_state.hitung >= 5:
            teks_iya = "IYAAAA"
        if st.session_state.hitung >= 6:
            teks_iya = "IYAAAAAAA"
        if st.session_state.hitung >= 7:
            teks_iya = "PENCET INI ATAU GUE NGAMBEK! 🔥"
            
        if st.button(teks_iya, use_container_width=True):
            st.session_state.selesai = True
            st.rerun()

            
    with col2:
        # Teks tombol TETAP "Nggak" konsisten tidak berubah-ubah, tapi kotaknya menyusut ciut
        if st.button("Nggak", use_container_width=True):
            st.session_state.hitung += 1
            st.rerun() 

   # --- ALTERNATIF: METERAN EMOSI / KEMARAHAN WEB KUSTOM ---
    st.markdown(f"""
    <div class="emotion-box">
        <div style="font-weight: bold; color: #ff3366; font-family: 'Poppins', sans-serif;">
            🔥 Level Kekesalan: {level_emosi}%
        </div>
        <div class="emotion-bar-container">
            <div class="emotion-bar-fill"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # REAKSI MENGELAK DENGAN EFEK LOOPING BERPUTAR TERUS
    if st.session_state.hitung > 0:
        h = st.session_state.hitung
        st.markdown('<div class="animate__animated animate__shakeX">', unsafe_allow_html=True)
        
        # Menggunakan modulus (%) agar omelannya terus berputar (looping) tidak ada habisnya
        pesan_loop = h % 6
        
        if pesan_loop == 1:
            st.warning(f"Klik ke-{h}: Masa sih salah? lu jgn meragukan gw!")
        elif pesan_loop == 2:
            st.error(f"Klik ke-{h}: SYIT! JGN MERAGUKAN INGATAN GW! INGAT KOK GW 7 DESEMBER 😤")
        elif pesan_loop == 3:
            st.error(f"Klik ke-{h}: WOY MONYET!")
        elif pesan_loop == 4:
            st.info(f"Klik ke-{h}: Capek kan mencet tombol 'Nggak'?")
        elif pesan_loop == 5:
            st.info(f"Klik ke-{h}: PENCET TOMBOL SEBELAH GAK!?")
        elif pesan_loop == 6:
            st.info(f"Klik ke-{h}: GW AMBIL YE FURUYA REI LUHK!")
        elif pesan_loop == 7:
            st.info(f"Klik ke-{h}: GW BENCI LU!")
        else:
            st.warning(f"Klik ke-{h}: LU ngeyel terus!")
            
        st.markdown('</div>', unsafe_allow_html=True)


# 5. LOGIKA HALAMAN KEJUTAN (SETELAH KLIK IYA - MAKIN RAMAI & RUSUH)
else:
    # EFEK PARTY MODE MAKSIMAL
    st.balloons()
    st.snow()
    
    st.markdown('<div class="animate__animated animate__jackInTheBox mega-title">✨ HAPPY BIRTHDAY, PENDEK! ✨</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animate__animated animate__fadeInUp">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnU1dTRneTI5ZHRkZXFlbGV5czZxY25sZ2p4MmNobnF4aGR0eDFmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IaGqkVQit54xT6BUDj/giphy.gif", width=300)
    st.markdown("""
    <p class="mega-text">
    🎂 <b>Happy Birthday, Bsf! 🥳🎈</b> 🎂<br><br>
    Happy Birthday my dearest beloved best friend. 17 tahun astagaa, BUAT KTP WOY!! tapi gausah buru buru buat KTP nya sih, 
    nanti kamu tersadar kalau kamu ini WNI wkekekekek. Wish you all the best yahh kekasih Furuya Rei!! 
    OMG im lucky to meet you dah asli. Mungkin you lah alasan gw lahir ke bumi. pas dikasih 77 pertanyaan terselip pertanyaan 
    ''Apakah kamu mau lahir ke bumi? disana ada Tiara'' gw be like ''Lho ya boleh wong ditawari'' :vvVVvV SORRYY FREAK BGT YYHHHH wkekekek maaf ✨<br><br>
    <span style="font-size: 22px; color: #ff3366;"><b>🎁 Pertanyaan Terakhir: Kapan nih kita bertemu lagih? Ditunggu undangannya ya! 🍕🍰</b></span>
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎁 PILIH KADO MISTERIUSMU SEKARANG! (Pilih salah satu)")
    
    k1, k2, k3 = st.columns(3)
    with k1:
        if st.button("Kado Kotak Merah 📦", use_container_width=True):
            st.session_state.kado_pilih = "merah"
    with k2:
        if st.button("Kado Pita Biru 🎀", use_container_width=True):
            st.session_state.kado_pilih = "biru"
    with k3:
        if st.button("Kado Emas 👑", use_container_width=True):
            st.session_state.kado_pilih = "emas"

# AMAN: Menggunakan .get() agar tidak error KeyError meskipun state kosong
    pilihan_kado = st.session_state.get("kado_pilih", None)
    
    if pilihan_kado == "merah":
        st.error("🎁 **Isi Kado Merah:** Tiket gratis ditraktir seblak level neraka (syarat & ketentuan: dibayarin pakai doa doang wkwk).")
    elif pilihan_kado == "biru":
        st.info("🎀 **Isi Kado Biru:** Halusinasi 1 jam penuh ditemenin Furuya Rei versi karton 2D. Lumayan kan wkwk!")
    elif pilihan_kado == "emas":
        st.success("👑 **Isi Kado Emas:** Ucapan tulus dari lubuk hati terdalam: Semoga semua impian 17 tahunmu terwujud, sehat & sukses selalu bestie tercinta! ✨")

    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Ulangi Kemegahan Dari Awal 🔄", use_container_width=True):
        st.session_state.hitung = 0
        st.session_state.selesai = False
        st.session_state.kado_pilih = None
        st.session_state.posisi_acak = False
        st.rerun()

    if "kado_pilih" not in st.session_state:
    st.session_state.kado_pilih = None
    if st.session_state.get(kado_pilih) == "merah":
        st.error("🎁 **Isi Kado Merah:** Lu nraktir gw")
    elif st.session_state.kado_pilih == "biru":
        st.info("🎀 **Isi Kado Biru:** Gw ditraktir lu!")
    elif st.session_state.kado_pilih == "emas":
        st.success("👑 **Isi Kado Emas:** Prabowo lengser")

    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Ulangi Kemegahan Dari Awal 🔄", use_container_width=True):
        st.session_state.hitung = 0
        st.session_state.selesai = False
        st.session_state.kado_pilih = None
        st.session_state.posisi_acak = False
        st.rerun()
