import streamlit as st
import math

def hitung_probabilitas(n, x, p):
    q = 1 - p
    kombinasi = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    probabilitas = kombinasi * p**x * q**(n - x)
    return probabilitas

def main():
    st.title("Perhitungan Distribusi Binomial")

    n = st.number_input("Jumlah percobaan (n)", min_value=0, step=1, value=0)
    x = st.number_input("Jumlah keberhasilan (x)", min_value=0, step=1, value=0)
    p = st.number_input("Probabilitas keberhasilan (p)", min_value=0.0, max_value=1.0, step=0.01, value=0.0)

    if st.button("Hitung"):
        probabilitas = hitung_probabilitas(n, x, p)
        st.write("Probabilitas: {:.4f}".format(probabilitas))

if __name__ == "__main__":
    main()
