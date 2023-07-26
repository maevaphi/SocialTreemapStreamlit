# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25  2023

@author: MaevaLavignePhilippot
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
#import numpy as np
#from plotly.subplots import make_subplots
#import plotly.graph_objects as go
#from wordcloud import ordCloud, STOPWORDS
#import matplotlib.pyplot as plt
#import seaborn as sns

#st.title("Social impacts of mining raw materials for battery active materials")

img = Image.open("C:/Users/mphilip1_admin/OneDrive - Vrije Universiteit Brussel/thèse/python/LCMtitle.jpg")
st.image(img)

'Maeva LAVIGNE PHILIPPOT, Joeri VAN MIERLO, Maarten MESSAGIE'
'VUB, Belgium'


df = pd.DataFrame({
    'first column': ['NMC622', 'NMC811', 'LNMO', 'all'],
    'second column': [1, 2, 3, 4]
    })

option = st.selectbox(
    'Which cathode active material do you want to visualize?',
     df['first column'])

# 'You selected: ', option

NMC622 = pd.read_csv("C:/Users/mphilip1_admin/OneDrive - Vrije Universiteit Brussel/thèse/python/NMC622Treemap.csv")
NMC811 = pd.read_csv("C:/Users/mphilip1_admin/OneDrive - Vrije Universiteit Brussel/thèse/python/NMC811Treemap.csv")
LNMO = pd.read_csv("C:/Users/mphilip1_admin/OneDrive - Vrije Universiteit Brussel/thèse/python/LNMOTreemap.csv")

if option == "NMC622":
    fig=px.treemap(NMC622,path=[px.Constant("NMC622"),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    #fig.update_traces(root_color="Lightgrey")
    #fig.update_traces(name="test legend", selector=dict(type='treemap'))
    #fig.update_traces(visible=True, selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    #fig.update_layout(legend = dict (title=None, orientation="h"))
    st.plotly_chart(fig, use_container_width=True)
if option == "NMC811":
    fig=px.treemap(NMC811,path=[px.Constant("NMC811"),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_traces(root_color="Lightgrey")
    fig.update_traces(name="test legend", selector=dict(type='treemap'))
    fig.update_traces(visible=True, selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    st.plotly_chart(fig, use_container_width=True)
if option == "LNMO":
    fig=px.treemap(LNMO,path=[px.Constant("LNMO"),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_traces(root_color="Lightgrey")
    fig.update_traces(name="test legend", selector=dict(type='treemap'))
    fig.update_traces(visible=True, selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    st.plotly_chart(fig, use_container_width=True)
if option == "all":
    'NMC622'
    fig=px.treemap(NMC622,path=[px.Constant("NMC622"),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_traces(root_color="Lightgrey")
    fig.update_traces(name="test legend", selector=dict(type='treemap'))
    fig.update_traces(visible=True, selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    st.plotly_chart(fig, use_container_width=True)
    'NMC811'
    fig=px.treemap(NMC811,path=[px.Constant("NMC811"),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_traces(root_color="Lightgrey")
    fig.update_traces(name="test legend", selector=dict(type='treemap'))
    fig.update_traces(visible=True, selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    st.plotly_chart(fig, use_container_width=True)
    'LNMO'
    fig=px.treemap(LNMO,path=[px.Constant("LNMO"),'Material','Label','Stakeholder','Indicator'],
               values='Area',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_traces(root_color="Lightgrey")
    fig.update_traces(name="test legend", selector=dict(type='treemap'))
    fig.update_traces(visible=True, selector=dict(type='treemap'))
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    st.plotly_chart(fig, use_container_width=True)

'Legend:'
'NMCxyz= LiNixCoyMnzO2'
'LNMO= LiNi0.5Mn1.5O4'

'The size of the areas indicates the material amount and the country s market share. Each stakeholder is allocated to the same area, even though the number of indicators is different. The indicators in PSILCA database are affected 6 level of risks from no risk (blue) to very high risk (red).'


#email



#linkedin

st.divider()

logo = Image.open("C:/Users/mphilip1_admin/OneDrive - Vrije Universiteit Brussel/thèse/python/AM4BAT - Brand PNG.png")
st.image(logo, width=200)

'This project has received funding from the European Union Horizon 2020 research and innovation programme under grant agreement No 101069756.'
flag = Image.open("C:/Users/mphilip1_admin/OneDrive - Vrije Universiteit Brussel/thèse/python/EU.jpg")
st.image(flag, width=100)