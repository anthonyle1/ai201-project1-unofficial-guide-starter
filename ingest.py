import json
import uuid
import requests

from pathlib import Path
from bs4 import BeautifulSoup

# load json files downloaded from reddit 
def load_reddit_json(filepath: Path):

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    post = data[0]["data"]["children"][0]["data"]

    documents.append({
        "source": str(filepath),
        "source_type": "reddit_post",
        "author": post.get("author"),
        "title": post.get("title"),
        "text": post.get("selftext", "")
    })

    def parse_comments(comment_list):
        comments = []
        for comment in comment_list:

            if comment.get("kind") != "t1":
                continue

            c = comment["data"]

            comments.append({
                "source": str(filepath),
                "source_type": "reddit_comment",
                "author": c.get("author"),
                "text": c.get("body", "")
            })

            replies = c.get("replies")

            if isinstance(replies, dict):
                comments.extend(
                    parse_comments(
                        replies["data"]["children"]
                    )
                )
        return comments

    documents.extend(
        parse_comments(
            data[1]["data"]["children"]
        )
    )

    return documents

# load non-reddit json files (html page documents)
def load_html(url):
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for tag in soup([
        "script", "style", "nav", "footer", "header", "aside"
    ]):
        tag.decompose()

    text = soup.get_text(
        separator="\n",
        strip=True
    )

    return [{
        "source": url,
        "source_type": "webpage",
        "text": text
    }]

# wrapper to load everything at once
def load_documents():

    documents = []

    reddit_folder = Path("documents/reddit")

    for json_file in reddit_folder.glob("*.json"):
        documents.extend(
            load_reddit_json(json_file)
        )

    documents.extend(
        load_html(
            "https://www.swamprentals.com/help-finding-apartments/off-campus-vs-dorm"
        )
    )

    documents.extend(
        load_html(
            "https://www.ratemydorm.com/ranking-dorms/university-of-florida"
        )
    )

    documents.extend(
        load_html(
            "https://residencehalls.alligator.org"
        )
    )

    return documents


def generate_chunks(
    text,
    doc,
    chunk_size=1000,
    overlap=200,
    min_length=50
):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "chunk_id": str(uuid.uuid4()), # utilize uuid for unique ids for chromadb
                "text": chunk_text,
                "source": doc["source"],
                "source_type": doc["source_type"],
                "author": doc.get("author"),
                "title": doc.get("title")
            })

        start += chunk_size - overlap
    return chunks

# wrapper function for chunks
def chunk_document(doc):
    source_type = doc["source_type"]

    # utilize fixed chunking for reddit related espec comments since they're already short
    if source_type == "reddit_comment":

        text = (
            f"Comment by {doc.get('author', 'unknown')}\n\n"
            f"{doc.get('text', '')}"
        ).strip()

        if len(text) >= 1200:
            return generate_chunks(
                text,
                doc,
                chunk_size=1000,
                overlap=200
            )
        else: 
            return [{
                "chunk_id": str(uuid.uuid4()),
                "text": text,
                "source": doc["source"],
                "source_type": source_type,
                "author": doc.get("author"),
                "title": None
            }]
        
    elif source_type == "reddit_post":

        text = (
            f"Title: {doc.get('title', '')}\n"
            f"Author: {doc.get('author', '')}\n\n"
            f"{doc.get('text', '')}"
        )

        # Keep short posts intact
        if len(text) < 1000:
            return [{
                "chunk_id": str(uuid.uuid4()),
                "text": text,
                "source": doc["source"],
                "source_type": source_type,
                "author": doc.get("author"),
                "title": doc.get("title")
            }]

        return generate_chunks(
            text,
            doc
        )

    else:
        return generate_chunks(
            doc["text"],
            doc
        )

def ingest():
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    all_chunks = []

    for doc in documents:
        all_chunks.extend(
            chunk_document(doc)
        )

    print(f"Generated {len(all_chunks)} chunks.")

    return all_chunks

def main():
    chunks = ingest()
    print("\nFirst 5 chunks:\n")

    for chunk in chunks[:5]:
        print("=" * 80)
        print(f"ID: {chunk['chunk_id']}")
        print(f"TYPE: {chunk['source_type']}")
        print(f"SOURCE: {chunk['source']}")
        print()

        preview = chunk["text"][:400]

        print(preview)
        print()

if __name__ == "__main__":
    main()