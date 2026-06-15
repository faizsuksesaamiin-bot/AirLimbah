# =====================================================
# FITUR RIWAYAT PENGUJIAN
# =====================================================

st.markdown("---")
st.header("📁 Riwayat Pengujian")

if not st.session_state.riwayat.empty:

    st.dataframe(
        st.session_state.riwayat,
        use_container_width=True
    )

    # DOWNLOAD CSV
    csv = st.session_state.riwayat.to_csv(index=False)

    st.download_button(
        label="⬇️ Unduh Riwayat Pengujian (CSV)",
        data=csv,
        file_name="riwayat_pengujian_air_limbah.csv",
        mime="text/csv"
    )

    # GRAFIK
    st.markdown("---")
    st.subheader("📈 Grafik Hasil Pengujian")

    grafik = st.session_state.riwayat[
        ["BOD (mg/L)", "COD (mg/L)", "TSS (mg/L)", "NH3 (mg/L)"]
    ]

    st.line_chart(grafik)

    # RESET DATA
    if st.button("🗑️ Hapus Seluruh Riwayat"):
        st.session_state.riwayat = pd.DataFrame(
            columns=[
                "Tanggal",
                "Jenis Sampel",
                "Nama Penyampling",
                "pH",
                "BOD (mg/L)",
                "COD (mg/L)",
                "TSS (mg/L)",
                "NH3 (mg/L)",
                "Status"
            ]
        )

        st.success("Riwayat berhasil dihapus.")
        st.rerun()

else:
    st.info("Belum ada data pengujian.")
