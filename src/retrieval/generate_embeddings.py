import json
import numpy as np
from pathlib import Path

from sentence_transformers import SentenceTransformer

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

CHUNK_FILE = ROOT / "data" / "chunks.json"

EMBEDDING_FILE = ROOT / "data" / "embeddings.npy"

METADATA_FILE = ROOT / "data" / "metadata.json"

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Loading chunks...")

with open(
    CHUNK_FILE,
    "r",
    encoding="utf-8"
) as fp:

    chunks = json.load(fp)

texts = []

for chunk in chunks:

    texts.append(
        chunk["content"]
    )

print(
    f"Generating embeddings for {len(texts)} documents..."
)

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    convert_to_numpy=True
)

np.save(
    EMBEDDING_FILE,
    embeddings
)

with open(
    METADATA_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        chunks,
        fp,
        indent=4,
        ensure_ascii=False
    )

print("\nDone.")
print(
    f"Embeddings Shape: {embeddings.shape}"
)