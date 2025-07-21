# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 16:54:18 2025

@author: Kirti
"""

import streamlit as st
import pandas as pd
from scraper import get_leads

st.title("Founder Lead Generation Web App")
st.write("Quickly extract SaaS company leads with contacts and LinkedIn profiles.")

keyword = st.text_input("Enter Target Industry/Keyword", "SaaS companies")
location = st.text_input("Enter Location", "Bangalore")
results_count = st.slider("Number of Leads", 5, 50, 10)

if st.button("Generate Leads"):
    st.info("Scraping leads... please wait.")
    leads = get_leads(keyword, location, results_count)
    df = pd.DataFrame(leads)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="founder_leads.csv", mime='text/csv')
