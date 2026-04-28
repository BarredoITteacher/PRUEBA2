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

# NAV
pagina = st.sidebar.selectbox("NAME APP", ["Inicio", "Sobre mí"])

if pagina == "Inicio":
    if st.button("Pulsa aquí"):
        st.write("Hola 👋")

elif pagina == "Sobre mí":
    st.write("Esta es otra sección de la app")

st.write("Hello E4ABD, world.")