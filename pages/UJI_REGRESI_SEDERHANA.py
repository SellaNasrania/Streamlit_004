import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

st.title ('STATISTIC APP')

n1 = st.number_input('input jumlah data', min_value=2)
df = pd.DataFrame(columns=range(1,3), index=range(1,n1+1), dtype=float)
df.columns = ['X','Y']
df_input = st.experimental_data_editor(df, use_container_width=True)

print(df_input)


# SCATTER PLOT
fig, ax = plt.subplots()
ax.scatter(df_input['X'], df_input['Y'])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Scatter Plot')
st.pyplot(fig)

# ALTERNATIF KAK JESS
# fig = plt.figure(figsize=(10, 4))
# sns.lmplot(x="X", data=df_input, y="Y")
# st.pyplot(fig)

# KORELASI 
corr = np.corrcoef(df_input['X'],df_input['Y'])
st.write("Koefisien korelasi pearson: ",corr[0,1])

# REGRESI
reg_model = sm.OLS(df_input.Y,sm.add_constant(df_input.X))
reg_result = reg_model.fit()
st.write(reg_result.summary())
st.write(reg_result.params[0]) 
# menampilkan konstanta (angka) 
# parameter regresi (konstanta B0 dan B1)
# index 0 konstanta index 1 kemiringan

B0 = round(reg_result.params[0],3)
B1 = round(reg_result.params[1],3)
st.write("Jadi berdasarkan varibel diatas, diperoleh persamaan regresi sebagai berikut")
Model = "y = {} + {}x".format(B0,B1)
st.write(Model)
st.write("artinya jika x bertambah satu satuan maka y akan bertambah/berkurang sebesar {}".format(B1))
