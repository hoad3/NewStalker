from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Summary import Return_summary
from Topics import return_topic

app = FastAPI()

app.add_middleware(

    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


# Tạo một lớp Pydantic để đại diện cho dữ liệu đầu vào
class DataItem(BaseModel):
    text: str
    lang: str


# Định nghĩa endpoint POST để nhận dữ liệu và phân tích nó
@app.post("/analyze/")
async def analyze_data(data_item: DataItem):
    text_summary = data_item.text

    topic = return_topic(text_summary)
    summary = Return_summary(text_summary)
    # Trả về kết quả phân tích
    return {
        "summarized": summary,  # Gọi hàm để lấy tóm tắt
        "keywords": topic  # Gọi hàm để lấy chủ đề
    }


@app.get("/")
async def redirect_to_swagger():
    return RedirectResponse("/docs#/default/analyze_data_analyze__post")


PORT = 42069

# Mở thực thi ứng dụng FastAPI
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=PORT)
