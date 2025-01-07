import webbrowser
from fastapi import FastAPI
import uvicorn
import threading
from typing import Union

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Fungsi untuk membuka Swagger UI
def open_browser():
    webbrowser.open("http://127.0.0.1:8000/docs")

# Menjalankan thread untuk membuka browser sebelum menjalankan Uvicorn
threading.Thread(target=open_browser).start()

# Definisi route untuk root
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Definisi route untuk mengambil item berdasarkan item_id
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Menjalankan aplikasi FastAPI menggunakan Uvicorn
if __name__ == "__main__":
    # Jalankan aplikasi menggunakan Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
