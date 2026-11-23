import json
from pathlib import Path

from src.ingestion.doc_reader import read_docx

from src.ingestion.metadata_extractor import (
    extract_release_number,
    extract_release_version,
    extract_airport
)

# ==========================================================
# PROJECT PATHS
# ==========================================================

ROOT = Path(
    r"C:\Users\Rohan.Chaugule\Documents\Github\ReleaseIntelligence"
)

DOCUMENTS_FOLDER = ROOT / "documents"

DATA_FOLDER = ROOT / "data"

OUTPUT_FILE = DATA_FOLDER / "release_notes.json"

# ==========================================================
# CREATE DATA FOLDER
# ==========================================================

DATA_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# START
# ==========================================================

print("\n")
print("=" * 100)
print("RELEASE INTELLIGENCE DOCUMENT LOADER")
print("=" * 100)

print(f"\nScanning Folder: {DOCUMENTS_FOLDER}")

docx_files = list(
    DOCUMENTS_FOLDER.rglob("*.docx")
)

print(
    f"Found {len(docx_files)} docx files"
)

documents = []

for file in docx_files:

    try:

        print(
            f"Reading : {file.name}"
        )

        document_text = read_docx(
            file
        )

        record = {

            "filename":
                file.name,

            "filepath":
                str(file),

            "release_number":
                extract_release_number(
                    file.name
                ),

            "release_version":
                extract_release_version(
                    file.name
                ),

            "airport":
                extract_airport(
                    str(file.parent)
                ),

            "content":
                document_text
        }

        documents.append(
            record
        )

    except Exception as ex:

        print(
            f"Failed: {file.name}"
        )

        print(ex)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as fp:

    json.dump(
        documents,
        fp,
        indent=4,
        ensure_ascii=False
    )

print("\n")
print("=" * 100)
print(
    f"Loaded {len(documents)} Release Notes"
)
print(
    f"Saved To : {OUTPUT_FILE}"
)
print("=" * 100)