from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database
import openai

app = FastAPI()

database.init_db()

class LectureCreate(BaseModel):
    title: str
    content: str

class QuestionRequest(BaseModel):
    lecture_id: int
    question: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Lecture Repository"}

@app.post("/upload")
def upload_lecture(lecture: LectureCreate):
    try:
        database.add_lecture(lecture.title, lecture.content)
        return {"status": "success", "message": f"Lecture '{lecture.title}' uploaded."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/lectures")
def get_all_lectures():
    lectures = database.get_lectures()

    return [{"id": l[0], "title": l[1]} for l in lectures]

# openai.api_key = "ТВОЙ_КЛЮЧ" 

@app.post("/ask")
def ask_question(req: QuestionRequest):
    lecture_content = database.get_lecture_content(req.lecture_id)
    if not lecture_content:
        raise HTTPException(status_code=404, detail="Lecture not found")

    prompt = f"""
    You are a professional student assistant at Innopolis. 
    The text of the training material is provided below. If the user has asked you a question, then answer the user's question based ONLY on this text. If the user told you to send him a task on a topic, then find the tasks in THIS PARTICULAR lecture text.
    If there is no answer in the text, say so.

    THE TEXT OF THE LECTURE:
    {lecture_content}

    QUESTION:
    {req.question}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"Sorry, I'm not connected to the API yet, but I found the lecture! It contains {len(lecture_content)} characters. Your question: {req.question}"

    database.save_interaction(req.lecture_id, req.question, answer)
    
    return {"answer": answer}

@app.get("/history/{lecture_id}")
def get_lecture_history(lecture_id: int):
    history = database.get_history(lecture_id)
    
    return [{"question": h[0], "answer": h[1]} for h in history]