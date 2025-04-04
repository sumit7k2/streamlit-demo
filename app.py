import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="Beautiful Streamlit App", page_icon="🌟", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Exploration", "Visualizations"])

# Home Page
if page == "Home":
    st.title("Welcome to the Beautiful Streamlit App 🌟")
    st.write("An elegant Streamlit app for interactive data visualization and exploration.")
    st.image("https://picsum.photos/800/400", use_column_width=True)
    st.write("### Features:")
    st.markdown("- Interactive Data Exploration")
    st.markdown("- Stunning Visualizations")
    st.markdown("- User-Friendly Interface")
    st.image("https://picsum.photos/600/300")

# Data Exploration Page
elif page == "Data Exploration":
    st.title("Data Exploration 🔍")
    st.image("https://picsum.photos/800/300")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        
        st.write("### Basic Statistics")
        st.write(df.describe())
        
        st.write("### Column Data Types")
        st.write(df.dtypes)

# Visualization Page
elif page == "Visualizations":
    st.title("Data Visualization 📊")
    st.image("https://picsum.photos/800/300")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"], key="viz")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        column = st.selectbox("Select a column to visualize", df.columns)
        
        chart_type = st.radio("Select Chart Type", ["Histogram", "Line Chart"])
        
        fig, ax = plt.subplots()
        
        if chart_type == "Histogram":
            sns.histplot(df[column], bins=20, kde=True, ax=ax)
        elif chart_type == "Line Chart":
            sns.lineplot(data=df[column], ax=ax)
        
        st.pyplot(fig)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Built with 🌟 using Streamlit")
