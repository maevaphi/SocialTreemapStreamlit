# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25  2023

@author: MaevaLavignePhilippot
"""
import streamlit as st
import os



st.title("Social Life Cycle Impacts of Batteries using Interactive Social Treemaps")


'Maeva LAVIGNE PHILIPPOT, Daniele COSTA, Maarten MESSAGIE'
'VUB, Belgium'

st.divider()

level = st.radio("What level you want to see the social risks?",["Mining","Refining","Cell manufacturing","Use stage","Recycling"], index = None)

folder_path = "html files"

file_mapping = {
    "Mining": [
        "Mining step of NMC811 cathode.html",
        "Mining step of LNMO cathode.html",
        "Mining step of natural graphite anode.html"
    ],
    "Refining": [
        "Refining step of NMC811 cathode.html",
        "Refining step of LNMO cathode.html",
        "Refining step of artificial graphite anode"
    ],
    "Cell manufacturing": [
        "Cell manufacturing capacity.html"
    ],
    "Use stage": [
        "Electricity demand.html"
    ],
    "Recycling": [
        "Recycling capacity.html"
    ]
}

selected_files = file_mapping.get(level, [])

if not selected_files:
    st.warning("Select a life cycle stage.")
else:
    for file_name in selected_files:

        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):

            st.markdown(f"**{file_name.replace('.html','')}**")

            st.image("Legend.PNG", use_container_width=True)

            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            st.components.v1.html(html_content, height=700, scrolling=True)
            

        else:
            st.error(f"{file_name} not found.")


with st.expander("Data sources"):
    st.write('The market share of each mining and refining country for cobalt, copper, graphite, lithium, manganese and nickel, '
    'is based on data from the U.S. Geological Survey, the British Geological Survey (https://doi.org/10.3133/mcs2022), '
    'the market share between synthetic and natural graphite is sourced from the JRC (Clean energy technology observatory: '
    'batteries for energy storage in the European Union - 2022 status report on technology development, '
    'trends, value chains and markets) '
    'and the World Bank for synthetic graphite.' )
    st.write('For the manufacturing step of the batteries, the previous JRC publication '
    'is used to retrieve the market share of the main supplying countries.')
    st.write('For the use stage, the activity variable is the country electricity '
    'demand for electric passenger cars, which is retrieved from the IEA Global EV Outlook 2024.')
    st.write('For recycling, the activity variable is the recycling capacity in kt '
    'of cell-equivalent mass of total recyclable material at country level. '
    'This information is sourced from IEA  EV Battery Supply Chain Sustainability which shows battery recycling '
    'capacity for pretreatment and material recovery. ')
    st.write('The risk level for each country sector is extracted from PSILCA v3.1 ')


st.divider()

'maeva.philippot@vub.be'

'www.linkedin.com/in/maeva-lavigne-philippot'

st.divider()


'This work was supported by the European Union’s Horizon Europe research and innovation programme under Grant Agreement No. 101069756 (AM4BAT project) and Grant Agreement No. 101091852 (REBORN project). The authors acknowledge the European Commission and project partners for their valuable contributions. The information and views expressed in this publication are solely those of the authors and do not reflect the position of the European Union or the European Commission. Neither the European Union nor the granting authority can be held responsible for any use that may be made of the information contained herein. '



