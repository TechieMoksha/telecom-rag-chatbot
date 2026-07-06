from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_DIR = "chroma_store"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

tickets_store = Chroma(
    collection_name="tickets",
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR,
)

# (Question, Expected Ticket ID)
test_cases = [
    ("Why is my mobile internet so slow?", "TK-008"),
    ("What should I do if I have no signal at home?", "TK-002"),
    ("How do I report a network outage?", "TK-015"),
    ("My calls keep dropping. What should I do?", "TK-017"),
    ("Why is my bill higher than usual?", "TK-004"),
    ("How do I get an itemised bill?", "TK-010"),
    ("My phone shows SIM not detected after a restart. What should I do?", "TK-005"),
    ("How do I activate international roaming?", "TK-012"),
    ("What is VoLTE and how do I enable it?", "TK-011"),
    ("How do I check my current data balance?", "TK-003"),
]

k = 3
correct = 0

print("=" * 70)
print("Telecom RAG Retrieval Evaluation (Recall@3)")
print("=" * 70)

for i, (question, expected_ticket) in enumerate(test_cases, start=1):

    results = tickets_store.similarity_search_with_score(question, k=k)

    retrieved_ids = [
        doc.metadata["ticket_id"]
        for doc, score in results
    ]

    hit = expected_ticket in retrieved_ids

    if hit:
        correct += 1

    print(f"\nTest Case {i}")
    print(f"Question        : {question}")
    print(f"Expected Ticket : {expected_ticket}")
    print(f"Retrieved       : {retrieved_ids}")
    print(f"Result          : {'PASS ✅' if hit else 'FAIL ❌'}")

recall = correct / len(test_cases)

print("\n" + "=" * 70)
print(f"Recall@{k}: {correct}/{len(test_cases)} = {recall:.2%}")
print("=" * 70)