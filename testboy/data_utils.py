import os

from tqdm import tqdm
from chromadb import Collection


def initialize_documents(
    documents_directory: str,
    chroma_collection: Collection
) -> None:
    # Read all files in the data directory
    documents = []
    metadatas = []
    files = os.listdir(documents_directory)
    for filename in files:
        with open(f"{documents_directory}/{filename}", "r") as file:
            documents.append(file.read())
            metadatas.append({
                "filename": filename,
                "usage": "testboy"
                })

    # Create ids from the current count
    count = chroma_collection.count()
    print(f"Collection contains {count} documents, adding extra {len(documents)} documents")
    ids = [str(i) for i in range(count, count + len(documents))]

    # Load the documents
    for i in tqdm(
        range(0, len(documents)), desc="Adding documents"
    ):
        results = chroma_collection.get(
            where={"filename": metadatas[i]["filename"]}, 
            include=[ "documents" ])
        if len(results['documents']) > 0:
            print(f"Document {metadatas[i]['filename']} already exists, skipping")
            continue
        chroma_collection.add(
            ids=ids[i],
            documents=documents[i],
            metadatas=metadatas[i],  # type: ignore
        )

    new_count = chroma_collection.count()
    print(f"Added {new_count - count} documents")