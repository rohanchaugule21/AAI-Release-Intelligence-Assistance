import os
import json
import pickle
import faiss
import numpy as np

from pathlib import Path

from src.ingestion.doc_reader import read_docx
from src.ingestion.chunker import chunk_text

from sentence_transformers import (
    SentenceTransformer
)


model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

documents_path = r"documents"

all_chunks = []
metadata = []

for file in Path(documents_path).rglob("*.docx"):

    content = read_docx(file)

    chunks = chunk_text(content)

    for chunk in chunks:

        all_chunks.append(chunk)

        metadata.append({
            "file": file.name,
            "path": str(file),
            "chunk": chunk
        })

embeddings = model.encode(
    all_chunks,
    convert_to_numpy=True
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings.astype("float32")
)

faiss.write_index(
    index,
    "data/faiss/release_index.faiss"
)

with open(
    "data/metadata/metadata.pkl",
    "wb"
) as f:

    pickle.dump(metadata, f)