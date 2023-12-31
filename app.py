import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Slack Message')
st.text('Channel Member Analysis')

upload_file = st.file_uploader("Upload your file")

if upload_file:
    df = pd.read_json(upload_file)
    st.header('Data Header')
    st.write(df.head())

    st.header('Data Analytics')
    st.write(df.describe())

    df = df[:3]
    fig, ax = plt.subplots()
    ax.plot(df['user'], df['text'])
    ax.set_xlabel('user')
    ax.set_ylabel('text')

    st.pyplot(fig)