import streamlit as st
import numpy as np
from scipy.stats import norm
import pandas as pd

# Judul aplikasi
st.title('Uji Z-Test')

# Input nilai-nilai
sample_mean = st.number_input('Rata-rata sampel', value=0.0)
population_mean = st.number_input('Rata-rata populasi', value=0.0)
sample_stddev = st.number_input('Deviasi standar sampel', value=1.0)
sample_size = st.number_input('Ukuran sampel', min_value=1, step=1, value=1)

# Menghitung nilai z-score
z_score = (sample_mean - population_mean) / (sample_stddev / np.sqrt(sample_size))

# Menghitung p-value
p_value = 2 * (1 - norm.cdf(np.abs(z_score)))

# Menampilkan hasil
st.subheader('Hasil Uji Z-Test')
st.write(f'Nilai Z-Score: {z_score}')
st.write(f'Nilai p-Value: {p_value}')

# Menampilkan interpretasi hasil
alpha = 0.05  # Tingkat signifikansi
if p_value < alpha:
    st.write('Karena p-value lebih kecil dari tingkat signifikansi (alpha), maka kita menolak hipotesis nol.')
else:
    st.write('Karena p-value lebih besar dari tingkat signifikansi (alpha), maka kita gagal menolak hipotesis nol.')
