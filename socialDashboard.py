# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25  2023

@author: MaevaLavignePhilippot
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.title("Social impacts of mining and refining raw materials for battery active materials")

#img = Image.open("LCMtitle.jpg") title for LCM app
#st.image(img)

'Maeva LAVIGNE PHILIPPOT, Joeri VAN MIERLO, Maarten MESSAGIE'
'VUB, Belgium'

st.divider()

level = st.radio("What level you want to see the social risks?",["Raw material mining","Raw material refining","Active material","Cell processing"])
#level = st.radio("What level you want to see the social risks?",["Raw material mining","Raw material refining"])

legend = Image.open("Legend.PNG")

def treemapAM(df, name):
    """Returns the treemap for a cathode active material"""
    fig=px.treemap(df,path=[px.Constant(name),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    st.plotly_chart(fig, use_container_width=True)

def treemap(df, name):
    """Returns the treemap for mining or refining of raw material"""
    if df["Value"].min() == 1:
        fig=px.treemap(df,path=[px.Constant(name),'Label','Stakeholder','Subcategory','Indicator'],
               values='Area if each stakeholder has the same weight',
               color='Value',
               color_continuous_scale=['rgb(0, 102, 51)', "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    if df["Value"].min() == 0:
        fig=px.treemap(df,path=[px.Constant(name),'Label','Stakeholder','Subcategory','Indicator'],
               values='Area if each stakeholder has the same weight',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    #trying to hide the legend but does not work fig.update_layout(showlegend = False)
    st.plotly_chart(fig, use_container_width=True)



st.divider()

'maeva.philippot@vub.be'

'www.linkedin.com/in/maeva-lavigne-philippot'

st.divider()

logo = Image.open("AM4BAT - Brand PNG.png")
st.image(logo, width=200)

'This project has received funding from the European Union Horizon 2020 research and innovation programme under grant agreement No 101069756.'
'https://am4batproject.eu/'
flag = Image.open("EU.jpg")
st.image(flag, width=100)

