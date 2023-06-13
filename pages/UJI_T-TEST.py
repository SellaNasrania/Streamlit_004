import streamlit as st
import numpy as np
from scipy.stats import t

# Judul aplikasi
st.title('Uji t Satu Populasi')

# Input nilai-nilai
sample_mean = st.number_input('Rata-rata sampel', value=0.0)
population_mean = st.number_input('Rata-rata populasi', value=0.0)
sample_stddev = st.number_input('Deviasi standar sampel', value=1.0)
sample_size = st.number_input('Ukuran sampel', min_value=1, step=1, value=1)

# Menghitung nilai t-score
t_score = (sample_mean - population_mean) / (sample_stddev / np.sqrt(sample_size))

# Menghitung derajat kebebasan
df = sample_size - 1

# Menghitung p-value
p_value = 2 * (1 - t.cdf(np.abs(t_score), df))

# Menampilkan hasil
st.subheader('Hasil Uji t Satu Populasi')
st.write(f'Nilai t-Score: {t_score}')
st.write(f'Derajat Kebebasan: {df}')
st.write(f'Nilai p-Value: {p_value}')

# Menampilkan interpretasi hasil
alpha = 0.05  # Tingkat signifikansi
if p_value < alpha:
    st.write('Karena p-value lebih kecil dari alpha, maka tolak hipotesis nol.')
else:
    st.write('Karena p-value lebih besar dari alpha, maka gagal tolak hipotesis nol.')
