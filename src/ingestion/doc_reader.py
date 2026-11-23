from docx import Document


def read_docx(file_path):

    doc = Document(file_path)

    content = []

    # Paragraphs
    for para in doc.paragraphs:

        text = para.text.strip()

        if text:
            content.append(text)

    # Tables
    for table in doc.tables:

        content.append("\n=== TABLE ===")

        for row in table.rows:

            row_data = []

            for cell in row.cells:

                row_data.append(
                    cell.text.strip()
                )

            content.append(
                " | ".join(row_data)
            )

    return "\n".join(content)