# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25  2023

@author: MaevaLavignePhilippot
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#st.title("Social impacts of mining and refining raw materials for battery active materials")

#img = Image.open("LCMtitle.jpg") title for LCM app
#st.image(img)

'Maeva LAVIGNE PHILIPPOT, Joeri VAN MIERLO, Maarten MESSAGIE'
'VUB, Belgium'

st.divider()

level = st.radio("What level you want to see the social risks?",["Raw material mining","Raw material refining","Active material","Cell processing"])

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
    if df["Value"].min() == 0:
        fig=px.treemap(df,path=[px.Constant(name),'Label','Stakeholder','Subcategory','Indicator'],
               values='Area if each stakeholder has the same weight',
               color='Value',
               color_continuous_scale=['rgb(0, 102, 51)', "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    if df["Value"].min() == 1:
        fig=px.treemap(df,path=[px.Constant(name),'Label','Stakeholder','Subcategory','Indicator'],
               values='Area if each stakeholder has the same weight',
               color='Value',
               color_continuous_scale=["blue", "green", "yellow", "orange", "red"],
               labels={"Value":"Risk"})
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2))
    #trying to hide the legend but does not work fig.update_layout(showlegend = False)
    st.plotly_chart(fig, use_container_width=True)

if level =="Raw material mining":
    st.subheader(":blue[You can see below the social risks of the mining of raw materials]")

    cobaltM = pd.read_csv("CobaltMiningTreemap.csv")
    copperM = pd.read_csv("CopperMiningTreemap.csv")
    graphiteM = pd.read_csv("GraphiteTreemap.csv")
    lithiumM = pd.read_csv("LithiumMiningTreemap.csv")
    manganeseM = pd.read_csv("ManganeseMiningTreemap.csv")
    nickelM = pd.read_csv("NickelMiningTreemap.csv")

    with st.expander("Mining of cobalt"): 
        treemap(cobaltM,"Cobalt mining")
        st.image(legend)

    with st.expander("Mining of copper"): 
        treemap(copperM,"Copper mining")
        st.image(legend)

    with st.expander("Mining of natural graphite"):
        treemap(graphiteM,"Natural graphite mining")
        st.image(legend)

    with st.expander("Mining of lithium"):
        treemap(lithiumM,"Lithium mining")
        st.image(legend)

    with st.expander("Mining of manganese"):
        treemap(manganeseM,"Manganese mining")
        st.image(legend)

    with st.expander("Mining of nickel"):
        treemap(nickelM,"Nickel mining")
        st.image(legend)

if level =="Raw material refining":
    st.subheader(":blue[You can see below the social risks of the refining of raw materials]")

    cobaltR = pd.read_csv("CobaltRefiningTreemap.csv")
    copperR = pd.read_csv("CopperRefiningTreemap.csv")
    graphiteS = pd.read_csv("GraphiteSyntheticTreemap.csv")
    lithiumR = pd.read_csv("LithiumRefiningTreemap.csv")
    manganeseR = pd.read_csv("ManganeseRefiningTreemap.csv")
    nickelR = pd.read_csv("NickelRefiningTreemap.csv")

    with st.expander("Refining of cobalt"): 
        treemap(cobaltR,"Cobalt refining")
        st.image(legend)

    with st.expander("Refining of copper"): 
        treemap(copperR,"Copper refining")
        st.image(legend)

    with st.expander("Synthetic graphite"):
        treemap(graphiteS,"Synthetic graphite")
        st.image(legend)

    with st.expander("Refining of lithium"):
        treemap(lithiumR,"Lithium refining")
        st.image(legend)

    with st.expander("Refining of manganese"):
        treemap(manganeseR,"Manganese refining")
        st.image(legend)

    with st.expander("Refining of nickel"):
        treemap(nickelR,"Nickel refining")
        st.image(legend)
        
if level == "Active material":
    st.subheader(":blue[You can see below the social risks of the mining of raw materials for 3 battery cathode active materials]")

    NMC622 = pd.read_csv("NMC622Treemap.csv")
    NMC811 = pd.read_csv("NMC811Treemap.csv")
    LNMO = pd.read_csv("LNMOTreemap.csv")

    with st.expander("NMC622 (LiNi\u2080.\u2086Mn\u2080.\u2082Co\u2080.\u2082O\u2082)"): 
        treemapAM(NMC622,"NMC622")
        st.image(legend)    
    with st.expander("NMC811 (LiNi\u2080.\u2088Mn\u2080.\u2081Co\u2080.\u2081O\u2082)"): 
        treemapAM(NMC811,"NMC811")
        st.image(legend)
    with st.expander("LNMO (Li\u2082NiMn\u2083O\u2088)"):
        treemapAM(LNMO,"LNMO")
        st.image(legend)

if level == "Active material":
    st.write("Work in progress")

st.subheader(':blue[More info]')

with st.expander("How to navigate"):
    st.write("Click on one treemap sector to zoom in/out.")

with st.expander("Context"):
    st.write("Current trends in the cathode active material of batteries for electric vehicles point towards reducing the amount of cobalt. In fact, cobalt is a critical raw material, which supply chain raises concerns, in particular regarding human rights and child labor during mining in the Democratic Republic of Congo (DRC). Current state-of-the-art (SoA) batteries have lithium nickel manganese cobalt oxide (NMC622) as cathode active material. AM4BAT project is developing two high-performance batteries for electric vehicles, one 3D printed all solid-state battery with single crystal NMC811 and one with lithium nickel manganese oxide (LNMO) as cathode active material.")
    st.write("This study assesses whether this change in cathode active material influences the social impacts.")

with st.expander("What the area size shows for the material and the country?"):
    st.write("The size of the areas indicates the material content and the country's market share for mining.")
    st.write("The material content of each assessed chemistry is evaluated in kg/kg active material.")
    st.write("The market share of the mining countries of 4 raw materials (cobalt, lithium, manganese and nickel) is gathered from the latest US Geological Survey.")

with st.expander("What the area size shows for the stakeholders?"):
    st.write("Each stakeholder is allocated to the same area, even though the number of indicators is different.")

with st.expander("How are the indicators selected?"):    
    st.write("PSILCA database v3 has 74 qualitative and quantitative indicators. Indicators for which there is no data for at least one sector assessed are removed, as well as environmental indicators. A total of 18 indicators are selected: 4 for the local community, 6 for the society, 1 for the value chain actors and 7 for the workers.")
    indicators = pd.read_csv("Indicators.csv")
    st.table(indicators)

with st.expander("References"):    
    st.write("U.S. Geological Survey, 2022. Mineral Commodity Summaries 2022. https://doi.org/10.3133/mcs2022")
    st.write("Maister, K., Di Noi, C., Ciroth, A., Srocka, M., 2020. PSILCA v.3")
    st.write("World Bank, 2022. Graphite; artificial exports by country in 2021")

st.divider()

'maeva.philippot@vub.be'

'www.linkedin.com/in/maeva-lavigne-philippot'

st.divider()

#logo = Image.open("AM4BAT - Brand PNG.png")
#st.image(logo, width=200)

#'This project has received funding from the European Union Horizon 2020 research and innovation programme under grant agreement No 101069756.'
#'https://am4batproject.eu/'
#flag = Image.open("EU.jpg")
#st.image(flag, width=100)
