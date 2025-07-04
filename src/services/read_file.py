import tempfile
from langchain_community.document_loaders import CSVLoader
import os


def read_file(file_bytes: bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        temp_file.write(file_bytes)
        temp_path = temp_file.name

    try:
        loader = CSVLoader(file_path=temp_path)
        documents = loader.load()

        extracted_data = []
        for doc in documents:
            extracted_data.append(doc.page_content)

        return extracted_data
    finally:
        os.unlink(temp_path)
