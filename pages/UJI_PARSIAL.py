import streamlit as st
import pandas as pd
import statsmodels.api as sm

def perform_regression(df, x_col, y_col):
    X = df[x_col]
    X = sm.add_constant(X)
    y = df[y_col]

    model = sm.OLS(y, X)
    results = model.fit()

    return results

def perform_partial_f_test(df, x_col, y_col):
    X = df[x_col]
    X = sm.add_constant(X)
    y = df[y_col]

    model = sm.OLS(y, X)
    results = model.fit()

    # Menghapus intersep dari model
    X_no_intercept = X.drop("const", axis=1)
    model_no_intercept = sm.OLS(y, X_no_intercept)
    results_no_intercept = model_no_intercept.fit()

    # Menghitung F-statistic dan p-value uji parsial intersep dan slope
    f_statistic_intercept = (results.rsquared - results_no_intercept.rsquared) / results_no_intercept.df_model
    p_value_intercept = results.f_pvalue
    f_statistic_slope = results.fvalue
    p_value_slope = results.f_pvalue

    return f_statistic_intercept, p_value_intercept, f_statistic_slope, p_value_slope

def main():
    st.title("Uji Parsial Intersep dan Slope")

    # Mengunggah file CSV
    file = st.file_uploader("Unggah file CSV", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)

        st.subheader("Data")
        st.write(df)

        # Memilih variabel x dan y
        x_col = st.selectbox("Pilih variabel x", options=df.columns.tolist())
        y_col = st.selectbox("Pilih variabel y", options=df.columns.tolist())

        # Menjalankan regresi
        if st.button("Jalankan Regresi"):
            results = perform_regression(df, x_col, y_col)

            st.subheader("Hasil Regresi")
            st.write(results.summary())

            # Menjalankan uji parsial intersep dan slope
            if st.button("Jalankan Uji Parsial"):
                f_stat_intercept, p_value_intercept, f_stat_slope, p_value_slope = perform_partial_f_test(df, x_col, y_col)

                st.subheader("Hasil Uji Parsial")
                st.write("Uji Parsial Intersep:")
                st.write("F-Statistic: {:.4f}".format(f_stat_intercept))
                st.write("P-value: {:.4f}".format(p_value_intercept))
                st.write("Uji Parsial Slope:")
                st.write("F-Statistic: {:.4f}".format(f_stat_slope))
                st.write("P-value: {:.4f}".format(p_value_slope))

if __name__ == "__main__":
    main()
