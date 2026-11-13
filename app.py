import streamlit as st

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

# Ukuran tombol "Nggak" MAKIN MENYUSUT KECIL
font_size_nggak = max(18 - (hitung_klik * 2), 6)
padding_nggak = max(10 - (hitung_klik * 1), 2)

# Hitung level emosi/kemarahan web dari 0% sampai 100% (nambah 10% tiap klik)
level_emosi = min(hitung_klik * 10, 100)

# 2. MENYUNTIKKAN ANIMATE.CSS DAN CSS DINAMIS UNTUK TOMBOL MEMBESAR
st.markdown(f"""
    <!-- Load Animate.css untuk efek teks bergerak -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    
    <style>
    /* Background gradasi mewah dreamy pastel */
    .stApp {{
        background: linear-gradient(135deg, #fbcfe8 0%, #e0e7ff 50%, #fde68a 100%);
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
    
    /* TOMBOL IYA (TERUS MEMBESAR TANPA BATAS) */
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
        transform: scale(1.03) !important;
    }}
    
    /* Tombol Nggak (MAKIN LAMA MAKIN MENYUSUT KECIL) */
    div[data-testid="stColumn"]:nth-of-type(2) .stButton>button {{
        background-color: #ffffff !important;
        color: #777777 !important;
        border: 1px solid #cccccc !important;
        border-radius: 50px !important;
        font-weight: bold !important;
        font-size: {font_size_nggak}!important;
        padding: {padding_nggak} !important;
        transition: all 0.3s ease !important;
        animation: pulse infinite 2s;
        box-shadow: 0 4px 15px rgba(255, 51, 102, 0.4) !important;
    }}
    
    div[data-testid="stColumn"]:nth-of-type(2) .stButton>button:hover {{
        transform: scale(1.05) !important;
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

# Ambil jumlah klik "Nggak" saat ini
hitung_klik = st.session_state.hitung

# Ukuran font tombol "Iya" TERUS MEMBESAR tanpa batas
font_size_iya = 18 + (hitung_klik * 6)
padding_iya = 10 + (hitung_klik * 8)

# 4. LOGIKA HALAMAN UTAMA
if not st.session_state.selesai:
    st.markdown("""
        <marquee behavior="scroll" direction="left" style="background: #ff3366; color: white; font-weight: bold; padding: 6px; border-radius: 10px; margin-bottom: 15px;">
            🚨 PERHATIAN: ADA YANG ULANG TAHUN HARI INI! DILARANG KERAS MENGELAK ATAU MEMENCET TOMBOL NGGAK! 🚨 WAKTUNYA HURU-HARA SWEET SEVENTEEN 👑✨
        </marquee>
    """, unsafe_allow_html=True)

    st.markdown('<div class="animate__animated animate__bounceIn mega-title">👑 SWEET SEVENTEEN PARTY 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><span class="party-badge">✨ SPESIAL 7 DESEMBER • HURU-HARA DIMULAI ✨</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animate__animated animate__fadeInUp">', unsafe_allow_html=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnU1dTRneTI5ZHRkZXFlbGV5czZxY25sZ2p4MmNobnF4aGR0eDFmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QsomqbDcRm9xMFxJMu/giphy.gif", use_container_width=True)
    with col_g2:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExajJoNHo0OHY2bTR3azFrcWp5N3lhbjRkMGhucTNkYndmNW96eG5yayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oz8xAFtphMRurshu0/giphy.gif", use_container_width=True)
        
    st.markdown('<p class="mega-text">Woy denger-denger hari ini ada jatah umur yang berkurang nih wkwk...<br><b>Jujur, kamu kan yang ulang tahun hari ini, si Pendek? 👀🎂</b></p>', unsafe_allow_html=True)
    
    if hitung_klik > 0:
        st.markdown(f"<p style='color: #ff3366; font-weight: bold; margin-top: 10px;'>⚠️ Status: Sudah ngeyel menolak sebanyak {hitung_klik} kali! Tombolnya mulai kabur-kaburan tuh wkwk 🤭</p>", unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

    # --- EFEK TOMBOL KABUR / ACAK POSISI ---
    lebar_iya = 1 + (st.session_state.hitung * 0.6)
    lebar_nggak = max(1 - (st.session_state.hitung * 0.15), 0.15)
    
    if st.session_state.posisi_acak:
        kolom_kiri, kolom_kanan = st.columns([lebar_nggak, lebar_iya])
        btn_kiri = kolom_kiri.button("Nggak", use_container_width=True)
        
        teks_iya = "Iya"
        if st.session_state.hitung >= 2:
            teks_iya = "Iya, Ngaku deh!"
        if st.session_state.hitung >= 3:
            teks_iya = "IYA KOK, UDAH PENCET AJA!"
        if st.session_state.hitung >= 4:
            teks_iya = "PENCET INI ATAU GUE NGAMBEK!"
        if st.session_state.hitung >= 5:
            teks_iya = "GW BENCI LU BGT!"
        if st.session_state.hitung >= 6:
            teks_iya = "BENCI!"
            
        btn_kanan = kolom_kanan.button(teks_iya, use_container_width=True)
        
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
            teks_iya = "Iya!"
            if st.session_state.hitung >= 2:
                teks_iya = "IYA!"
            if st.session_state.hitung >= 3:
                teks_iya = "IYAA!"
            if st.session_state.hitung >= 4:
                teks_iya = "IYAAA!"
            if st.session_state.hitung >= 5:
                teks_iya = "IYAAAA!"
            if st.session_state.hitung >= 6:
                teks_iya = "IYAAAA!"
            if st.session_state.hitung >= 7:
                teks_iya = "IYAAAAA!"
            
            if st.button(teks_iya, use_container_width=True):
                st.session_state.selesai = True
                st.rerun()
                
        with col2:
            if st.button("Nggak", use_container_width=True):
                st.session_state.hitung += 1
                st.session_state.posisi_acak = random.choice([True, False])
                st.rerun() 

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


    # REAKSI MENGELAK BERPUTAR (LOOPING)
    if st.session_state.hitung > 0:
        h = st.session_state.hitung
        st.markdown('<div class="animate__animated animate__shakeX">', unsafe_allow_html=True)
        
        pesan_loop = h % 6
        
        if pesan_loop == 1:
            st.warning(f"Klik ke-{h}: Masa sih salah? lu jgn meragukan gw!")
        elif pesan_loop == 2:
            st.error(f"Klik ke-{h}: SYIT! JGN MERAGUKAN INGATAN GW! GW INGET KOK 7 DESEMBER!!!)
        elif pesan_loop == 3:
            st.error(f"Klik ke-{h}: WOY MONYET!")
        elif pesan_loop == 4:
            st.info(f"Klik ke-{h}: Capek kan ngejar tombol 'Nggak'? Pencet 'Iya' aja!!")
        elif pesan_loop == 5:
            st.info(f"Klik ke-{h}: PENCET TOMBOL SEBELAH GAK!?")
        else:
            st.warning(f"Klik ke-{h}: Ngeyel mulu!")
            
        st.markdown('</div>', unsafe_allow_html=True)

# 5. LOGIKA HALAMAN KEJUTAN (SETELAH KLIK IYA)
else:
    st.balloons()
    st.snow()
    
    st.markdown('<div class="animate__animated animate__jackInTheBox mega-title">✨ HAPPY BIRTHDAY, PENDEK! ✨</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animate__animated animate__fadeInUp">', unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExajJoNHo0OHY2bTR3azFrcWp5N3lhbjRkMGhucTNkYndmNW96eG5yayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IaGqkVQit54xT6BUDj/giphy.gif", width=300)
    st.markdown("""
    <p class="mega-text">
    🎂 <b>Happy Birthday, Bsf! 🥳🎈</b> 🎂<br><br>
    Happy Birthday my dearest beloved best friend. 17 tahun astagaa, BUAT KTP WOY!! tapi gausah buru buru buat KTP nya sih, 
    nanti kamu tersadar kalau kamu ini WNI wkekekekek. Wish you all the best yahh kekasih Furuya Rei!! 
    OMG im lucky to meet you dah asli. Mungkin you lah alasan gw lahir ke bumi. pas dikasih 77 pertanyaan terselip pertanyaan 
    ''Apakah kamu mau lahir ke bumi? disana ada Tiara'' gw be like ''Lho ya boleh wong ditawari'' :vvVVvV SORRYY FREAK BGT YYHHHH wkekekek maaf ✨<br><br>
    </p>
    """, unsafe_allow_html=True)
    
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
            
    if st.session_state.kado_pilih == "merah":
        st.error("🎁 **Isi Kado Merah:** Lu nraktir gw")
    elif st.session_state.kado_pilih == "biru":
        st.info("🎀 **Isi Kado Biru:** Gw ditraktir lu ")
    elif st.session_state.kado_pilih == "emas":
        st.success("👑 **Isi Kado Emas:** Prabowo lengser")

    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Ulangi Kemegahan Dari Awal 🔄", use_container_width=True):
        st.session_state.hitung = 0
        st.session_state.selesai = False
        st.session_state.kado_pilih = None
        st.session_state.posisi_acak = False
        st.rerun()
