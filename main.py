from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from mlAusCar.utils.common import filter_choices
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
async def train_route(): # Route to train
    os.system("python run.py")
    # os.system("dvc repro")
    return {"message": "Training done successfully!"}

@app.post("/config") # Route to get return the possible configurations of the car based on currently selected features
async def get_config(request: Request):
    data = await request.json()
    return filter_choices(data)

@app.post("/predict")  # route to show the predictions in a web UI
async def predict(request: Request,
            # year: int = Form(...),
            # model: str = Form(...),
            # usedornew: str = Form(...),
            # transmission: str = Form(...),
            # displacement: float = Form(...),
            # drivetype: str = Form(...),
            # fueltype: str = Form(...),
            # fuelconsumption: float = Form(...),
            # kilometers: int = Form(...),
            # cylinders: int = Form(...),
            # bodytype: str = Form(...),
            # location: str = Form(...)
            ):
    data = await request.json()
    return data
    try:
        data = pd.DataFrame({
                        'Year': [year],
                        'Model': [model],
                        'UsedOrNew': [usedornew],
                        'Transmission': [transmission],
                        'EngineDisplacement(L)': [displacement],
                        'DriveType': [drivetype],
                        'FuelType': [fueltype],
                        'FuelConsumption(L)/100km': [fuelconsumption],
                        'Kilometers': [kilometers],
                        'CylindersinEngine': [cylinders],
                        'BodyType': [bodytype],
                        'State': [location]
                    })
        # return data
        obj = PredictionPipeline(model_path='XG Boost model.pkl')
        prediction = obj.predict(data)

        return templates.TemplateResponse('results.html', {"request": request, "prediction": str(np.exp(prediction))})

    except Exception as e:
        print('The Exception message is: ', e)
        return 'something is wrong'

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="localhost", port=8080, reload=True)