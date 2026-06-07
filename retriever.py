import chromadb
from sentence_transformers import SentenceTransformer
import ingest

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "uf_housing"

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Persistent database
client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

def build_vector_store(chunks):
    if not chunks:
        print("No chunks found.")
        return

    texts = [chunk["text"] for chunk in chunks]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    ).tolist()

    ids = [
        f"{chunk['source']}_{chunk['chunk_id']}"
        for chunk in chunks
    ]

    metadatas = [
        {
            "source": chunk["source"],
            "chunk_position": chunk["chunk_id"]
        }
        for chunk in chunks
    ]

    # Remove old data to avoid duplicates
    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(ids=existing["ids"])

    except Exception:
        pass

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks.")


def retrieve(query, k=4):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results

def print_results(query, k=4):
    results = retrieve(query, k)

    print("\n" + "=" * 80)
    print(f"QUERY: {query}")
    print("=" * 80)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for rank, (doc, meta, dist) in enumerate(
        zip(documents, metadatas, distances),
        start=1
    ):
        print(f"\nRank #{rank}")
        print(f"Source: {meta['source']}")
        print(f"Chunk Position: {meta['chunk_position']}")
        print(f"Distance: {dist:.4f}")
        print("\nChunk:")
        print(doc)
        print("-" * 80)

def evaluate():
    evaluation_queries = [
        "What are the most popular off-campus housing options for studnets?",
        # "What are the cons of living off-campus student apartments?",
        # "What are the disadvantages of living off campus as a freshman??"
    ]

    for query in evaluation_queries:
        print_results(query, k=4)

if __name__ == "__main__":

    print("Loading chunks...")
    chunks = ingest.ingest()

    print(f"Loaded {len(chunks)} chunks.")

    build_vector_store(chunks)

    evaluate()