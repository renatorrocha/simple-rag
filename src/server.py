from fastapi import FastAPI, File
from typing import Annotated
from services.read_file import read_file

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

    return {
        "message": "Arquivo processado com sucesso!",
        "rows": extracted_data,
    }


@app.get("/health")
def health():
    return {"message": "OK"}
