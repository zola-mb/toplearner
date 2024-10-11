import pandas as pd
import openpyxl as py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Top Learner Data", page_icon=":student:", layout="centered")

# Landing page title and image
st.title("TOP LEARNER DATA")
try:
    img_contact_form = Image.open("Walmer High School - Masinyusane x Standard Bank (23 August 2024) (14).jpg")
    st.image(img_contact_form, use_column_width=True)
except FileNotFoundError:
    st.error("Image file not found. Please make sure it is available.")

# Summary Stats
st.write("---")
text_column1, text_column2, text_column3 = st.columns(3)
with text_column1:
    st.subheader("Partner Schools")
    st.write("41")
with text_column2:
    st.subheader("Number of Top Learners")
    st.write("858")
with text_column3:
    st.subheader("Number of Applications")
    st.write("1255")

# Import data
uploaded_file = st.file_uploader("Choose an Excel file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="Other Universities")

    # Number of schools
    st.subheader("Number of learners per High School")
    schools_df = df["School"].value_counts().reset_index()
    schools_df.columns = ['School', 'Count']

    fig = px.bar(schools_df, x='School', y='Count', title='TLs per School')
    st.plotly_chart(fig)

    # Filter to show TLs who have applications to the four universities
    applications = df.loc[
        (df["NMU Applied For"] == "Yes") |
        (df["CPUT Applied for"] == "Yes") |
        (df["UWC Applied for"] == "Yes") |
        (df["UJ Applied for"] == "Yes")
    ]

    # Group by mentor and count applications
    mentor = applications.groupby("Mentor")[["NMU Applied For", "CPUT Applied for", "UWC Applied for", "UJ Applied for"]].apply(lambda x: (x == "Yes").sum()).reset_index()
    mentor['Total Applications'] = mentor[['NMU Applied For', 'CPUT Applied for', 'UWC Applied for', 'UJ Applied for']].sum(axis=1)

    # Display total applications by mentor
    fig_mentor_total = px.bar(mentor, x='Mentor', y='Total Applications', title='Total Applications by Mentor')
    st.plotly_chart(fig_mentor_total)

    # Stacked bar chart for applications by mentor per university
    fig_mentor_universities = go.Figure()
    fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['NMU Applied For'], name='NMU'))
    fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['CPUT Applied for'], name='CPUT'))
    fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['UWC Applied for'], name='UWC'))
    fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['UJ Applied for'], name='UJ'))

    fig_mentor_universities.update_layout(
        barmode='stack',
        title='Applications by Mentor for Each University',
        xaxis_title='Mentor',
        yaxis_title='Number of Applications',
        legend_title='University'
    )
    st.plotly_chart(fig_mentor_universities)

    st.dataframe(mentor)
