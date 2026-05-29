import streamlit as st


def show_home():

    st.markdown("""
    <div style="text-align:center;padding-top:50px;">
        <h1>📚 لخص دروسك</h1>
        <h3>اسأل أي سؤال من كتابك الدراسي واحصل على إجابة مختصرة مع المصدر</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.info(
            "ارفع كتاب PDF ثم ابدأ بطرح الأسئلة."
        )

        if st.button(
            "🚀 ابدأ الآن",
            use_container_width=True
        ):
            st.session_state.page = "upload"
            st.rerun()