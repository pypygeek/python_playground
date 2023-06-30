from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id:str
    content:str

memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '성공'

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content=req_memo.content
            return '변경 완료'
    return '메모를 찾을 수 없습니다.'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    # enumerate : 배열에 인덱스와 값을 같이 뽑아주는 함수
    for index,memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)
            return '변경 완료'
    return '메모를 찾을 수 없습니다.'

app.mount("/", StaticFiles(directory='static', html=True), name='stattic')