
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Netflix Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_netflix.csv")

df = load_data()

st.title("Netflix Movies & TV Shows Analysis")

# Sidebar filter
content_type = st.sidebar.multiselect("Select Type", df["type"].unique(), df["type"].unique())
df = df[df["type"].isin(content_type)]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(df))
col2.metric("Average Duration", round(df["duration"].mean(), 1))
col3.metric("Unique Countries", df["country"].nunique())

# Content by year
st.subheader("Content Release Trend")
fig, ax = plt.subplots()
df.groupby("release_year").size().plot(ax=ax)
st.pyplot(fig)

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")
fig, ax = plt.subplots()
df["type"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

# Genre distribution
st.subheader("Genre Distribution")
fig, ax = plt.subplots()
df["genre"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

# Correlation
st.subheader("Correlation Matrix")
corr = df[["release_year", "duration"]].corr()
fig, ax = plt.subplots()
im = ax.imshow(corr, cmap="coolwarm")
plt.colorbar(im)
ax.set_xticks(range(len(corr)))
ax.set_yticks(range(len(corr)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)
st.pyplot(fig)
