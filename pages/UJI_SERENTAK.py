import streamlit as st
import pandas as pd
import statsmodels.api as sm

def perform_regression(df, x_cols, y_col):
    X = df[x_cols]
    X = sm.add_constant(X)
    y = df[y_col]

    model = sm.OLS(y, X)
    results = model.fit()

    return results

def main():
    st.title("Uji Serentak Regresi")

    # Mengunggah file CSV
    file = st.file_uploader("Unggah file CSV", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)

        st.subheader("Data")
        st.write(df)

        # Memilih variabel x dan y
        x_cols = st.multiselect("Pilih variabel x", options=df.columns.tolist())
        y_col = st.selectbox("Pilih variabel y", options=df.columns.tolist())

        # Menjalankan regresi
        if st.button("Jalankan Regresi"):
            results = perform_regression(df, x_cols, y_col)

            st.subheader("Hasil Regresi")
            st.write(results.summary())

if __name__ == "__main__":
    main()
