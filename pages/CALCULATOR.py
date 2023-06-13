import streamlit as st

def calculator():
    st.header("Kalkulator")

    num1 = st.number_input("Masukkan angka pertama:")
    num2 = st.number_input("Masukkan angka kedua:")

    operation = st.selectbox("Pilih operasi matematika:", ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"))

    if st.button("Hitung"):
        if operation == "Penjumlahan":
            result = num1 + num2
            st.success("Hasil penjumlahan: {}".format(result))
        elif operation == "Pengurangan":
            result = num1 - num2
            st.success("Hasil pengurangan: {}".format(result))
        elif operation == "Perkalian":
            result = num1 * num2
            st.success("Hasil perkalian: {}".format(result))
        elif operation == "Pembagian":
            if num2 != 0:
                result = num1 / num2
                st.success("Hasil pembagian: {}".format(result))
            else:
                st.error("Angka kedua tidak boleh nol untuk pembagian!")

if __name__ == '__main__':
    calculator()
