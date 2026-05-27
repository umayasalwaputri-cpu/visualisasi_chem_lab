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
app = Flask(_name_)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Halaman simulasi menimbang
@app.route('/timbang')
def timbang():
    return render_template('timbang.html')

# Halaman simulasi titrasi
@app.route('/titrasi')
def titrasi():
    return render_template('titrasi.html')

if _name_ == '_main_':
    app.run(debug=True)



    
        
