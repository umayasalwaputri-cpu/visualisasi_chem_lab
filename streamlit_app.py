import streamlit as st
import time

# =========================
# JUDUL WEB
# =========================

st.title("🧪 VirtualChem Lab")

st.write("Simulasi Praktikum Kimia Virtual")

# =========================
# MENU PRAKTIKUM
# =========================

menu = st.selectbox(
    "Pilih Praktikum",
    ["Menimbang", "Titrasi"]
)

# =========================
# SIMULASI MENIMBANG
# =========================

if menu == "Menimbang":

    st.header("⚖️ Simulasi Penimbangan")

    st.write(
        "Geser slider untuk menambahkan bahan kimia ke neraca"
    )

    # gambar penimbangan
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1046/1046857.png",
        width=300
    )

    # slider massa
    massa = st.slider(
        "Tambahkan Massa (gram)",
        0.0,
        10.0,
        0.0,
        0.1
    )

    # tampilan angka neraca
    st.metric(
        label="Hasil Neraca Digital",
        value=f"{massa} gram"
    )

    # tombol mulai
    if st.button("Mulai Menimbang"):

        st.write("Proses Penimbangan...")

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        st.success(
            f"Penimbangan selesai: {massa} gram"
        )

        st.balloons()

# =========================
# SIMULASI TITRASI
# =========================

if menu == "Titrasi":

    st.header("🧪 Simulasi Titrasi")

    st.write(
        "Geser slider untuk menambahkan NaOH dari buret ke Erlenmeyer"
    )

    # gambar buret + erlenmeyer
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2784/2784487.png",
        width=300
    )

    # slider volume
    volume = st.slider(
        "Volume NaOH (mL)",
        0,
        50,
        0
    )

    # animasi proses
    if st.button("Mulai Titrasi"):

        st.write("Proses Titrasi...")

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        # kondisi larutan
        if volume < 25:

            st.info(
                "Larutan masih bening"
            )

        elif volume == 25:

            st.success(
                "Titik ekuivalen tercapai 🎉"
            )

            st.balloons()

        else:

            st.warning(
                "Larutan berubah menjadi pink"
            )

    # tampilan volume
    st.metric(
        label="Volume Saat Ini",
        value=f"{volume} mL"
    )









        
        
