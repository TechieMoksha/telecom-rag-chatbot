"""
Builds the RAG chain:
  merged retriever → prompt → Qwen3-32B on Groq → string output
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain_groq import ChatGroq

from retriever import build_retriever


SYSTEM_PROMPT = """
You are a helpful and professional telecom customer care assistant.

Your job is to help customers resolve technical issues with their mobile service.

Use ONLY the context below to answer the customer's question.

The context comes from three sources:
- FAQ entries
- Past resolved support tickets
- Telecom technical guide

Each context section includes its source information (FAQ ID, Ticket ID, or Guide Page).

Instructions:
- Use only the provided context.
- Do not make up information.
- If multiple sources support the answer, combine them naturally.
- End every answer with a **Sources** section.
- In the Sources section, list every source you used exactly as provided in the context.
- If the context does not contain enough information to answer confidently, clearly state that you do not know and recommend the customer call 611 or use the MyTelecom app.
- If the context contains NO_MATCH_FOUND, respond exactly:
  "I'm sorry, I don't know based on the available information.
   Please call 611 or use the MyTelecom app."
- If multiple sources support the answer, combine them naturally.
- End every answer with a Sources section.

Context:
{context}
"""


def _format_docs(docs: list[Document]) -> str:
    sections = []

    for doc in docs:
        source = doc.metadata.get("source", "").lower()

        if source == "faq":
            source_text = f"Source: FAQ ID: {doc.metadata.get('faq_id', 'Unknown')}"

        elif source == "ticket":
            source_text = f"Source: Ticket ID: {doc.metadata.get('ticket_id', 'Unknown')}"

        elif source == "guide":
            source_text = f"Source: Guide Page: {doc.metadata.get('page', 'Unknown')}"

        else:
            source_text = "Source: Unknown"

        sections.append(
            f"{source_text}\n\n{doc.page_content}"
        )

    return "\n\n------------------------------\n\n".join(sections)


def build_chain():
    retriever = build_retriever()

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ])

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
    )

    chain = (
        {
            "context": retriever | _format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
