import streamlit as st
import numpy as np
import scipy.stats as stats

def anova_test(groups):
    st.subheader("UJI ANOVA")

    # Melakukan uji ANOVA
    statistic, p_value = stats.f_oneway(*groups)

    st.write("Hipotesis Nol: Rata-rata populasi dari semua grup sama")
    st.write("Hipotesis Alternatif: Rata-rata populasi dari setidaknya satu grup berbeda")

    st.write("Statistik Uji:", statistic)
    st.write("Nilai p:", p_value)

    if p_value < 0.05:
        st.write("Kesimpulan: Terdapat perbedaan yang signifikan antara setidaknya satu pasang grup")
    else:
        st.write("Kesimpulan: Tidak terdapat perbedaan yang signifikan antara setidaknya satu pasang grup")

def main():
    st.title("Aplikasi Uji ANOVA")

    st.write("Masukkan data untuk setiap grup")

    num_groups = st.number_input("Jumlah grup:", min_value=2, step=1)

    groups = []
    for i in range(num_groups):
        group_data = st.text_input(f"Data untuk Grup {i+1} (pisahkan dengan koma):")
        group_values = [float(x.strip()) for x in group_data.split(",")]
        groups.append(group_values)

    if st.button("Hitung"):
        anova_test(groups)
clicked = st.button('DO the Anova test!!')

if __name__ == '__main__':
    main()
