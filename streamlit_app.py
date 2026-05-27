import streamlit as st
import random

st.title("🧪 VirtualChem Lab")

st.write("Simulasi Praktikum Kimia Virtual")

menu = st.selectbox(
    "Pilih Praktikum",
    ["Menimbang", "Titrasi"]
)

# =========================
# SIMULASI MENIMBANG
# =========================
if menu == "Menimbang":

    st.header("⚖️ Simulasi Menimbang")

    # Pilihan bahan
    bahan = st.selectbox(
        "Pilih Bahan Kimia",
        ["NaOH", "HCl", "KCl", "CuSO4"]
    )

    # Target massa
    target = st.number_input(
        "Target Massa (gram)",
        min_value=0.0,
        step=0.01
    )

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2921/2921822.png",
        width=150
    )

    if st.button("Mulai Menimbang"):

        # simulasi hasil massa
        hasil = round(
            random.uniform(target - 0.02, target + 0.02),
            2
        )

        st.subheader("Hasil Penimbangan")

        st.success(
            f"{bahan} berhasil ditimbang {hasil} gram"
        )

        # pengecekan akurasi
        if hasil == target:
            st.info("Penimbangan sangat akurat ✅")

        elif hasil > target:
            st.warning("Massa melebihi target ⚠️")

        else:
            st.warning("Massa kurang dari target ⚠️")

# =========================
# SIMULASI TITRASI
# =========================
if menu == "Titrasi":

    st.header("🧪 Simulasi Titrasi")

    volume = st.slider(
        "Tambahkan Volume NaOH (mL)",
        0,
        50
    )

    if volume < 25:
        st.info("Larutan masih bening")

    elif volume == 25:
        st.success("Titik ekuivalen tercapai 🎉")

    else:
import streamlit as st
import time

st.title("🧪 VirtualChem Lab")

st.header("⚖️ Simulasi Penimbangan")

# gambar neraca
st.image(
    "https://cdn-icons-png.flaticon.com/512/2921/2921822.png",
    width=250
)

st.write("Tambahkan bahan kimia ke neraca")

# slider massa
massa = st.slider(
    "Geser untuk menambahkan massa",
    0.0,
    10.0,
    0.0,
    0.1
)

# animasi loading penimbangan
if st.button("Mulai Menimbang"):

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.success(
        f"Penimbangan selesai: {massa} gram"
    )

    # simulasi hasil di layar neraca
    st.metric(
        label="Hasil Neraca Digital",
        value=f"{massa} g"
    )

    st.balloons()
volume = st.slider(
    "Putar buret (mL)",
    0,
    50
)

if volume < 25:
    st.info("Larutan masih bening")

elif volume == 25:
    st.success("Titik ekuivalen tercapai")

else:
    st.warning("Larutan berubah pink")

    


        
        st.warning("Larutan berubah menjadi pink")
