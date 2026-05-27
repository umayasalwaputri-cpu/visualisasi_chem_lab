import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="VirtualChem Lab Game", layout="wide")

# =========================
# STATE GAME
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "log" not in st.session_state:
    st.session_state.log = []

def add_xp(value):
    st.session_state.xp += value

def add_log(text):
    st.session_state.log.append(text)

# =========================
# SIDEBAR (HUD GAME)
# =========================
st.sidebar.title("🎮 VirtualChem Lab")
st.sidebar.write(f"⭐ XP: {st.session_state.xp}")

menu = st.sidebar.radio(
    "Navigasi",
    ["🏠 Home", "⚖️ Menimbang", "🧪 Titrasi", "📒 Log Book"]
)

# =========================
# HOME DASHBOARD
# =========================
if menu == "🏠 Home":

    st.title("🧪 VirtualChem Lab - Game Dashboard")

    st.write("Selamat datang di simulasi laboratorium virtual")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Level", "Beginner")

    with col2:
        st.metric("XP", st.session_state.xp)

    with col3:
        st.metric("Status", "Active 🟢")

    st.divider()

    st.subheader("🎯 Quest Hari Ini")

    st.write("1. Lakukan penimbangan zat")
    st.write("2. Selesaikan titrasi sampai titik ekuivalen")

    st.info("Selesaikan quest untuk mendapatkan XP!")

# =========================
# MENIMBANG LEVEL
# =========================
if menu == "⚖️ Menimbang":

    st.title("⚖️ Level 1 - Penimbangan")

    st.image("https://cdn-icons-png.flaticon.com/512/809/809957.png", width=200)

    massa = st.slider("Tambahkan massa (gram)", 0.0, 10.0, 0.0, 0.1)

    st.metric("Neraca Digital", f"{massa:.2f} g")

    if st.button("Mulai Penimbangan"):

        add_log("Penimbangan dimulai")

        bar = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        add_xp(10)
        add_log(f"Penimbangan selesai: {massa:.2f} g")

        st.success("Level selesai +10 XP 🎉")
        st.balloons()

# =========================
# TITRASI LEVEL
# =========================
if menu == "🧪 Titrasi":

    st.title("🧪 Level 2 - Titrasi Asam Basa")

    volume = st.slider("Volume NaOH (mL)", 0, 50, 0)

    # warna larutan
    if volume < 15:
        color = "#4da6ff"
        status = "Asam kuat"
    elif volume < 25:
        color = "#ffff66"
        status = "Menuju ekuivalen"
    elif volume == 25:
        color = "#66ff66"
        status = "Ekuivalen"
    else:
        color = "#ff66cc"
        status = "Basa berlebih"

    st.markdown(
        f"""
        <div style="
            background-color:{color};
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:18px;
            font-weight:bold;">
            Larutan: {status}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(volume / 50)

    if st.button("Mulai Titrasi"):

        add_log("Titrasi dimulai")

        bar = st.progress(0)

        for i in range(100):
            time.sleep(0.015)
            bar.progress(i + 1)

            if i % 10 == 0:
                st.write("💧 Tetesan masuk...")

        if volume == 25:
            st.success("Perfect! Titik ekuivalen 🎉 +20 XP")
            add_xp(20)
            st.balloons()

        elif volume < 25:
            st.warning("Kurang titrasi")
            add_xp(5)

        else:
            st.error("Over titration")
            add_xp(3)

    # grafik
    st.subheader("📊 Kurva Titrasi")

    x = np.linspace(0, 50, 100)
    y = [2 + v * 0.2 if v < 25 else 7 + (v - 25) * 0.3 for v in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axvline(25, color="red", linestyle="--")
    ax.set_xlabel("Volume NaOH (mL)")
    ax.set_ylabel("pH")

    st.pyplot(fig)

# =========================
# LOG BOOK
# =========================
if menu == "📒 Log Book":

    st.title("📒 Lab Activity Log")

    st.write(f"Total XP: {st.session_state.xp}")

    for i, log in enumerate(st.session_state.log[-15:]):
        st.write(f"{i+1}. {log}")








        
        
