import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# parse already installed json files from reddit 
def load_reddit_json(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    post = data[0]["data"]["children"][0]["data"]

    documents.append({
        "source": filepath,
        "source_type": "post",
        "author": post.get("author"),
        "title": post.get("title"),
        "text": post.get("selftext", "")
    })

    def parse_comments(comment_list):
        comments = []

        for comment in comment_list:

            if comment["kind"] != "t1":
                continue

            c = comment["data"]

            comments.append({
                "source_type": "comment",
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
    # print(json.dumps(documents, indent=4))

    return documents

# pulls all text from website, concern about hallucinating + feeding unrelevant data to llm but maybe
# this is good enough
def load_html(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    
    # print(text)

    return {
        "source": url,
        "text": text
    }

# wrapper function to encompass all documents
def load_documents():
    documents = []
    # loading downlowded reddit pages
    folder = Path("documents/reddit")
    json_files = [file.name for file in folder.glob("*.json")]
    
    for json_path in json_files:
        documents.append(load_reddit_json("documents/reddit/"+json_path))

    # loading swamprentals
    documents.append(load_html("https://www.swamprentals.com/help-finding-apartments/off-campus-vs-dorm"))
    
    # loading ratemydorm
    documents.append(load_html("https://www.ratemydorm.com/ranking-dorms/university-of-florida"))

    # loading the alligator
    documents.append(load_html("https://residencehalls.alligator.org/#beaty"))
    documents.append(load_html("https://residencehalls.alligator.org/#beaty"))
    documents.append(load_html("https://residencehalls.alligator.org/#yulee"))
    documents.append(load_html("https://residencehalls.alligator.org/#cypress"))
    documents.append(load_html("https://residencehalls.alligator.org/#reid"))
    documents.append(load_html("https://residencehalls.alligator.org/#mallory"))
    documents.append(load_html("https://residencehalls.alligator.org/#broward"))
    documents.append(load_html("https://residencehalls.alligator.org/#rawlings"))
    documents.append(load_html("https://residencehalls.alligator.org/#infinity"))
    documents.append(load_html("https://residencehalls.alligator.org/#murphree"))
    documents.append(load_html("https://residencehalls.alligator.org/#buckman"))
    documents.append(load_html("https://residencehalls.alligator.org/#fletcher"))
    documents.append(load_html("https://residencehalls.alligator.org/#sledd"))
    documents.append(load_html("https://residencehalls.alligator.org/#thomas"))
    documents.append(load_html("https://residencehalls.alligator.org/#tolbert"))
    documents.append(load_html("https://residencehalls.alligator.org/#weaver"))
    documents.append(load_html("https://residencehalls.alligator.org/#east"))
    documents.append(load_html("https://residencehalls.alligator.org/#riker"))
    documents.append(load_html("https://residencehalls.alligator.org/#north"))
    documents.append(load_html("https://residencehalls.alligator.org/#graham"))
    documents.append(load_html("https://residencehalls.alligator.org/#simpson"))
    documents.append(load_html("https://residencehalls.alligator.org/#trusler"))
    documents.append(load_html("https://residencehalls.alligator.org/#keys"))
    documents.append(load_html("https://residencehalls.alligator.org/#springs"))
    documents.append(load_html("https://residencehalls.alligator.org/#lakeside"))
    documents.append(load_html("https://residencehalls.alligator.org/#hume"))

    return documents

def ingest():
    documents = load_documents()
    print(f"loaded {len(documents)} documents.")
    return

def main():
    ingest()

if __name__ == "__main__":
    main()