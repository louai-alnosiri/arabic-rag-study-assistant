from langchain_ollama import ChatOllama

from src.prompt import SYSTEM_PROMPT


llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.3
)


def ask_question(question, documents):

    context = ""

    if documents:
        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content