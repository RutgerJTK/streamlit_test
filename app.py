import streamlit as st
import pandas as pd
import seaborn as sns

# This sets the page title and a cute favicon
st.set_page_config(page_title="Squirrel Census", page_icon="🐿")

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df = df.fillna("None")
    return df

data = load_data("data/squirrel_census.csv")


st.title("The Central Park Squirrel Census🐿")
st.image("data/central_park.jpg")
st.markdown(
    """As part of the [Squirrel Census](https://www.thesquirrelcensus.com/) in 2018, 
     volunteers counted all squirrels in Central Park and recorded features like their
     color, where they were sighted and whether they were doing anything interesting at
     that time. Strangely, this was the first time anyone had ever attempted anything 
     like this. The results? Central Park is the home of **3023 squirrels**, most of 
     which are gray! A few of them must be especially fast, since the Census volunteers 
     weren't even able to see what color they had 🐿💨"""
)

# Set a few custom parameters to make our plot blend in with the white background
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)
sns.color_palette("Set2")

# Plot the fur data using Seaborn's countplot
fig, ax = sns.subplots(figsize=(10, 5))
ax = sns.countplot(data["Primary Fur Color"])

st.pyplot(fig)