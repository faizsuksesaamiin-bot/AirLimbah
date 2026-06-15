
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Sistem Evaluasi Baku Mutu Air Limbah", page_icon="💧", layout="wide")

if "riwayat" not in st.session_state:
    st.session_state.riwayat = pd.DataFrame(
        columns=[
            "Tanggal","Jenis Sampel","Nama Penyampling",
            "pH","BOD (mg/L)","COD (mg/L)","TSS (mg/L)","NH3 (mg/L)"
        ]
    )

menu = st.sidebar.radio("📌 Menu", ["Beranda", "Sistem Evaluasi"])

if menu == "Beranda":
    st.title("💧 Sistem Evaluasi Baku Mutu Air Limbah")

    st.header("👨‍💻 Identitas Penyusun")
    st.write("**Kelompok 9**")
    st.write("**Kelas : 1F Pengolahan Limbah Industri**")

    st.table(pd.DataFrame({
        "Nama":[
            "Banyu Biru Birowo",
            "Muhammad Faiz Retmano",
            "Muhammad Nafis",
            "Muhammad Rasya Fadillah",
            "Risman Hilmansyah"
        ],
        "NIM":[
            "2530601","2530633","2530636","2530638","2530649"
        ]
    }))

    st.header("📖 Acuan Baku Mutu")
    st.info(""" Permen LHK RI Nomor P.68/MENLHK/SETJEN/KUM.1/8/2016 Tentang Baku Mutu Air Limbah Domestik """)

    st.header("📚 Penjelasan Parameter Air Limbah")

    st.subheader("BOD (Biochemical Oxygen Demand)")
    st.write("Jumlah oksigen yang dibutuhkan mikroorganisme untuk menguraikan bahan organik. Baku mutu ≤ 30 mg/L.")

    st.subheader("COD (Chemical Oxygen Demand)")
    st.write("Jumlah oksigen yang diperlukan untuk mengoksidasi bahan pencemar secara kimia. Baku mutu ≤ 100 mg/L.")

    st.subheader("TSS (Total Suspended Solid)")
    st.write("Jumlah padatan tersuspensi dalam air limbah. Baku mutu ≤ 30 mg/L.")

    st.subheader("NH₃ (Amonia)")
    st.write("Senyawa nitrogen yang dapat bersifat toksik bagi organisme perairan. Baku mutu ≤ 10 mg/L.")

    st.subheader("pH")
    st.write("Tingkat keasaman atau kebasaan air. Baku mutu 6–9.")

    st.header("📋 Ringkasan Baku Mutu")
    st.table({
        "Parameter":["BOD","COD","TSS","NH₃","pH"],
        "Baku Mutu":["≤ 30 mg/L","≤ 100 mg/L","≤ 30 mg/L","≤ 10 mg/L","6–9"]
    })

    st.caption("Satuan BOD, COD, TSS, dan NH₃ menggunakan mg/L (setara ppm pada air).")

else:
    st.title("🔍 Sistem Evaluasi Baku Mutu Air Limbah")

    st.header("📥 Informasi Sampel")
    c1, c2, c3 = st.columns(3)

    with c1:
        jenis_sampel = st.selectbox("Jenis Sampel",
            ["LIMBAH DOMESTIK","LIMBAH INDUSTRI","LIMBAH CAIR LABORATORIUM"])

    with c2:
        penyampling = st.text_input("Nama Penyampling")

    with c3:
        tanggal = st.date_input("Tanggal Pengambilan Sampel", value=date.today())

    st.header("🧪 Parameter Air Limbah")

    bod = st.number_input("BOD (mg/L atau ppm)", min_value=0.0)
    cod = st.number_input("COD (mg/L atau ppm)", min_value=0.0)
    tss = st.number_input("TSS (mg/L atau ppm)", min_value=0.0)
    nh3 = st.number_input("NH₃ (mg/L atau ppm)", min_value=0.0)
    ph = st.number_input("pH", min_value=0.0, max_value=14.0)

    baku_mutu = {"BOD":30,"COD":100,"TSS":30,"NH3":10,"pH_min":6,"pH_max":9}

    if st.button("🔎 Evaluasi"):
        pelanggaran = []

        if bod > baku_mutu["BOD"]: pelanggaran.append("BOD")
        if cod > baku_mutu["COD"]: pelanggaran.append("COD")
        if tss > baku_mutu["TSS"]: pelanggaran.append("TSS")
        if nh3 > baku_mutu["NH3"]: pelanggaran.append("NH₃")
        if ph < baku_mutu["pH_min"] or ph > baku_mutu["pH_max"]:
            pelanggaran.append("pH")

        persentase = (len(pelanggaran)/5)*100

        st.header("📋 Hasil Evaluasi")

        if len(pelanggaran) == 0:
            st.success("✅ Memenuhi Baku Mutu")
        else:
            st.error("❌ Tidak Memenuhi Baku Mutu")
            st.write("Parameter yang melampaui batas:")
            for p in pelanggaran:
                st.write(f"• {p}")

        st.write(f"### Persentase Pelanggaran : {persentase:.2f}%")

        hasil = pd.DataFrame({
            "Parameter":["BOD","COD","TSS","NH₃","pH"],
            "Nilai Hasil Uji":[bod,cod,tss,nh3,ph],
            "Baku Mutu":["≤30 mg/L","≤100 mg/L","≤30 mg/L","≤10 mg/L","6-9"]
        })

        st.table(hasil)

        data_baru = pd.DataFrame({
            "Tanggal":[tanggal],
            "Jenis Sampel":[jenis_sampel],
            "Nama Penyampling":[penyampling],
            "pH":[ph],
            "BOD (mg/L)":[bod],
            "COD (mg/L)":[cod],
            "TSS (mg/L)":[tss],
            "NH3 (mg/L)":[nh3]
        })

        st.session_state.riwayat = pd.concat(
            [st.session_state.riwayat, data_baru],
            ignore_index=True
        )

    st.header("📁 Riwayat Pengujian")

    if not st.session_state.riwayat.empty:
        st.dataframe(st.session_state.riwayat, use_container_width=True)

        csv = st.session_state.riwayat.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Riwayat (CSV)",
            data=csv,
            file_name="riwayat_pengujian_air_limbah.csv",
            mime="text/csv"
        )
    else:
        st.info("Belum ada data pengujian.")
