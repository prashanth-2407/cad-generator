import requests
import json
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FastEmbedEmbeddings


def scrape_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = [p.get_text() for p in soup.find_all("p")]
    code_blocks = [code.get_text() for code in soup.find_all("code")]

    return {
        "text": "\n".join(paragraphs),
        "code": "\n\n".join(code_blocks)
    }


# Scrape multiple pages for better coverage
urls = [
    "https://cadquery.readthedocs.io/en/latest/apireference.html",
    "https://cadquery.readthedocs.io/en/latest/primer.html",
    "https://cadquery.readthedocs.io/en/latest/examples.html",
]

docs = []
for url in urls:
    try:
        data = scrape_page(url)
        docs.append({
            "source": url,
            "content": data["text"],
            "code": data["code"]
        })
        print(f"Scraped: {url}")
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

with open("cadquery_docs.json", "w") as f:
    json.dump(docs, f)

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = []
for doc in docs:
    combined = doc["content"] + "\n\nCode:\n" + doc["code"]
    chunks.extend(splitter.split_text(combined))

print(f"Total chunks: {len(chunks)}")

# Build vector store
embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vector_db = FAISS.from_texts(chunks, embeddings)
vector_db.save_local("cadquery_index")

# Load and query
vector_db = FAISS.load_local(
    "cadquery_index",
    embeddings,
    allow_dangerous_deserialization=True
)

query = "create a hollow cylinder"
results = vector_db.similarity_search(query, k=1)

for r in results:
    print('start of result')
    print(r.page_content)
    print('end of result')
    print("---")