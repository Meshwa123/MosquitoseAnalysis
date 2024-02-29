import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Mosquitoe" ,page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Mosquito Data Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# Load data from the CSV file
data = pd.read_csv('Mosquitoes.csv')
st.subheader(":pencil: Dataset")
st.write(data)

# Check for missing values and fill if needed
data.fillna(0, inplace=True)

data.rename(columns={'2021 (Prov till 5th Dec.) - Dengue - Cases': '2021 - Dengue - Cases'},
                     inplace=True)
data.rename(columns={'2021 (Prov till 5th Dec.) - Chikungunya - Suspected': '2021 - Chikungunya - Suspected'},
                     inplace=True)
data.rename(columns={'2021 (Prov till 5th Dec.) - Chikungunya - Confirmed': '2021 - Chikungunya - Confirmed'},
                     inplace=True)
# Display missing values
st.subheader(":slot_machine: Missing Values")
st.write(data.isnull().sum())

# Subset the data
df = data.iloc[0:37, :]

# Set the style for the Streamlit app
sns.set(style="darkgrid")

# Display summary statistics
st.subheader(":chart: Summary Statistics")
st.write(data.describe())

st.subheader(":earth_asia: Statewise Analysis")
# Sidebar for state selection
selected_state = st.sidebar.selectbox(":earth_asia: Select a State", data["State/UT"].unique())
visualization_option = st.sidebar.selectbox(":chart_with_downwards_trend: Select a Visualization", 
                                    ["Bar Plot - Dengue Cases", 
                                     "Bar Plot - Chikungunya - Suspected",
                                     "Bar Plot - Chikungunya - Confirmed"])
selected_year = st.sidebar.selectbox(':calendar: Select Year', ['2018', '2019', '2020', '2021'])

# Filter the data for the selected state
state_data = data[data["State/UT"] == selected_state]
# Display the data for the selected state
st.write(f"Data for {selected_state}")
st.write(state_data)

#selected states
st.subheader(f':chart_with_upwards_trend: Data Visualization of {selected_state}')
st.subheader(f':pushpin: Dengue Cases of {selected_state}')
st.bar_chart(state_data[['2018 - Dengue - Cases', '2019 - Dengue - Cases', 
                         '2020 - Dengue - Cases', '2021 - Dengue - Cases']])
st.subheader(f':pushpin: Chikungunya - Suspected Cases of {selected_state}')
st.bar_chart(state_data[['2018 - Chikungunya - Suspected', '2019 - Chikungunya - Suspected', 
                         '2020 - Chikungunya - Suspected', '2021 - Chikungunya - Suspected']])
st.subheader(f':pushpin: Chikungunya - Confirmed Cases of {selected_state}')
st.bar_chart(state_data[['2018 - Chikungunya - Confirmed', '2019 - Chikungunya - Confirmed', 
                         '2020 - Chikungunya - Confirmed', '2021 - Chikungunya - Confirmed']])

#year+diseases+state_selected

if visualization_option == "Bar Plot - Dengue Cases":
    st.subheader(f':chart_with_upwards_trend: Bar Plot - Dengue Cases : {selected_year} : {selected_state}')
    selected_year_column = f'{selected_year} - Dengue - Cases'
    selected_data = state_data[['State/UT', selected_year_column]]
    fig, ax = plt.subplots()
    ax = sns.barplot(x=selected_year_column, y='State/UT', data=selected_data,
                     hue="State/UT",palette="viridis")
    plt.xlabel('Dengue Cases')
    plt.ylabel('State/UT')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif visualization_option == "Bar Plot - Chikungunya - Suspected":
    st.subheader(f':chart_with_upwards_trend: Bar Plot - Chikungunya Suspected : {selected_year} :{selected_state}')
    selected_year_column = f'{selected_year} - Chikungunya - Suspected'
    selected_data = state_data[['State/UT', selected_year_column]]
    fig, ax = plt.subplots()
    ax = sns.barplot(x=selected_year_column, y='State/UT', data=selected_data,hue="State/UT"
                     ,palette="viridis")
    plt.xlabel('Chikungunya - Suspected Cases')
    plt.ylabel('State/UT')
    plt.xticks(rotation=45)
    st.pyplot(fig)


elif visualization_option == "Bar Plot - Chikungunya - Confirmed":
    st.subheader(f':chart_with_upwards_trend: Bar Plot - Chikungunya Confirmed : {selected_year} :{selected_state}')
    selected_year_column = f'{selected_year} - Chikungunya - Confirmed'
    selected_data = state_data[['State/UT', selected_year_column]]
    fig, ax = plt.subplots()
    ax = sns.barplot(x=selected_year_column, y='State/UT', data=selected_data,hue="State/UT"
                     ,palette="viridis")
    plt.xlabel('Chikungunya - Confirmed Cases')
    plt.ylabel('State/UT')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Data source
st.write("Data source: Your Data Source")

#year+diseases
if visualization_option == "Bar Plot - Dengue Cases":
    st.subheader(f':chart_with_downwards_trend: Bar Plot - Dengue Cases : {selected_year}')
    selected_year_column = f'{selected_year} - Dengue - Cases'
    selected_data = df[['State/UT', selected_year_column]]
    fig, ax = plt.subplots()
    ax = sns.barplot(x=selected_year_column, y='State/UT', data=selected_data,hue="State/UT"
                     ,palette="viridis")
    plt.xlabel('Dengue Cases')
    plt.ylabel('State/UT')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif visualization_option == "Bar Plot - Chikungunya - Suspected":
    st.subheader(f':chart_with_downwards_trend: Bar Plot - Chikungunya Suspected : {selected_year} ')
    selected_year_column = f'{selected_year} - Chikungunya - Suspected'
    selected_data = df[['State/UT', selected_year_column]]
    fig, ax = plt.subplots()
    ax = sns.barplot(x=selected_year_column, y='State/UT', data=selected_data,hue="State/UT"
                     ,palette="viridis")
    plt.xlabel('Chikungunya - Suspected Cases')
    plt.ylabel('State/UT')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif visualization_option == "Bar Plot - Chikungunya - Confirmed":
    st.subheader(f':chart_with_downwards_trend: Bar Plot - Chikungunya Confirmed : {selected_year} ')
    selected_year_column = f'{selected_year} - Chikungunya - Confirmed'
    selected_data = df[['State/UT', selected_year_column]]
    fig, ax = plt.subplots()
    ax = sns.barplot(x=selected_year_column, y='State/UT', data=selected_data,hue="State/UT"
                     ,palette="viridis")
    plt.xlabel('Chikungunya - Confirmed Cases')
    plt.ylabel('State/UT')
    plt.xticks(rotation=45)
    st.pyplot(fig)


# Define columns for the correlation heatmap
year_and_disease_columns = [
    "2018 - Dengue - Cases", "2018 - Chikungunya - Suspected", 
    "2018 - Chikungunya - Confirmed",
    "2019 - Dengue - Cases", "2019 - Chikungunya - Suspected", 
    "2019 - Chikungunya - Confirmed",
    "2020 - Dengue - Cases", "2020 - Chikungunya - Suspected", 
    "2020 - Chikungunya - Confirmed",
    "2021 - Dengue - Cases", 
    "2021 - Chikungunya - Suspected",
    "2021 - Chikungunya - Confirmed"
]

# Calculate the correlation matrix
correlation_matrix = df[year_and_disease_columns].corr()

# Create a heatmap for the correlation matrix
st.subheader(":nazar_amulet: Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
plt.title("Correlation Heatmap")
st.pyplot(fig)

# Create a bar plot for Dengue cases in 2019
st.subheader("Dengue Cases by State in 2019")
fig = plt.figure(figsize=(12, 6))
sns.barplot(x='2019 - Dengue - Cases', y='State/UT', 
            data=df.sort_values('2019 - Dengue - Cases', ascending=False))
plt.xlabel('Dengue Cases in 2019')
plt.ylabel('State/UT')
plt.title('Dengue Cases by State in 2019')
st.pyplot(fig)

# # Data source
# st.write("Data source: Your Data Source")

