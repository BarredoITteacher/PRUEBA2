import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: red;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("My First Streamlit App")

if st.button("Pulsa aquí"):
    st.write("Hola 👋")

st.write("Hello E4ABD, world.")