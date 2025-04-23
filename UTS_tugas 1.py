#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Parameter distribusi Poisson
lambda_ = 8  # Rata-rata pelanggan setiap jam
n_trials = 43200 # Jumlah jam yang disimulasikan

# Generate data dari distribusi Poisson
data = poisson.rvs(lambda_, size=n_trials)

# Hitung frekuensi hasil
unique, counts = np.unique(data, return_counts=True)
freq = dict(zip(unique, counts))

# Visualisasi
plt.bar(unique, counts, color='purple')
plt.title('Simulasi Kedatangan Pelanggan di Gerai Makanan Cepat Saji')
plt.xlabel('Jumlah Kedatangan Pelanggan')
plt.ylabel('Frekuensi')
plt.show()


# In[ ]:





# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

# Baca file Excel
df_nasabah = pd.read_excel("loan_data_set.xlsx")

# Hapus spasi di awal/akhir pada nama kolom
df_nasabah.columns = df_nasabah.columns.str.strip()

# Tampilkan informasi dasar dataset
print("=== 5 Baris Pertama dari Dataset ===")
print(df_nasabah.head(), "\n")

# 1. Nasabah menikah dan tanggungan > 1
married_dependents = df_nasabah[(df_nasabah['Marital Status'] == 'Married') & (df_nasabah['Dependents'] > 1)]
prob_on_time_married = married_dependents['Loan Status'].value_counts(normalize=True)

print("1. Probabilitas bersyarat (menikah dan tanggungan > 1):")
print(prob_on_time_married, "\n")

# 2. Nasabah di area perkotaan & income di atas rata-rata
avg_income = df_nasabah['Income'].mean()
urban_high_income = df_nasabah[(df_nasabah['Housing Area'] == 'Urban') & (df_nasabah['Income'] > avg_income)]
prob_on_time_urban = urban_high_income['Loan Status'].value_counts(normalize=True)

print("2. Probabilitas bersyarat (perkotaan & income > rata-rata):")
print(prob_on_time_urban, "\n")

# 3. Visualisasi distribusi berdasarkan jenjang pendidikan
edu_loan_dist = df_nasabah.groupby(['Education Level', 'Loan Status']).size().unstack().fillna(0)
edu_loan_prob = edu_loan_dist.div(edu_loan_dist.sum(axis=1), axis=0)

edu_loan_prob.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('Distribusi Probabilitas Pinjaman Tepat Waktu per Jenjang Pendidikan')
plt.xlabel('Jenjang Pendidikan')
plt.ylabel('Probabilitas')
plt.legend(title='Loan Status')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[ ]:




