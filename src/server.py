from fastapi import FastAPI, File
from typing import Annotated
from services.read_file import read_file
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

app = FastAPI(
    title="Maid API",
    description="API for the Maid app",
    version="0.1.0",
    contact={
        "name": "Maid API",
        "url": "https://maid.com",
    },
)


@app.post("/generate-embeddings")
async def generate_embeddings(
    file: Annotated[bytes, File()],
):
    extracted_data = read_file(file)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(extracted_data)

    return {
        "message": "Arquivo processado com sucesso!",
        "rows": chunks,
    }


@app.get("/health")
def health():
    return {"message": "OK"}
