from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import numpy as np
import pandas as pd
import os
from fastapi.templating import Jinja2Templates
from mlAusCar.pipeline.prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

templates = Jinja2Templates(directory="templates")  
app = FastAPI()

# Mounting CSS and JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you might want to limit this to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClientApp:
    def __init__(self):
        pass
    
clApp = ClientApp()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def train_route():
    os.system("python run.py")
    # os.system("dvc repro")
    return {"message": "Training done successfully!"}

@app.post("/predict")  # route to show the predictions in a web UI
def predict(request: Request, 
            Brand: str = Form(...),
            Year: int = Form(...),
            Model: str = Form(...),
            UsedOrNew: str = Form(...),
            Transmission: str = Form(...),
            EngineDisplacementL: float = Form(...),
            DriveType: str = Form(...),
            FuelType: str = Form(...),
            FuelConsumption: float = Form(...),
            Kilometers: int = Form(...),
            CylindersinEngine: int = Form(...),
            BodyType: str = Form(...),
            Location: str = Form(...)
            ):
    try:
        # data = [Year, Model, UsedOrNew, Transmission, EngineDisplacementL,
        #         DriveType, FuelType, FuelConsumption, Kilometers, CylindersinEngine,
        #         Location, BodyType]
        # data = np.array(data).reshape(1, 12)
        data = pd.DataFrame({
                        'Year': [Year],
                        'Model': [Model],
                        'UsedOrNew': [UsedOrNew],
                        'Transmission': [Transmission],
                        'EngineDisplacement(L)': [EngineDisplacementL],
                        'DriveType': [DriveType],
                        'FuelType': [FuelType],
                        'FuelConsumption(L)/100km': [FuelConsumption],
                        'Kilometers': [Kilometers],
                        'CylindersinEngine': [CylindersinEngine],
                        'State': [Location],
                        'BodyType': [BodyType],
                    })
        obj = PredictionPipeline(model_path='XG Boost model.pkl')
        prediction = obj.predict(data)

        return templates.TemplateResponse('results.html', {"request": request, "prediction": str(np.exp(prediction))})

    except Exception as e:
        print('The Exception message is: ', e)
        return 'something is wrong'

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)