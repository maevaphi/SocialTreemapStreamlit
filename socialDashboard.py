# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25  2023

@author: MaevaLavignePhilippot
"""
import streamlit as st
import os



st.title("Interactive Social Treemap for Batteries: Direct Social Impacts of Supplying Countries ")

#img = Image.open("LCMtitle.jpg") title for LCM app
#st.image(img)

'Maeva LAVIGNE PHILIPPOT, Daniele COSTA, Maarten MESSAGIE'
'VUB, Belgium'

st.divider()

level = st.radio("What level you want to see the social risks?",["Mining","Refining","Cell manufacturing","Use stage","Recycling"])

folder_path = "html files"

file_mapping = {
    "Mining": [
        "Mining step of NMC811 cathode.html",
        "Mining step of LNMO cathode.html"
    ],
    "Refining": [
        "Refining step of NMC811 cathode.html",
        "Refining step of LNMO cathode.html"
    ],
    "Cell manufacturing": [
        "Cell manufacturing.html"
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
    st.warning("No treemaps available for this level.")
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





st.divider()

'maeva.philippot@vub.be'

'www.linkedin.com/in/maeva-lavigne-philippot'

st.divider()


'This project has received funding from the European Union Horizon 2020 research and innovation programme under grant agreement No 101069756.'
'https://am4batproject.eu/'



