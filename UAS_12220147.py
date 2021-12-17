# import module

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import json
import pandas as pd

f = open('kode_negara_lengkap.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
st.title("Tubes Prokom ")
df = pd.read_csv('produksi_minyak_mentah.csv')
negara=list()
negara1=list()
negara2=list()
for x in df['kode_negara']:
    p=0
    for y in data:
        if y['alpha-3']==x:
            p=1
            negara.append(y['name'])
            negara1.append(y['region'])
            negara2.append(y['sub-region'])
            break
    if p==0:
        negara.append("N/A")
        negara1.append("N/A")
        negara2.append("N/A")
print(len(negara))
df['name'] = negara
df['region'] = negara1
df['sub-region'] = negara2
ff=df
# Closing file
f.close()
# Title
#st.title("Hello GeeksForGeeks !!!")
nama=list()
tahun=list()
st.cache(allow_output_mutation=True)


a_input = st.text_input("Input Nama Negara (Menampilkan Grafik Produksi perTahun Pada Suatu Negara)")

if a_input!="":
    
    for x in range(0,len(df)):
        if(df.loc[x]['name'] == a_input):
            nama.append(df.loc[x]['produksi'])
            tahun.append(df.loc[x]['tahun'])
    df1 = pd.DataFrame(dict(
        Produksi = nama,
        Tahun = tahun
        ))

    fig = px.bar(        
            df1, #Data Frame
            x = "Tahun", #Columns from the data frame
            y = "Produksi",
            title = a_input
        )

    st.plotly_chart(fig)

b_input = st.text_input("Input Tahun (Menampilkan Grafik Produksi perNegara Pada Suatu Tahun)")
b_b_input = st.text_input("Input Banyak Negara ")

if b_input!="" and b_b_input:
    negara=list()
    produksi=list()
    for x in range(1,len(df)):
        if df.loc[x]['name']!="N/A" and df.loc[x]['tahun']==int(b_input):
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
    df1 = pd.DataFrame(dict(
        Produksi = produksi[0:int(b_b_input)],
        nama_negara = negara[0:int(b_b_input)]
        ))

    fig = px.bar(        
            df1, #Data Frame
            x = "nama_negara", #Columns from the data frame
            y = "Produksi",
            title = b_input
        )

    st.plotly_chart(fig)


c_input = st.text_input("Jumlah Negara (Mencari Produksi Maksimum tidap negara)")


if c_input !="":
    negara=list()
    produksi=list()
    negara.append(df.loc[0]['name'])
    produksi.append(df.loc[0]['produksi'])
    for x in range(1,len(df)):
        if df.loc[x]['name']!="N/A":
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
    df1 = pd.DataFrame(dict(
        Produksi = produksi[0:int(c_input)],
        nama_negara = negara[0:int(c_input)]
        ))

    fig = px.bar(        
            df1, #Data Frame
            x = "nama_negara", #Columns from the data frame
            y = "Produksi",
            title = b_input
        )

    st.plotly_chart(fig)


c_input = st.button("Menampilkan Data Tiap Negara")
if c_input:
    st.dataframe(ff)
