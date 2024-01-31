import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
df = pd.read_csv('Bendraskeloniu.csv')


# Stulpeline diagrama rodanti vidutines keliones kaina pagal TOP 10 saliu
# TOP 10 saliu yra atrinktos pagal tos salies daznuma
saliu_kiekiai = df.groupby(['Salis']).size().reset_index(name="kiekis").sort_values(by='kiekis', ascending=False)
top_10_saliu = saliu_kiekiai.head(10)['Salis']
df_top_10_saliu = df[df['Salis'].isin(top_10_saliu)]
df_top_10_saliu['Kaina'] = pd.to_numeric(df_top_10_saliu['Kaina'], errors='coerce')
vidutine_keliones_kaina_pagal_sali = df_top_10_saliu.groupby('Salis')['Kaina'].mean().reset_index().round(2)

# print(vidutine_keliones_kaina_pagal_sali)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(vidutine_keliones_kaina_pagal_sali['Salis'], vidutine_keliones_kaina_pagal_sali['Kaina'], color='skyblue')
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval,2), ha='center', va='bottom')
plt.title('Vidutinės kelionės kainos pagal TOP 10 šalių')
plt.xlabel('Šalis')
plt.ylabel('Vidutinė kaina')
plt.xticks(rotation=45, ha='right')  # Pasukti šalių pavadinimus, kad būtų geriau matoma
plt.tight_layout()
plt.show()

