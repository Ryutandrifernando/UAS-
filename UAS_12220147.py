#UAS Prokom
#Ryu Tandri Fernando 
#12220147
#import

import pandas as pd
import json
import numpy as np
import matplotlib as lib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

#data load
fhand = open('kode_negara_lengkap.json')
data = json.load(fhand)
st.title("Tubes Prokom Ryu Tandri Fernando ")
df = pd.read_csv('produksi_minyak_mentah.csv')

#Dibuat 3 list untuk variabel berbeda
negara=list()
negara1=list()
negara2=list()

for x in df['kode_negara']:
    flag = 0
    for y in data:
        if y['alpha-3']==x:
            flag=1
            negara.append(y['name'])
            negara1.append(y['region'])
            negara2.append(y['sub-region'])
            break
    if flag==0:
        negara.append("null")
        negara1.append("null")
        negara2.append("null")
print(len(negara))
df['name'] = negara
df['region'] = negara1
df['sub-region'] = negara2
ff=df

#LISt
nama=list()
tahun=list()


#SOAL A
st.title("Bagian A ")
list_negara = df["name"].unique().tolist()
list_negara.sort()
#menggunakan selectbox
a= st.selectbox("Pilih Negara", list_negara)


for o in range(0,len(df)):
    if(df.loc[o]['name'] == a):
        nama.append(df.loc[o]['produksi'])
        tahun.append(df.loc[o]['tahun'])
df1 = pd.DataFrame(dict(Produksi = nama,Tahun = tahun))
fig = px.bar(df1,x = "Tahun",y = "Produksi",color = "Produksi", title = a)
st.plotly_chart(fig)
st.write(df1)

#SOAL B 
st.title("Bagian B")
b = st.selectbox("Pilih tahun", range(1971, 2016), 44)
b2 = st.text_input("Input Banyak Negara ")

st.write(b)

if b2 and b!="" :
    negara=list()
    produksi=list()
    for i in range(1,len(df)):
        if df.loc[i]['tahun']==int(b) and df.loc[i]['name']!="null":
            negara.append(df.loc[i]['name'])
            produksi.append(df.loc[i]['produksi'])     
#Loop untuk mengurutkan 
    for i in range(0,len(produksi)-1):
        for n in range(i+1,len(negara)):
            if produksi[i]<produksi[n]:
                dum=negara[i]
                dums=produksi[i]
                negara[i]=negara[n]
                produksi[i]=produksi[n]
                negara[n]=dum
                produksi[n]=dums
    dfb = pd.DataFrame(dict(Produksi = produksi[0:int(b2)],nama_negara = negara[0:int(b2)]))

    fig = px.bar(dfb,x = "nama_negara",y = "Produksi",color = "Produksi",title = b)
    st.plotly_chart(fig)
    st.write(dfb)

#SOAL C
st.title("Bagian C")
c = st.text_input("Jumlah Negara (Mencari Produksi Maksimum tidap negara)")

if c !="":
    for x in range(1,len(df)):
        if df.loc[x]['name']!="null":
            if df.loc[x]['name']==negara[len(negara)-1]:
                produksi[len(produksi)-1]+=df.loc[x]['produksi']
            else:
                negara.append(df.loc[x]['name'])
                produksi.append(df.loc[x]['produksi'])
    for i in range(0,len(produksi)-1):
        for n in range(i+1,len(negara)):
            if produksi[i]<produksi[n]:
                dum=negara[i]
                dums=produksi[i]
                negara[i]=negara[n]
                produksi[i]=produksi[n]
                negara[n]=dum
                produksi[n]=dums
    dfc = pd.DataFrame(dict(Produksi = produksi[0:int(c)],nama_negara = negara[0:int(c)]))
    figc = px.bar(dfc,x = "nama_negara",y = "Produksi",color="Produksi", title = "Negara produksi Terbesar")
    st.plotly_chart(figc)
    st.write(dfc)




#SOAL D
st.title("Bagian D")

st.dataframe(ff)

tahun = b

total= df.groupby(['name', 'kode_negara', 'region', 'sub-region'])['produksi'].sum()
total =total.reset_index().sort_values(['produksi'], ascending=[0])
total = total.reset_index(drop=True)
totalmax = total[["name","kode_negara","region","sub-region","produksi"]].iloc[0]

produksipertahun = df[(df["tahun"] == tahun)][['name', 'kode_negara','region','sub-region','produksi']].sort_values(by=['produksi'])
produksimax = produksipertahun[["name","kode_negara","region","sub-region","produksi"]].iloc[0]
jumlah = produksipertahun[(produksipertahun["produksi"]>0)].iloc[0]

st.markdown(f"""Negara dengan total produksi keseluruhan tahun terbesar adalah Negara {totalmax["name"]} """)
st.markdown("Dengan rincian  : ")
st.markdown(f"""
    Kode negara= {totalmax["kode_negara"]}\n
    Region = {totalmax["region"]}\n
    Sub region = {totalmax["sub-region"]}\n
    Jumlah produksi= {totalmax["produksi"]}\n""")
    
st.markdown(f"""Negara dengan jumlah produksi terbesar pada tahun {tahun} adalah Negara {produksimax["name"]} """  )
st.markdown("Dengan rincian  : ")
st.markdown(f"""
    Kode negara= {produksimax["kode_negara"]}\n
    Region = {produksimax["region"]}\n
    Sub region = {produksimax["sub-region"]}\n
    Jumlah produksi= {jumlah["produksi"]}\n""")

totalmin =  total[["name","kode_negara","region","sub-region","produksi"]].iloc[-1]
jumlahmin = total[(total["produksi"] > 0)].iloc[-1]

produksimin = produksipertahun[["name","kode_negara","region","sub-region"]].iloc[-1]   
produksimin = produksipertahun[(produksipertahun["produksi"] > 0)].iloc[-1]

st.markdown(f""" Negara dengan total produksi keseluruhan tahun terkecil adalah Negara {totalmin["name"]} """)
st.markdown("Dengan rincian  : ")
st.markdown(f"""
    Kode negara= {totalmin["kode_negara"]}\n
    Region = {totalmin["region"]}\n
    Sub Region = {totalmin["sub-region"]}\n
    Jumlah produksi= {jumlahmin["produksi"]}\n""")

st.markdown(f"""Negara dengan jumlah produksi terkecil pada tahun {tahun} adalah Negara {produksimin["name"]} """)  
st.markdown("Dengan rincian  : ")
st.markdown(f"""
    Kode negara= {produksimin["kode_negara"]}\n
    Region = {produksimin["region"]}\n
    Sub Region = {produksimin["sub-region"]}\n
    Jumlah produksi= {produksimin["produksi"]}\n""")
    
