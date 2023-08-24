# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25  2023

@author: MaevaLavignePhilippot
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#st.title("Social impacts of mining raw materials for battery active materials")

img = Image.open("LCMtitle.jpg")
st.image(img)

'Maeva LAVIGNE PHILIPPOT, Joeri VAN MIERLO, Maarten MESSAGIE'
'VUB, Belgium'


df = pd.DataFrame({
    'first column': ['NMC622 (LiNi0.8Mn0.1Co0.1O2)', 'NMC811 (LiNi0.8Mn0.1Co0.1O2)', 'LNMO (Li2NiMn3O8)', 'all'],
    'second column': [1, 2, 3, 4]
    })

option = st.selectbox(
    'Which cathode active material do you want to visualize?',
     df['first column'])

'You selected: ', option

NMC622 = pd.read_csv("NMC622Treemap.csv")
NMC811 = pd.read_csv("NMC811Treemap.csv")
LNMO = pd.read_csv("LNMOTreemap.csv")

if option == "NMC622 (LiNi0.8Mn0.1Co0.1O2)":
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
if option == "NMC811 (LiNi0.8Mn0.1Co0.1O2)":
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
if option == "LNMO (Li2NiMn3O8)":
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


with st.expander("What the area size shows for the material and the country?"):
    st.write("The size of the areas indicates the material content and the country s market share for mining.")
    st.write("The material content")
    st.write("The market share of the mining countries of 5 raw materials (cobalt, lithium, manganese and nickel) is gathered from the latest US Geological Survey.")

with st.expander("What the area size shows for the stakeholders?"):
    st.write("Each stakeholder is allocated to the same area, even though the number of indicators is different.")

with st.expander("What are the colors for?"):    
    st.write("The indicators in PSILCA database are affected 6 level of risks from no risk (blue) to very high risk (red).")
    legend = Image.open("legend.png")
    st.image(legend)

with st.expander("References"):    
    st.write("U.S. Geological Survey, 2022. Mineral Commodity Summaries 2022. https://doi.org/10.3133/mcs2022")
    st.write("Maister, K., Di Noi, C., Ciroth, A., Srocka, M., 2020. PSILCA v.3")

'maeva.philippot@vub.be'

'www.linkedin.com/in/maeva-lavigne-philippot'

st.divider()

logo = Image.open("AM4BAT - Brand PNG.png")
st.image(logo, width=200)

'This project has received funding from the European Union Horizon 2020 research and innovation programme under grant agreement No 101069756.'
flag = Image.open("EU.jpg")
st.image(flag, width=100)
