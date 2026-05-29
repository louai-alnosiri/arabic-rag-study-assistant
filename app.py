import streamlit as st

from ui.home import show_home
from ui.upload import show_upload
from ui.chat import show_chat

st.set_page_config(
    page_title="لخص دروسك",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "page" not in st.session_state:
    st.session_state.page = "home"

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

css = """
<style>

.stApp{
    background:#F8FAFC;
}

[data-testid="stSidebar"]{
    background:#111827;
}

[data-testid="stSidebar"] *{
    color:white;
}

.stButton > button{
    border-radius:12px;
    height:48px;
    font-weight:bold;
}

.block-container{
    padding-top:2rem;
}

</style>
"""

st.markdown(css, unsafe_allow_html=True)

if st.session_state.page == "home":
    show_home()

elif st.session_state.page == "upload":
    show_upload()

elif st.session_state.page == "chat":
    show_chat()