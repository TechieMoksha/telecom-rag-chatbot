"""
Builds a merged retriever across all three Chroma collections:
  - faq     : FAQ entries (no chunking — 1 row = 1 doc)
  - tickets : resolved support tickets (no chunking — 1 ticket = 1 doc)
  - guides  : PDF guide chunks (RecursiveCharacterTextSplitter applied at ingest)
"""
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document

CHROMA_DIR  = "chroma_store"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def build_retriever(
    k_faq: int = 3,
    k_tickets: int = 3,
    k_guides: int = 3,
) -> RunnableLambda:
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    faq_store = Chroma(
        collection_name="faq",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    tickets_store = Chroma(
        collection_name="tickets",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    guides_store = Chroma(
        collection_name="guides",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    THRESHOLD = 1.0

    def retrieve(query: str) -> list[Document]:
        results = []

        results.extend(
            faq_store.similarity_search_with_score(query, k=k_faq)
        )

        results.extend(
            tickets_store.similarity_search_with_score(query, k=k_tickets)
        )

        results.extend(
            guides_store.similarity_search_with_score(query, k=k_guides)
        )

        results.sort(key=lambda x: x[1])

        if not results:
            return [
                Document(
                    page_content="NO_MATCH_FOUND",
                    metadata={"source": "fallback"}
                )
            ]

        best_score = results[0][1]

        if best_score > THRESHOLD:
            return [
                Document(
                    page_content="NO_MATCH_FOUND",
                    metadata={"source": "fallback"}
                )
            ]

        return [doc for doc, score in results]

    return RunnableLambda(retrieve)
