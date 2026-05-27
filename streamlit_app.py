import streamlit as st

st.title("🧪 VirtualChem Lab")

st.write("Simulasi Praktikum Kimia Virtual")

menu = st.selectbox(
    "Pilih Praktikum",
    ["Menimbang", "Titrasi"]
)

# Simulasi Menimbang
if menu == "Menimbang":

    st.header("Simulasi Menimbang")

    massa = st.number_input(
        "Masukkan massa (gram)",
        min_value=0.0
    )

    if st.button("Timbang"):
        st.success(
            f"Berhasil menimbang {massa} gram"
        )

# Simulasi Titrasi
if menu == "Titrasi":

    st.header("Simulasi Titrasi")

    if st.button("Mulai Titrasi"):
        st.info(
            "Larutan berubah warna menjadi pink"
        )
# Judul
st.title("Simulasi Menimbang")

# Input massa
massa = st.number_input(
    "Masukkan massa (gram)",
    min_value=0.0,
    step=0.1
)

# Tombol
if st.button("Timbang"):
    st.success(f"Hasil penimbangan: {massa} gram")


    
        
