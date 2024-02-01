import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics

pd.set_option('display.max_rows', 500)

pd.set_option('display.max_columns', 500)

pd.set_option('display.width', 2000)
df = pd.read_csv('Bendraskeloniu.csv')

df['Kaina'] = pd.to_numeric(df['Kaina'], errors='coerce')

# 1.
# TOP10 POPULIARIAUSIOS KELIONES PAGAL KAINOS VIDURKI.
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
plt.savefig("Vidutinės kelionės kainos pagal TOP 10 šalių.png")
plt.show()

# #2.
# #TOP10 BRANGIAUSIOS SALYS
df_cleaned = df.dropna(subset=['Kaina', 'Regionas'])

idx = df_cleaned.groupby('Salis')['Kaina'].idxmax()
top_regions = df_cleaned.loc[idx]
top_10_expensive_regions = top_regions.sort_values(by='Kaina', ascending=False).head(10).reset_index(drop=True)

# print(top_10_expensive_regions)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(top_10_expensive_regions['Salis'], top_10_expensive_regions['Kaina'], color='skyblue')
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval,2), ha='center', va='bottom')
plt.title('Brangiausių šalių top 10')
plt.xlabel('Šalis')
plt.ylabel('Kaina')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("Brangiausių šalių top 10.png")
plt.show()


# # 3.
# # KELIONIŲ REITINGŲ PASISKIRSTYMAS PROCENTALIAI
df['Reitingas'] = pd.to_numeric(df['Reitingas'], errors='coerce').fillna(0).astype(int)
reitingas_counts = df['Reitingas'].value_counts()
# print(reitingas)

plt.figure(figsize=(8, 8))
plt.pie(reitingas_counts, labels=reitingas_counts.index.astype(int), autopct='%1.0f%%', colors=[
        'blue', 'green', 'coral', 'orange', 'red'])
plt.title('Kelionių reitingų pasiskirstymas procentaliai')
plt.legend(title= 'Reitingas',loc='upper left')
plt.savefig("Kelionių reitingų pasiskirstymas procentaliai.png")
plt.show()

# # 4.
# # KELIONIŲ TIPAI AGENTŪROSE
kelioniu_tipai_agenturoje = df.groupby(['agentura', 'Keliones tipas']).size().reset_index(name='Kiekis')
print(kelioniu_tipai_agenturoje)
custom_palette = sns.color_palette("Set1", 5)
plt.figure(figsize=(12, 6))
sns.barplot(x='agentura', y='Kiekis', hue='Keliones tipas', data=kelioniu_tipai_agenturoje, palette=custom_palette)
plt.title('Agentūrų siūlomos kelionės pagal tipus')
plt.xlabel('Agentūra')
plt.ylabel('Kiekis')
plt.legend(title='Keliones tipas')
for p in plt.gca().patches:
    height = p.get_height()
    plt.gca().text(p.get_x() + p.get_width() / 2., height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')
plt.tight_layout()
plt.savefig("Agentūrų siūlomos kelionės pagal tipus.png")
plt.show()

# # # 5.
# # #BENDRAS KELIONIŲ KIEKIS PAGAL MĖNESIUS
df = pd.read_csv('Bendraskeloniu.csv')
df['Reitingas'].fillna(df['Reitingas'].mean(), inplace=True)
df.loc[df['Kaina'] == "Išparduota", "Kaina"] = 0
df['Kaina'] = df['Kaina'].astype(int)
df_be_datos = df[df['Data'] == "Nenurodyta"]
df_su_datom = df[df['Data'] != "Nenurodyta"]
df_su_datom['Data'] = pd.to_datetime(df_su_datom['Data'])
# print(df_su_datom)

# # Konvertuoja 'Data' stulpeli i teisinga duomenu formata
df_su_datom['Data'] = pd.to_datetime(df_su_datom['Data'])
# Gauna menesio numeri is datu stulpelio
df_su_datom['Menuo'] = df_su_datom['Data'].dt.month
# print(df_su_datom['Menuo'])

# # Abieju agenturu kelioniu kiekis bendrai sudejus pagal menesius
menesinis_kelioniu_kiekis = df.groupby(df_su_datom['Menuo']).size().reset_index(name='Kelioniu kiekis')
plt.figure(figsize=(12, 6))
sns.lineplot(x='Menuo', y='Kelioniu kiekis',
             data=menesinis_kelioniu_kiekis, marker='o')
plt.title('Kelionių kiekis pagal mėnesius')
plt.xlabel('Menuo')
plt.ylabel('Kelioniu kiekis')
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("Kelionių kiekis pagal mėnesius.png")
plt.show()


# # # 6
# # #MĖNESINIS KELIONIŲ SKAIČIUS PAGAL AGENTŪRAS
df = pd.read_csv('Bendraskeloniu.csv')
df['Reitingas'].fillna(df['Reitingas'].mean(), inplace=True)
df.loc[df['Kaina'] == "Išparduota", "Kaina"] = 0
df['Kaina'] = df['Kaina'].astype(int)
df_be_datos = df[df['Data'] == "Nenurodyta"]
df_su_datom = df[df['Data'] != "Nenurodyta"]
df_su_datom['Data'] = pd.to_datetime(df_su_datom['Data'])
# print(df_su_datom)

# # Konvertuoja 'Data' stulpeli i teisinga duomenu formata
df_su_datom['Data'] = pd.to_datetime(df_su_datom['Data'])
# Gauna menesio numeri is datu stulpelio
df_su_datom['Menuo'] = df_su_datom['Data'].dt.month
# print(df_su_datom['Menuo'])
menesinis_kelioniu_kiekis_pagal_agentura = df_su_datom.groupby(['Menuo', 'agentura']).size().reset_index(name='Kelioniu kiekis')

plt.figure(figsize=(12, 6))
sns.lineplot(x='Menuo', y='Kelioniu kiekis', hue='agentura',
             data=menesinis_kelioniu_kiekis_pagal_agentura, marker='o')
plt.title('Mėnesinis kelionių kiekis pagal agentūras')
plt.xlabel('Menuo')
plt.ylabel('Kelioniu kiekis')
plt.xticks(range(1, 13))
plt.legend(title='Agentura')
for line in range(0, menesinis_kelioniu_kiekis_pagal_agentura.shape[0]):
    plt.text(menesinis_kelioniu_kiekis_pagal_agentura['Menuo'].iloc[line],
             menesinis_kelioniu_kiekis_pagal_agentura['Kelioniu kiekis'].iloc[line] + 0.2,
             menesinis_kelioniu_kiekis_pagal_agentura['Kelioniu kiekis'].iloc[line],
             horizontalalignment='center', verticalalignment='bottom', fontsize=9)
plt.tight_layout()
plt.savefig("Mėnesinis kelionių kiekis pagal agentūras.png")
plt.show()

