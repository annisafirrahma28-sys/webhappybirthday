import streamlit as st

# 1. SETTING HALAMAN PREMIUM
st.set_page_config(
    page_title="Happy Birthday BSF! 🎂🎉", 
    page_icon="👑", 
    layout="centered"
)

# Ambil jumlah klik "Nggak" saat ini untuk mengatur ukuran tombol secara dinamis
hitung_klik = st.session_state.get('hitung', 0)

# Ukuran font dan padding tombol "Iya" yang bakal makin bengkak/membesar tiap diklik "Nggak"
font_size_iya = min(18 + (hitung_klik * 4), 36)
padding_iya = min(10 + (hitung_klik * 5), 30)

# 2. MENYUNTIKKAN ANIMATE.CSS DAN EMAS/PINK GLASSMORPHISM STYLE
st.markdown("""
    <!-- Load Animate.css untuk efek teks bergerak -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    
    <style>
    /* Background gradasi mewah */
    .stApp {
        background: linear-gradient(135deg, #a8ede3 0%, #fed6e3 100%);
    }
    
    /* Wadah utama bergaya kaca transparan mewah (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.45);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(8.5px);
        -webkit-backdrop-filter: blur(8.5px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Judul Megah Animasi */
    .mega-title { 
        font-family: 'Times New Roman', sans-serif;
        font-size: 32px !important; 
        font-weight: 900; 
        color: #fb6f92; 
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
        margin-top: 10px;
        margin-bottom: 10px;
    }
    
    /* Teks Narasi */
    .mega-text { 
        font-family: 'Helvetica', sans-serif;
        font-size: 20px !important; 
        color: #333333;
        font-weight: 500;
        text-align: center; 
        line-height: 1.8;
    }
    
    /* Kustomisasi tombol bawaan streamlit */
    .stButton>button {
        border-radius: 50px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        padding: 10px 25px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    }

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
    
    /* Tombol Nggak (Tetap standar) */
    div[data-testid="stColumn"]:nth-of-type(2) .stButton>button {{
        background-color: #ffffff !important;
        color: #777777 !important;
        border: 1px solid #cccccc !important;
        border-radius: 50px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        padding: 10px 25px !important;
        transition: all 0.3s ease !important;
        animation: pulse infinite 2s;
        box-shadow: 0 4px 15px rgba(255, 51, 102, 0.4) !important;
    }}
    
    div[data-testid="stColumn"]:nth-of-type(2) .stButton>button:hover {{
        transform: scale(1.05) !important;
    }}
    
# 3. INITIALIZE STATE (Memori Klik)
if 'hitung' not in st.session_state:
    st.session_state.hitung = 0
if 'selesai' not in st.session_state:
    st.session_state.selesai = False

# 4. LOGIKA HALAMAN UTAMA
if not st.session_state.selesai:
    # Judul dengan animasi berdenyut masuk
    st.markdown('<div class="animate__animated animate__fadeInDown mega-title">👑 sweet seventeen 👑</div>', unsafe_allow_html=True)
    
    # Bungkus konten ke dalam kartu kaca mewah
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnU1dTRneTI5ZHRkZXFlbGV5czZxY25sZ2p4MmNobnF4aGR0eDFmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QsomqbDcRm9xMFxJMu/giphy.gif", use_container_width=True)
    st.markdown('<p class="mega-text">Denger-denger hari ini ada yang jatah umurnya berkurang nih... <br><b>Kamu yang ulang tahun hari ini kan? 👀</b></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BAGIAN TOMBOL DINAMIS (MEMBESAR & MENYUSUT) ---
    lebar_kolom_iya = min(1 + (st.session_state.hitung * 0.4), 3.0)
    lebar_kolom_nggak = max(1 - (st.session_state.hitung * 0.15), 0.3)
    
    col1, col2 = st.columns([lebar_kolom_iya, lebar_kolom_nggak])
    
    with col1:
        teks_iya = "Iya"
        if st.session_state.hitung >= 2:
            teks_iya = "IYA"
        if st.session_state.hitung >= 3:
            teks_iya = "IYAA"
        if st.session_state.hitung >= 4:
            teks_iya = "IYAAA"
        if st.session_state.hitung >= 5:
            teks_iya = "IYAAAA"
        if st.session_state.hitung >= 6:
            teks_iya = "IYAAAAAA!"
        if st.session_state.hitung >= 6:
            teks_iya = "PENCET INI WOY!"
            
        if st.button(teks_iya, use_container_width=True):
            st.session_state.selesai = True
            st.rerun()
            
    with col2:
        if st.button("Nggak", use_container_width=True):
            st.session_state.hitung += 1
            st.rerun() 

    # REAKSI MENGELAK DENGAN EFEK LOOPING BERPUTAR TERUS
    if st.session_state.hitung > 0:
        h = st.session_state.hitung
        st.markdown('<div class="animate__animated animate__shakeX">', unsafe_allow_html=True)
        
        # Menggunakan modulus (%) agar omelannya terus berputar (looping) tidak ada habisnya
        pesan_loop = h % 6
        
        if pesan_loop == 1:
            st.warning(f"Klik ke-{h}: Masa sih salah? lu jgn meragukan gw! 🧐")
        elif pesan_loop == 2:
            st.error(f"Klik ke-{h}: SYIT! JGN MERAGUKAN INGATAN GW! INGAT KOK GW 7 DESEMBER 😤")
        elif pesan_loop == 3:
            st.error(f"Klik ke-{h}: WOY MONYET! Ngaku aja napa! 🐒")
        elif pesan_loop == 4:
            st.info(f"Klik ke-{h}: Capek kan mencet tombol 'Nggak'? Tombol 'Iya'-nya makin raksasa tuh! 💻😭")
        elif pesan_loop == 5:
            st.info(f"Klik ke-{h}: PENCET TOMBOL SEBELAH GAK!? Gak bakal bisa kabur lu! 🫵🔥")
        else:
            st.warning(f"Klik ke-{h}: Total ngeyel terus! Web ini bakal nge-loop terus sampe subuh kalau gak ngaku! 🤣💀")
            
        st.markdown('</div>', unsafe_allow_html=True)

# 5. LOGIKA HALAMAN KEJUTAN (SETELAH KLIK IYA)
else:
    st.balloons()
    st.snow()
    
    st.markdown('<div class="animate__animated animate__jackInTheBox mega-title">✨ HAPPY BIRTHDAY, PENDEK! ✨</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animate__animated animate__fadeInUp">', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/xTkgqj6W1lI5q144z6/giphy.gif", width=300)
    st.markdown("""
    <p class="mega-text">
    🎂 <b>Selamat berkurang jatah umur ya!</b> 🎂<br><br>
    Happy Birthday my dearest beloved best friend. 17 tahun astagaa, BUAT KTP WOY!! tapi gausah buru buru buat KTP nya sih, 
    nanti kamu tersadar kalau kamu ini WNI wkekekekek. Wish you all the best yahh kekasih Furuya Rei!! 
    OMG im lucky to meet you dah asli. Mungkin you lah alasan gw lahir ke bumi. pas dikasih 77 pertanyaan terselip pertanyaan 
    ''Apakah kamu mau lahir ke bumi? disana ada Tiara'' gw be like ''Lho ya boleh wong ditawari'' :vvVVvV SORRYY FREAK BGT YYHHHH wkekekek maaf ✨ ✨<br><br>
    <span style="font-size: 22px; color: #ff3366;"><b>🎁 Pertanyaan Terakhir: Kapan nih kita bertemu lagih ><? Ditunggu undangannya ya! 🍕🍰</b></span>
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Ulangi Kemegahan 🔄", use_container_width=True):
        st.session_state.hitung = 0
        st.session_state.selesai = False
        st.rerun()
