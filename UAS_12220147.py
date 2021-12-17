#UAS Prokom
#Ryu Tandri Fernando 
#12220147
# import module

import pandas as pd
import json
import numpy as np
import matplotlib as lib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


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

nama=list()
tahun=list()
st.cache(allow_output_mutation=True)

#SOAL A
st.title("Bagian A ")
list_negara = df["name"].unique().tolist()
list_negara.sort()
#menggunakan selectbox
a= st.selectbox("Pilih Negara", list_negara)

if a!="":
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

if b!="" and b2:
    negara=list()
    produksi=list()
    for i in range(1,len(df)):
        if df.loc[i]['name']!="null" and df.loc[i]['tahun']==int(b):
            negara.append(df.loc[i]['name'])
            produksi.append(df.loc[i]['produksi'])
                
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
c = b

if c !="":
    negara=list()
    produksi=list()
    negara.append(df.loc[0]['name'])
    produksi.append(df.loc[0]['produksi'])
    for x in range(1,len(df)):
        if df.loc[x]['name']!="null":
            if df.loc[x]['name']==negara[len(negara)-1]:
                if produksi[len(produksi)-1]<df.loc[x]['produksi']:
                    produksi[len(produksi)-1]=df.loc[x]['produksi']
            else:
                negara.append(df.loc[x]['name'])
                produksi.append(df.loc[x]['produksi'])
    for x in range(0,len(produksi)-1):
        for y in range(x+1,len(negara)):
            if produksi[x]<produksi[y]: 
                dum=negara[x]
                dums=produksi[x]
                negara[x]=negara[y]
                produksi[x]=produksi[y]
                negara[y]=dum
                produksi[y]=dums
    df2 = pd.DataFrame(dict(Produksi = produksi[0:int(c)],nama_negara = negara[0:int(c)]))
    fig = px.bar(df2,x = "nama_negara",y = "Produksi",color = "Produksi", title = b)
    st.plotly_chart(fig)
    st.write(df2)
st.title("Bagian D")
c_input = st.button("Menampilkan Data Tiap Negara")
if c_input:
    st.dataframe(ff)
