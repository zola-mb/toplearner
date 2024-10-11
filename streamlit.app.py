#Import steps here
    #Import libraries
    #Import data
    #Run calculations
    #Create graphs
    #Visualise on streamlit

#Import libraries
import pandas as pd
import openpyxl as py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

#Landing page
st.set_page_config(page_title="Top Learner Data", page_icon=":student:", layout="centered")
st.title("TOP LEARNER DATA")
img_contact_form = Image.open("Walmer High School - Masinyusane x Standard Bank (23 August 2024) (14).jpg")
st.image(img_contact_form, use_column_width=True)
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

st.write("---")

#Import data
df = pd.read_excel("2025 Top Learner  High School - Main 20240912 (2).xlsx", sheet_name="Other Universities")
hs = pd.read_excel("2025 Top Learner  High School - Main 20240912 (2).xlsx", sheet_name="High School")
#Raw data
#st.header("Raw Data")
#df

#st.dataframe(hs)
#Top Learners by Gender
st.subheader("Stats on Top Learners")

#Number of schools
#st.subheader("Number of learners per High School")
schools_df = df["School"].value_counts().reset_index()
schools_df.columns = ['School', 'Count']
fig = px.bar(schools_df, x='School', y='Count', title='TLs per School')
st.plotly_chart(fig)

intake = hs["Intake"].value_counts().reset_index()
fig_intake = px.bar(intake, x="Intake", y="count", title="TLs by Intake")
st.plotly_chart(fig_intake)
intake

gender = hs["Gender"].value_counts().reset_index()
fig_gender = px.bar(gender, x="Gender", y="count", title="TLs by Gender")
st.plotly_chart(fig_gender)
gender

#Top Learners by Region
region = hs["Region"].value_counts().reset_index()
fig_region = px.bar(region, x="Region", y="count", title="TLs by Region")
st.plotly_chart(fig_region)
region

#TL Houses
house = hs["House Type"].value_counts().reset_index()
fig_house = px.bar(house, x="House Type", y="count", title="TL Houses")
st.plotly_chart(fig_house)
house

#TLs Living with their Father
live_mother = hs["Live with Mother"].value_counts().reset_index()
fig_mother = px.bar(live_mother, x="Live with Mother", y="count", title="TLs who live with their mother")
st.plotly_chart(fig_mother)
live_mother

#TLs Living with their Father
live_father = hs["Live with Father"].value_counts().reset_index()
fig_father = px.bar(live_father, x="Live with Father", y="count", title="TLs who live with their father")
st.plotly_chart(fig_father)
live_father

#Financial Support
financial_support = hs["Financial Support Type"].value_counts().reset_index()
fig_financial_support = px.bar(financial_support, x="Financial Support Type", y="count", title="TLs' Source of Financial Support")
st.plotly_chart(fig_financial_support)
financial_support

st.write("---")

#Applications
#st.header("University Applications")

#filter to show TLs who have applications to the four universities
applications = df.loc[
    (df["NMU Applied For"] == "Yes") |
    (df["CPUT Applied for"] == "Yes") |
    (df["UWC Applied for"] == "Yes") |
    (df["UJ Applied for"] == "Yes")
]

#group the above by mentor
mentor = applications.groupby("Mentor")[["NMU Applied For", "CPUT Applied for", "UWC Applied for", "UJ Applied for"]].apply(lambda x: (x == "Yes").sum()).reset_index()

# Create a dictionary with university names and counts
nmu_count = (applications["NMU Applied For"] == "Yes").sum()
cput_count = (applications["CPUT Applied for"] == "Yes").sum()
uwc_count = (applications["UWC Applied for"] == "Yes").sum()
uj_count = (applications["UJ Applied for"] == "Yes").sum()

application_counts = {
    'University': ['NMU', 'CPUT', 'UWC', 'UJ'],
    'Application Count': [nmu_count, cput_count, uwc_count, uj_count]
}

# Convert the dictionary into a dataframe
df_application_counts = pd.DataFrame(application_counts)

# Display the dataframe
st.subheader("Stats on University Applications")

# Create a bar chart for application counts
fig_applications = px.bar(df_application_counts, x='University', y='Application Count', title='Total Applications per University')
st.plotly_chart(fig_applications)
df_application_counts

#Show on streamlit
#st.subheader("Applications by Mentor")
mentor['Total Applications'] = mentor[['NMU Applied For', 'CPUT Applied for', 'UWC Applied for', 'UJ Applied for']].sum(axis=1)
fig_mentor_total = px.bar(mentor, x='Mentor', y='Total Applications', title='Total Applications by Mentor')
st.plotly_chart(fig_mentor_total)
st.dataframe(mentor)

fig_mentor_universities = go.Figure()
fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['NMU Applied For'], name='NMU'))
fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['CPUT Applied for'], name='CPUT'))
fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['UWC Applied for'], name='UWC'))
fig_mentor_universities.add_trace(go.Bar(x=mentor['Mentor'], y=mentor['UJ Applied for'], name='UJ'))

# Update layout for stacked bars
fig_mentor_universities.update_layout(
    barmode='stack',  # This will stack the bars on top of each other
    title='Applications by Mentor for Each University',
    xaxis_title='Mentor',
    yaxis_title='Number of Applications',
    legend_title='University'
)
st.plotly_chart(fig_mentor_universities)

st.dataframe(mentor)
