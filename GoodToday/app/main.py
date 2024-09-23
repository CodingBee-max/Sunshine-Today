from fastapi import FastAPI, HTTPException
from model import NoteRequest

app = FastAPI()


@app.get("/")
async def root():
    docs_path = 'http://127.0.0.1:8000/docs'
    return f"Hello welcome to the Currency Forecast API. Visit {docs_path} to try out."


@app.post("/api/notes")
async def create_note(notes_data: NoteRequest):
    if not notes_data.content:
        raise HTTPException(
            status_code=400, detail='Bad request. Content field not added')
    title = notes_data.title
    content = notes_data.content
    return {
        "title": title,
        "content": content,
    }
