import streamlit as st

from src.vector_store import load_vector_store
from src.retriever import get_retriever
from src.rag_chain import ask_question
from src.memory import initialize_memory, clear_memory


def show_chat():

    initialize_memory()

    st.title("🤖 مساعد الدراسة")

    # ==========================
    # Sidebar
    # ==========================
    with st.sidebar:

        st.header("⚙️ الإعدادات")

        st.toggle(
            "الوضع الليلي",
            value=False
        )

        st.divider()

        if st.button(
            "➕ محادثة جديدة",
            use_container_width=True
        ):
            clear_memory()
            st.rerun()

        st.divider()

        st.subheader("📝 المحادثات السابقة")

        if "saved_chats" not in st.session_state:
            st.session_state.saved_chats = []

        if len(st.session_state.saved_chats) == 0:
            st.caption("لا توجد محادثات بعد")

        else:

            for item in reversed(
                st.session_state.saved_chats[-10:]
            ):
                st.write("•", item)

    # ==========================
    # عرض آخر سؤالين فقط
    # ==========================

    visible_messages = (
        st.session_state.chat_history[-4:]
    )

    for msg in visible_messages:

        if msg["role"] == "user":

            with st.chat_message("user"):

                st.write(
                    msg["content"]
                )

        elif msg["role"] == "assistant":

            with st.chat_message(
                "assistant"
            ):

                if isinstance(
                    msg["content"],
                    dict
                ):

                    st.markdown(
                        "### 📌 الإجابة"
                    )

                    st.write(
                        msg["content"][
                            "answer"
                        ]
                    )

                    st.divider()

                    with st.expander(

                            "📚 عرض المصدر"

                    ):
                        st.text(
                                 msg["content"]["source"][:1500]
                                )
    
                    

                   

                else:

                    st.write(
                        msg["content"]
                    )

    # ==========================
    # إدخال السؤال
    # ==========================

    question = st.chat_input(
        "اكتب سؤالك من الكتاب..."
    )

    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        st.session_state.saved_chats.append(
            question
        )

        with st.spinner(
            "جاري البحث داخل الكتاب..."
        ):

            try:

                vector_store = (
                    load_vector_store()
                )

                retriever = (
                    get_retriever(
                        vector_store
                    )
                )

                documents = (
                    retriever.invoke(
                        question
                    )
                )

                answer = (
                    ask_question(
                        question,
                        documents
                    )
                )

                source_text = ""

                for doc in documents:

                    page = (
                        doc.metadata.get(
                            "page",
                            "غير معروف"
                        )
                    )

                    source_text += (
                        f"\n📄 الصفحة {page + 1}\n"
                    )

                    source_text += (
                        doc.page_content[:500]
                    )

                    source_text += (
                        "\n\n"
                        + "=" * 40
                        + "\n\n"
                    )

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": {
                            "answer": answer,
                            "source": source_text
                        }
                    }
                )

            except Exception as e:

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content":
                        f"حدث خطأ:\n{str(e)}"
                    }
                )

        st.rerun()