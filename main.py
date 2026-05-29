import streamlit as st

st.set_page_config(
    page_title="لخص دروسك",
    page_icon="📚",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "home"


def go_to_upload():
    st.session_state.page = "upload"


st.markdown(
    """
    <h1 style='text-align:center;'>
    📚 لخص دروسك
    </h1>

    <h4 style='text-align:center;'>
    اسأل أي سؤال من كتابك الدراسي واحصل على إجابة دقيقة مع المصدر
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")

col1, col2, col3 = st.columns([1,2,1])

with col2:

    if st.button(
        "ابدأ الآن",
        use_container_width=True
    ):
        go_to_upload()