import streamlit as st
import os

from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_vector_store


def show_upload():

    st.title("📖 رفع الكتاب")

    st.caption(
        "اختر كتاب PDF ثم اضغط تحليل الكتاب."
    )

    uploaded_file = st.file_uploader(
        "اختر ملف PDF",
        type=["pdf"]
    )

    if uploaded_file:

        os.makedirs(
            "data/books",
            exist_ok=True
        )

        file_path = os.path.join(
            "data/books",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success(
            f"تم رفع: {uploaded_file.name}"
        )

        if st.button(
            "📚 تحليل الكتاب",
            use_container_width=True
        ):

            with st.spinner(
                "جاري تحليل الكتاب..."
            ):

                documents = load_pdf(
                    file_path
                )

                chunks = split_documents(
                    documents
                )

                create_vector_store(
                    chunks
                )

            st.success(
                "تم تحليل الكتاب بنجاح"
            )

            st.session_state.page = "chat"

            st.rerun()