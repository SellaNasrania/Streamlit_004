import streamlit as st
import numpy as np

def vector_calculator():
    st.header("Kalkulator Vektor")

    vector_input = st.text_input("Masukkan vektor (pisahkan elemen dengan koma, contoh: 1,2,3):")
    vector = np.array([float(x) for x in vector_input.split(",")])

    if st.button("Hitung"):
        st.subheader("Hasil Perhitungan")

        st.write("Vektor:", vector)
        st.write("Dimensi vektor:", vector.shape[0])
        st.write("Jumlah elemen vektor:", vector.size)
        st.write("Nilai maksimum:", np.max(vector))
        st.write("Nilai minimum:", np.min(vector))
        st.write("Rata-rata:", np.mean(vector))
        st.write("Standar deviasi:", np.std(vector))

def matrix_calculator():
    st.header("Kalkulator Matriks")

    matrix_rows = st.number_input("Masukkan jumlah baris matriks:")
    matrix_cols = st.number_input("Masukkan jumlah kolom matriks:")

    matrix = np.zeros((int(matrix_rows), int(matrix_cols)))

    st.subheader("Isi Matriks")
    for i in range(int(matrix_rows)):
        for j in range(int(matrix_cols)):
            matrix[i][j] = st.number_input("Masukkan elemen matriks pada baris {} dan kolom {}: ".format(i+1, j+1))

    if st.button("Hitung"):
        st.subheader("Hasil Perhitungan")

        st.write("Matriks:")
        st.write(matrix)

        st.write("Dimensi matriks:", matrix.shape)
        st.write("Jumlah elemen matriks:", matrix.size)
        st.write("Transpos:", matrix.T)
        st.write("Determinan:", np.linalg.det(matrix))
        st.write("Invers:", np.linalg.inv(matrix))

if __name__ == '__main__':
    calculator_type = st.selectbox("Pilih jenis kalkulator:", ("Kalkulator Vektor", "Kalkulator Matriks"))

    if calculator_type == "Kalkulator Vektor":
        vector_calculator()
    elif calculator_type == "Kalkulator Matriks":
        matrix_calculator()
