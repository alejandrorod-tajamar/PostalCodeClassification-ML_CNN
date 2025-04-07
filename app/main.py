from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.model_loader import load_model, predict_digit
from app.utils import preprocess_image
from PIL import Image
import io

app = FastAPI()
model = load_model()

@app.get("/")
def read_root():
    return {"message": "API de reconocimiento de dígitos funcionando 🚀"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    processed = preprocess_image(image)
    prediction = predict_digit(model, processed)
    return JSONResponse(content={"prediction": prediction})
