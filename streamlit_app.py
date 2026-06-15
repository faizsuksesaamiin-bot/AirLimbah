import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Sistem Evaluasi Baku Mutu Air Limbah",
    page_icon="💧",
    layout="wide"
)

# =====================================
# SIDEBAR MENU
# =====================================
menu = st.sidebar.radio(
    "📌 Pilih Menu",
    ["Beranda", "Sistem Evaluasi"]
)

# =====================================
# BERANDA
# =====================================
if menu == "Beranda":

    st.title("💧 Sistem Evaluasi Baku Mutu Air Limbah")

    st.markdown("---")

    # IDENTITAS PENYUSUN
    st.header("👨‍💻 Identitas Penyusun")

    st.write("**Kelompok 9**")
    st.write("**Kelas : D4 Pengolahan Limbah Industri**")

    st.table({
        "Nama": [
            "Banyu Biru Birowo",
            "Muhammad Faiz Retmano",
            "Muhammad Nafis",
            "Muhammad Rasya",
            "Risman Hilmansyah"
        ],
        "NIM": [
            "Isi NIM",
            "Isi NIM",
            "Isi NIM",
            "Isi NIM",
            "Isi NIM"
        ]
    })

    st.markdown("---")

    # ACUAN
    st.header("📖 Acuan Baku Mutu")

    st.info("""
    Peraturan Menteri Lingkungan Hidup dan Kehutanan Republik Indonesia

    Nomor P.68/MENLHK/SETJEN/KUM.1/8/2016

    Tentang Baku Mutu Air Limbah Domestik
    """)

    st.markdown("---")

    # PENJELASAN PARAMETER
    st.header("📚 Penjelasan Parameter Air Limbah")

    st.subheader("1. BOD (Biochemical Oxygen Demand)")
    st.write("""
    BOD adalah jumlah oksigen yang dibutuhkan oleh mikroorganisme
    untuk menguraikan bahan organik dalam air limbah.
    
    Semakin tinggi nilai BOD maka semakin tinggi tingkat pencemaran organik.
    
    **Baku Mutu : ≤ 30 mg/L**
    """)

    st.subheader("2. COD (Chemical Oxygen Demand)")
    st.write("""
    COD adalah jumlah oksigen yang diperlukan untuk mengoksidasi
    bahan pencemar secara kimia.

    Nilai COD yang tinggi menunjukkan banyaknya zat pencemar
    dalam air limbah.

    **Baku Mutu : ≤ 100 mg/L**
    """)

    st.subheader("3. TSS (Total Suspended Solid)")
    st.write("""
    TSS merupakan jumlah padatan tersuspensi yang terdapat
    dalam air limbah.

    Nilai TSS yang tinggi dapat menyebabkan kekeruhan dan
    mengganggu ekosistem perairan.

    **Baku Mutu : ≤ 30 mg/L**
    """)

    st.subheader("4. NH₃ (Amonia)")
    st.write("""
    Amonia merupakan senyawa nitrogen yang dapat bersifat toksik
    bagi organisme perairan.

    Kadar amonia yang tinggi dapat menurunkan kualitas air.

    **Baku Mutu : ≤ 10 mg/L**
    """)

    st.subheader("5. pH")
    st.write("""
    pH menunjukkan tingkat keasaman atau kebasaan air.

    Nilai pH yang terlalu rendah atau terlalu tinggi dapat
    mengganggu kehidupan organisme perairan.

    **Baku Mutu : 6 – 9**
    """)

    st.markdown("---")

    # TABEL BAKU MUTU
    st.header("📋 Ringkasan Baku Mutu")

    st.table({
        "Parameter": ["BOD", "COD", "TSS", "NH₃", "pH"],
        "Baku Mutu": [
            "≤ 30 mg/L",
            "≤ 100 mg/L",
            "≤ 30 mg/L",
            "≤ 10 mg/L",
            "6 - 9"
        ]
    })

# =====================================
# SISTEM EVALUASI
# =====================================
elif menu == "Sistem Evaluasi":

    st.title("🔍 Sistem Evaluasi Baku Mutu Air Limbah")

    st.write("Masukkan hasil analisis laboratorium:")

    # INPUT DATA
    bod = st.number_input(
        "BOD (mg/L)",
        min_value=0.0,
        value=30.0
    )

    cod = st.number_input(
        "COD (mg/L)",
        min_value=0.0,
        value=100.0
    )

    tss = st.number_input(
        "TSS (mg/L)",
        min_value=0.0,
        value=30.0
    )

    nh3 = st.number_input(
        "NH₃ (mg/L)",
        min_value=0.0,
        value=5.0
    )

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=7.0
    )

    # BAKU MUTU
    baku_mutu = {
        "BOD": 30,
        "COD": 100,
        "TSS": 30,
        "NH3": 10,
        "pH_min": 6,
        "pH_max": 9
    }

    # PROSES EVALUASI
    if st.button("🔎 Evaluasi"):

        pelanggaran = []

        if bod > baku_mutu["BOD"]:
            pelanggaran.append("BOD")

        if cod > baku_mutu["COD"]:
            pelanggaran.append("COD")

        if tss > baku_mutu["TSS"]:
            pelanggaran.append("TSS")

        if nh3 > baku_mutu["NH3"]:
            pelanggaran.append("NH₃")

        if ph < baku_mutu["pH_min"] or ph > baku_mutu["pH_max"]:
            pelanggaran.append("pH")

        total_parameter = 5
        persentase = (len(pelanggaran) / total_parameter) * 100

        st.markdown("---")

        st.header("📋 Hasil Evaluasi")

        if len(pelanggaran) == 0:
            st.success("✅ Memenuhi Baku Mutu")

        else:
            st.error("❌ Tidak Memenuhi Baku Mutu")

            st.subheader("Parameter yang Melampaui Batas")

            for p in pelanggaran:
                st.write(f"• {p}")

        st.write(
            f"### Persentase Pelanggaran : {persentase:.2f}%"
        )

        st.markdown("---")

        st.header("📊 Ringkasan Data")

        data = {
            "Parameter": [
                "BOD",
                "COD",
                "TSS",
                "NH₃",
                "pH"
            ],
            "Nilai Hasil Uji": [
                bod,
                cod,
                tss,
                nh3,
                ph
            ],
            "Baku Mutu": [
                "≤ 30",
                "≤ 100",
                "≤ 30",
                "≤ 10",
                "6 - 9"
            ]
        }

        st.table(data)
